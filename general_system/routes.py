from flask import render_template, request, flash, redirect, url_for
from flask_login import logout_user, login_user, current_user, login_required
from general_system import app, data_base, bcrypt
from general_system.forms import FormCreateAccount, FormLogin, FormEditProfile
from general_system.models import Usuario


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/atividades')
@login_required
def works():
    return render_template('works.html')


@app.route("/register_login", methods=['GET', 'POST'])
def register_login():
    form_account = FormCreateAccount()
    form_login = FormLogin()

    if form_account.validate_on_submit() and "button_submit_account" in request.form:
        password_encrypted = bcrypt.generate_password_hash(form_account.password.data)
        people = Usuario(username=form_account.username.data, email=form_account.email.data,
                         password=password_encrypted)
        data_base.session.add(people)
        data_base.session.commit()
        flash(f'Cadastro de {form_account.username.data} realizado com sucesso.', 'alert-success')
        return redirect(url_for('home'))

    if form_login.validate_on_submit() and "button_submit_login" in request.form:
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.password, form_login.password.data):
            login_user(usuario, remember=form_login.remember_password.data)
            flash(f'Login feito com sucesso no e-mail: {form_login.email.data}', 'alert-success')
            next_parameter = request.args.get('next')
            if next_parameter:
                return redirect(next_parameter)
            else:
                return redirect(url_for('home'))
        else:
            flash(f'Falha no Login. E-mail ou Senha Incorretos.', 'alert-danger')

    return render_template('register_login.html', form_account=form_account, form_login=form_login)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash(f'Logout realizado com sucesso!', 'alert-success')
    return redirect(url_for('home'))


@app.route('/my_profile')
@login_required
def my_profile():
    image_id = url_for('static', filename='image_id_user/{}'.format(current_user.perf_photo))
    return render_template('my_profile.html', image_id=image_id)


@app.route("/my_profile/edit_profile", methods=['GET', 'POST'])
@login_required
def edit_profile():
    form_profile = FormEditProfile()
    image_id = url_for('static', filename='image_id_user/{}'.format(current_user.perf_photo))
    return render_template('edit_profile.html', image_id=image_id, form_profile=form_profile)


@app.route("/post/create", methods=['GET', 'POST'])
@login_required
def create_post():
    return render_template('create_posts.html')


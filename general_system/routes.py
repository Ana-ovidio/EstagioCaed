from flask import render_template, request, flash, redirect, url_for
from general_system import app, data_base, bcrypt
from general_system.forms import FormCreateAccount, FormLogin
from general_system.models import Usuario


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/atividades')
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
            return redirect(url_for('home'))
        else:
            flash(f'Falha no Login. E-mail ou Senha Incorretos.', 'alert-danger')

    return render_template('register_login.html', form_account=form_account, form_login=form_login)

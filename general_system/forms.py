from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from general_system.models import Usuario, Post
from flask_login import current_user


class FormCreateAccount(FlaskForm):
    username = StringField('Nome de usuário:', validators=[DataRequired()])
    email = StringField('E-mail:', validators=[DataRequired(), Email()])
    password = PasswordField('Senha:', validators=[DataRequired(), Length(6, 20)])
    confirmation_password = PasswordField('Confirmar senha:', validators=[DataRequired(), EqualTo('password')])
    description = StringField('Descrição', validators=[DataRequired()])
    button_submit_account = SubmitField('Criar uma conta')


    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado. Cadastre-se com outro e-mail ou faça login para continuar')


class FormLogin(FlaskForm):
    email = StringField('E-mail:', validators=[DataRequired(), Email()])
    password = PasswordField('Senha:', validators=[DataRequired(), Length(6, 20)])
    remember_password = BooleanField('Aceita relembrar os dados de acesso')
    button_submit_login = SubmitField('Entrar')


class FormEditProfile(FlaskForm):
    username = StringField('Nome de usuário:', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    description = StringField('Descrição', validators=[DataRequired()])
    error_message = 'Extensão inválida, insira arquivos com jpeg, jpg, jfif ou png.'
    photo_profile = FileField('Atualizar foto de perfil: ', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'jfif'],
                                                                                    message=error_message)])
    button_submit_edit_profile = SubmitField('Confirmar Edição')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('E-mail já cadastrado. Por gentileza, inclua outro email.')


class FormCreatePost(FlaskForm):
    title = StringField('Título do post', validators=[DataRequired(), Length(2, 140)])
    body_text = TextAreaField('Escreva seu post aqui: ', validators=[DataRequired()])
    button_submit_create_post = SubmitField('Criar Post')
    button_submit_edit_post = SubmitField('Editar Post')

    work_change_genre = BooleanField('Trocar de gênero')
    work_change_adjective = BooleanField('Trocar adjetivos por sinônimo/antônimos')
    work_paraphrase1 = BooleanField('Paráfrase i')
    work_paraphrase2 = BooleanField('Paráfrase ii')
    work_paraphrase3 = BooleanField('Paráfrase iii')
    work_canonical = BooleanField('Palavras canônicas')

    def validate_title(self, title):
        current_title = title.data
        post = Post.query.filter_by(title=current_title).first()
        if post:
            raise ValidationError('Este título já está registrado. Por favor, insira outro título.')

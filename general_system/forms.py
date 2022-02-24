from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from general_system.models import Usuario


class FormCreateAccount(FlaskForm):
    username = StringField('Nome de usuário:', validators=[DataRequired()])
    email = StringField('E-mail:', validators=[DataRequired(), Email()])
    password = PasswordField('Senha:', validators=[DataRequired(), Length(6, 20)])
    confirmation_password = PasswordField('Confirmar senha:', validators=[DataRequired(), EqualTo('password')])
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

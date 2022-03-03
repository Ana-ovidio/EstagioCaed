from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = '49efa731a11117e6df6df72f3c63d7b5'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Atividades_Caed.db'

data_base = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'register_login'
login_manager.login_message_category = 'alert-info'
login_manager.login_message = 'Faça o Login para prosseguir'


# it is necessary app to routes work correctly.
from general_system import routes
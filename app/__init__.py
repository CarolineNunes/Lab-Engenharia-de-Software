from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)  # instância da minha aplicacao
app.config['SECRET_KEY'] = 'b843c6cf3ef9cedcd0fbd635b84f17ae'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)  # cria uma instancia da base de dados
bcrypt = Bcrypt(app)  # hash das senhas
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from app import routes


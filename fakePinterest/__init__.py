from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "os.getenv('DATABASE_URL')"
app.config["SECRET_KEY"] = "7973ff729a436b6e9409b8276072788d"
app.config["UPLOAD_FOLDER"] = "static/fotos_posts"
database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"
from fakePinterest import routes

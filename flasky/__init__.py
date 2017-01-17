import os

import pbr.version
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_login import LoginManager

__version__ = pbr.version.VersionInfo(
    'flasky').version_string()

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = '\xe2\x0c\xed\x96\x15\xe9\xc6\x0f\xcf\x1f\xd5\xc3\xfa\xaf\xac\x91~?4n\xde\xbc\xe2\\'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'flasky.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# Configure authentication
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
login_manager.init_app(app)

# For displaying timestamps
moment = Moment(app)

import models
import views
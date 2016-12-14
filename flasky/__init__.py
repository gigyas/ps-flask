import pbr.version


__version__ = pbr.version.VersionInfo(
    'flasky').version_string()

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = '\xe2\x0c\xed\x96\x15\xe9\xc6\x0f\xcf\x1f\xd5\xc3\xfa\xaf\xac\x91~?4n\xde\xbc\xe2\\'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'flasky.db')
db = SQLAlchemy(app)

import models
import views
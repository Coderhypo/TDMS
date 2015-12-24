# coding=utf-8
import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from config import config

__author__ = 'hypo'

app = Flask(__name__)
db = SQLAlchemy(use_native_unicode="utf8")

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'

with app.app_context():
    config_name = os.getenv('CONFIG') or 'default'
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(userid):
        return Users.query.filter_by(user_id=int(userid)).first()


from .views import *
from .devices import *
from .users import *
from .logs import *
from .api import *
from .search import *
from models import Users
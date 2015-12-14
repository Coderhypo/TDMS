# coding=utf-8
import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from config import config

__author__ = 'hypo'

app = Flask(__name__)
db = SQLAlchemy(use_native_unicode="utf8")

with app.app_context():
    config_name = os.getenv('CONFIG') or 'default'
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

from .views import *
from .devices import *
from .users import *
from .logs import *
from .api import *

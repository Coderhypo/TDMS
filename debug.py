#!/usr/bin/env python
# coding=utf-8
from flask.ext.script import Manager
from app import app
from app.models import *

manager = Manager(app)

manager.run()

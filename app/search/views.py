# coding=utf-8
from app import app
from flask import render_template, request
from flask.ext.login import login_required, current_user

from app.models import Devices, Users, LendLogs

__author__ = 'hypo'


@app.route('/admin/search')
@login_required
def search():
    pass
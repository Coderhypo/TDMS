# coding=utf-8
from app import app
from flask import render_template, request
from flask.ext.login import login_required, current_user

from app.models import Devices, Users, LendLogs

__author__ = 'hypo'


@app.route('/admin/search')
@login_required
def search():
    if request.method == 'POST':
        info = request.args.get('info', '')


def search_user(info):
    pass


def search_device(info):
    pass


def search_log(info):
    pass

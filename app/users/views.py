# coding=utf-8
from app import app
from flask import render_template

__author__ = 'hypo'


@app.route('/admin/users')
def users():

    """用户管理界面"""

    return render_template('/admin/users/usermanage.html')


@app.route('/admin/schools')
def schools():

    """学院管理 管理员权限"""

    return render_template('/admin/users/schoolmanage.html')


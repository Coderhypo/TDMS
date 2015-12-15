# coding=utf-8
from app import app
from flask import render_template

__author__ = 'hypo'


@app.route('/')
def index():

    """首页"""

    return render_template('base.html')


@app.route('/login')
def login():

    """登录"""

    return render_template('login.html')


@app.route('/logout')
def logout():

    """登出"""

    return render_template('base.html')


@app.route('/admin')
def admin():

    """后台主页"""

    return render_template('/admin/index.html')

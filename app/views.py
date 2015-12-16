# coding=utf-8
from flask.ext.login import login_user, logout_user
from app import app
from app.models import Users
from flask import render_template, request, redirect, url_for, flash

__author__ = 'hypo'


@app.route('/')
def index():

    """首页"""

    return render_template('base.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    """登录"""
    if request.method == 'POST':
        userlogin = request.form['login']
        password = request.form['password']

        user = Users.query.filter_by(user_login=userlogin).first()
        if user is not None and user.verify_password(password):
            print 'HELLO'
            remember = True if 'remember' in request.form else False
            login_user(user, remember)
            return redirect(url_for('admin'))

    return render_template('login.html')


@app.route('/logout')
def logout():

    """登出"""
    logout_user()
    flash('登出成功！')

    return render_template('login.html')


@app.route('/admin')
def admin():

    """后台主页"""

    return render_template('/admin/index.html')

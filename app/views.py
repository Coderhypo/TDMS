# coding=utf-8
__author__ = 'hypo'

from app import app
from flask import render_template


@app.route('/')
def index():

    """首页"""

    return render_template('base.html')


@app.route('/login')
def login():

    """登录"""

    return render_template('base.html')


@app.route('/logout')
def logout():

    """登出"""

    return render_template('base.html')


@app.route('/admin')
def admin():

    """后台主页"""

    return render_template('/admin/index.html')


@app.route('/admin/lend')
def lend():

    """设备借出页面"""

    return render_template('/admin/devices/lenddevice.html')


@app.route('/admin/return')
def reDevices():

    """归还设备页面"""

    return render_template('/admin/devices/returndevice.html')


@app.route('/admin/devices')
def devices():

    """设备管理页面"""

    return render_template('/admin/devices/devicemanage.html')


@app.route('/admin/users')
def users():

    """用户管理界面"""

    return render_template('/admin/users/usermanage.html')


@app.route('/admin/lendlogs')
def lendLogs():

    """设备借出归还日志"""

    return render_template('/admin/logs/lendlogs.html')


@app.route('/admin/schools')
def schools():

    """学院管理 管理员权限"""

    return render_template('/admin/users/schoolmanage.html')


@app.route('/admin/logs')
def logs():

    """系统日志 管理员权限"""

    return render_template('/admin/logs/logmanage.html')

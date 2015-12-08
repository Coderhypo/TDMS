# coding=utf-8
from app import app
from flask import render_template

__author__ = 'hypo'


@app.route('/admin/lendlogs')
def lendLogs():

    """设备借出归还日志"""

    return render_template('/admin/logs/lendlogs.html')


@app.route('/admin/logs')
def logs():

    """系统日志 管理员权限"""

    return render_template('/admin/logs/logmanage.html')

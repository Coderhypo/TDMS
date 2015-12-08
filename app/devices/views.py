# coding=utf-8
from app import app
from flask import render_template

__author__ = 'hypo'


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


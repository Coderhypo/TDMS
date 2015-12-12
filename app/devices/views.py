# coding=utf-8
from app import app
from app.models import Devices
from flask import render_template, request, redirect, url_for

from .devices import DeviceInfo
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

    list = []
    devices = Devices.query.all()

    for device in devices:
        tmp = {'id': device.device_id, 'name': device.device_name}

        if device.device_status == 0:
            tmp['status'] = u'正常'
        elif device.device_status == 1:
            tmp['status'] = u'损坏'

        if device.lend_log_id == -1:
            tmp['lend'] = u'未借出'
        else:
            tmp['lend'] = u'已借出'

        list.append(tmp)

    return render_template('/admin/devices/devicemanage.html', list=list)


@app.route('/admin/adddevices', methods=['GET', 'POST'])
def addDevice():

    """添加设备页面"""

    if request.method == 'POST':
        num = 1
        while True:

            if 'devicename' + str(num) not in request.form:
                break

            devicename = request.form['devicename' + str(num)]

            if len(devicename) < 1:
                num += 1
                continue

            device = DeviceInfo()
            device.setName(devicename)
            device.getNewDevice()

            num += 1

    return redirect(url_for('devices'))


# coding=utf-8
from app import app, db
from app.models import Devices, Users, LendLogs
from flask import render_template, request, redirect, url_for
from flask.ext.login import current_user

from .devices import DeviceInfo
from app.logs import LendLog

__author__ = 'hypo'


@app.route('/admin/lend', methods=['GET'])
def lend():
    """设备借出页面"""

    if request.method == 'GET':

        if request.args.get('login') and request.args.get('deviceid'):

            login = request.args.get('login')
            deviceid = request.args.get('deviceid')
            device = Devices.query.filter_by(device_id=deviceid).first()
            doer = current_user.user_login
            if len(login) > 0 and len(deviceid) > 0 and device.lend_log_id == -1:
                user = Users.query.filter_by(user_login=login).first()

                lendlog = LendLog()
                lendlog.setDevice(deviceid)
                lendlog.setLender(user.user_id)
                lendlog.setDoer(doer.user_id)
                logid = lendlog.lendDevice()
                device.lend_log_id = logid

                db.session.add(device)
                db.session.commit()

    ulist = []
    users = Users.query.all()

    for user in users:
        tmp = {'id': user.user_id, 'login': user.user_login, 'name': user.user_name, 'phone': user.user_phone}
        ulist.append(tmp)

    dlist = []
    devices = Devices.query.filter_by(lend_log_id=-1).all()

    for device in devices:
        tmp = {'id': device.device_id, 'name': device.device_name}
        dlist.append(tmp)

    return render_template('/admin/devices/lenddevice.html', users=ulist, devices=dlist)


@app.route('/admin/return')
def reDevices():
    """归还设备页面"""

    if request.args.get('deviceid'):
        return redirect(url_for('upredev', deviceid=request.args.get('deviceid')))

    lendlogs = LendLogs.query.filter_by(return_time=None).all()
    users = []
    devices = []

    userlogin = request.args.get('login', 0)

    if userlogin != 0:
        chooseuser = Users.query.filter_by(user_login=userlogin).first()

    for lendlog in lendlogs:
        users.append(lendlog.lender_id)

        if userlogin == 0 or userlogin == '0':
            devices.append(lendlog.device_id)
        elif chooseuser.user_id == lendlog.lender_id:
            devices.append(lendlog.device_id)
    users = set(users)

    ulist = []
    for userid in users:
        user = Users.query.filter_by(user_id=userid).first()

        tmp = {'id': user.user_id, 'login': user.user_login, 'name': user.user_name, 'phone': user.user_phone}
        ulist.append(tmp)

    dlist = []
    for deviceid in devices:
        device = Devices.query.filter_by(device_id=deviceid).first()
        tmp = {'id': device.device_id, 'name': device.device_name}
        dlist.append(tmp)

    return render_template('/admin/devices/returndevice.html', users=ulist, devices=dlist)


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
        elif device.device_status == 2:
            tmp['status'] = u'丢失'

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
        doer = current_user.user_login
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


@app.route('/admin/updatedevice', methods=['GET', 'POST'])
def updateDevice():
    """更新设备页面"""

    if request.method == 'POST':
        doer = current_user.user_login
        if 'update' == request.form['type']:
            id = request.form['editid']
            device = DeviceInfo()
            device.setName(request.form['editname'])
            device.setStatus(request.form['status'])
            device.updateDevice(id)
        elif 'delete' == request.form['type']:
            id = request.form['delid']
            device = DeviceInfo()
            device.deleteDevice(id)

    return redirect(url_for('devices'))


@app.route('/admin/upredev', methods=['GET', 'POST'])
def upredev():

    device = Devices.query.filter_by(device_id=request.args.get('deviceid')).first()

    if request.method == 'POST':
        doer = current_user.user_login
        lendlog = LendLog()
        lendlog.setDoer(doer.user_id)
        lendlog.returnDevice(device.lend_log_id)

        device.lend_log_id = -1
        device.device_status = request.form['status']
        db.session.add(device)
        db.session.commit()

        return redirect(url_for('reDevices'))

    deviceinfo = {'id': device.device_id, 'name': device.device_name}

    return render_template('/admin/devices/updatedevice.html', device=deviceinfo)

# coding=utf-8
from app import app
from app.models import LendLogs, Devices, Users
from flask import render_template, request

__author__ = 'hypo'


@app.route('/admin/lendlogs')
def lendLogs():

    """设备借出归还日志"""
    show = request.args.get('show', 'all')

    if show == 'return':
        lends = LendLogs.query.filter(LendLogs.return_time!=None).all()
    elif show == 'unreturn':
        lends = LendLogs.query.filter_by(return_time=None).all()
    else:
        lends = LendLogs.query.all()
    list = []

    for lend in lends:
        tmp = {'id': lend.log_id, 'lendtime': lend.lend_time}
        lender = Users.query.filter_by(user_id=lend.lender_id).first()
        doer = Users.query.filter_by(user_id=lend.lender_id).first()
        device = Devices.query.filter_by(device_id=lend.device_id).first()
        tmp['lender'] = lender.user_name
        tmp['doer'] = doer.user_name
        tmp['device'] = device.device_name
        if lend.return_time is None:
            tmp['returntime'] = u'未归还'
        else:
            tmp['returntime'] = lend.return_time
        list.append(tmp)

    return render_template('/admin/logs/lendlogs.html', list=list)


@app.route('/admin/logs')
def logs():

    """系统日志 管理员权限"""

    return render_template('/admin/logs/logmanage.html')

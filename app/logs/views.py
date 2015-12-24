# coding=utf-8
from sqlalchemy import desc
from app import app
from app.models import LendLogs, Devices, Users, Logs
from flask import render_template, request
from flask.ext.login import current_user

__author__ = 'hypo'


@app.route('/admin/lendlogs')
def lendLogs():

    """设备借出归还日志"""
    show = request.args.get('show', 'all')
    doer = current_user

    uid = request.args.get('uid', -1)
    did = request.args.get('did', -1)

    if show == 'return':
        lends = LendLogs.query.filter(LendLogs.return_time!=None).filter_by(school_id=doer.school_id).order_by(desc(LendLogs.lend_time))
    elif show == 'unreturn':
        lends = LendLogs.query.filter_by(return_time=None, school_id=doer.school_id).order_by(desc(LendLogs.lend_time))
    else:
        lends = LendLogs.query.filter_by(school_id=doer.school_id).order_by(desc(LendLogs.lend_time))

    if uid != -1:
        lends = lends.filter_by(lender_id=uid)

    if did != -1:
        lends = lends.filter_by(device_id=did)

    lends = lends.all()

    list = []

    for lend in lends:
        tmp = {'id': lend.log_id, 'lendtime': lend.lend_time}
        lender = Users.query.filter_by(user_id=lend.lender_id).first()
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
    doer = current_user
    if doer.school_id != 1:
        return u'没有访问权限'

    logs = Logs.query.all()

    list = []

    for log in logs:
        tmp = {'id': log.log_id, 'type': log.log_type, 'content': log.log_content, 'logtime': log.log_time,
               'user': log.user_id, 'device': log.device_id}

        list.append(tmp)

    return render_template('/admin/logs/logmanage.html', list=list)

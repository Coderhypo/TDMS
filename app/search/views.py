# coding=utf-8
from app import app
from flask import render_template, request, url_for, redirect
from flask.ext.login import login_required, current_user

from app.models import Devices, Users

__author__ = 'hypo'


@app.route('/admin/search', methods=['GET', 'POST'])
@login_required
def search():
    if request.method == 'POST':
        info = request.args.get('info', '')

        ulist = search_user(info)
        dlist = search_device(info)

        return render_template('admin/search.html', ulist=ulist, dlist=dlist)

    return redirect(url_for('admin'))


def search_user(info):
    list = []
    doer = current_user

    users = Users.query.filter_by(school_id=doer.school_id).filter(Users.user_name.ilike('%' + info + '%')).all()
    users += Users.query.filter_by(school_id=doer.school_id).filter(Users.user_login.ilike('%' + info + '%')).all()

    for user in users:
        tmp = {'id': user.user_id, 'login': user.user_login, 'name': user.user_name, 'phone': user.user_phone}
        list.append(tmp)

    return list


def search_device(info):
    list = []
    doer = current_user

    devices = Devices.query.filter_by(school_id=doer.school_id).filter(Devices.device_id.ilike('%' + info + '%')).all()
    devices += Devices.query.filter_by(school_id=doer.school_id).filter(Devices.device_name.ilike('%' + info + '%')).all()

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

    return list


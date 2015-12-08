# coding=utf-8
from app import app
from app.models import Devices
from flask import jsonify, request

__author__ = 'hypo'


@app.route('/api/device', methods=['GET'])
def device():
    rnt = {}

    if request.method == 'GET':
        deviceid = request.args.get('id', 0)
        status = request.args.get('sid', 0)

        if deviceid != 0:
            device = Devices.query.filter_by(device_id=deviceid).first()
            if device is not None:
                rnt = {'id': device.device_id, 'name': device.device_name, 'type_id': device.device_type_id,
                       'status': device.device_status, 'school_id': device.school_id, 'log_id': device.lend_log_id}

        if status != 0:
            devices = Devices.query.filter_by(device_status=status).all()
            rnt = []
            for device in devices:
                tmp = {'id': device.device_id, 'name': device.device_name, 'type_id': device.device_type_id,
                       'status': device.device_status, 'school_id': device.school_id, 'log_id': device.lend_log_id}
                rnt.append(tmp)

    return jsonify(rnt)

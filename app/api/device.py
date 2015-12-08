# coding=utf-8
import json
from app import app
from app.models import Devices
from flask import request

__author__ = 'hypo'


@app.route('/api/device', methods=['GET'])
def device():
    rnt = {}

    if request.method == 'GET':
        deviceid = request.args.get('did', 0)
        status = request.args.get('sid', 0)

        if deviceid != 0:
            device = Devices.query.filter_by(device_id=deviceid).first()
            if device is not None:
                rnt = device.to_json()

        if status != 0:
            devices = Devices.query.filter_by(device_status=status).all()
            rnt = []
            for device in devices:
                tmp = device.to_json()
                rnt.append(tmp)

    return json.dumps(rnt)

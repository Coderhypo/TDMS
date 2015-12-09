# coding=utf-8
import json
from app import app
from app.models import Devices
from flask import request

__author__ = 'hypo'


@app.route('/api/device/<int:deviceid>', methods=['GET'])
def device(deviceid):
    rnt = {}

    if request.method == 'GET':

        if deviceid != 0:
            device = Devices.query.filter_by(device_id=deviceid).first()
            if device is not None:
                rnt = device.to_json()

    return json.dumps(rnt)


@app.route('/api/devices/<int:status>', methods=['GET'])
def devicestatus(status):
    rnt = []

    if request.method == 'GET':

        if status != 0:
            devices = Devices.query.filter_by(device_status=status).all()
            for device in devices:
                tmp = device.to_json()
                rnt.append(tmp)

    return json.dumps(rnt)
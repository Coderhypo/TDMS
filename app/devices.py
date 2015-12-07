# coding=utf-8
from app import db
from app.models import Devices

__author__ = 'hypo'

class DeviceInfo():

    __device_name = 'NONE'
    __device_type_id = 1
    __device_status = 0
    __school_id = -1
    __lend_log_id = -1

    def setName(self, name):
        self.__device_name = name

    def setStatus(self, status):
        self.__device_status = status

    def setSchool(self,schoolid):
        self.__school_id = schoolid

    def setLendLogId(self, logid):
        self.__lend_log_id = logid

    def getDevice(self):

        device = Devices()
        device.device_name = self.__device_name
        device.device_type_id = self.__device_type_id
        device.device_status = self.__device_status
        device.school_id = self.__school_id
        device.lend_log_id = self.__lend_log_id

        db.session.add(device)
        db.session.commit()

        return device


class Device():

    __device = 0

    def __init__(self, id):
        self.__device = Devices.query.filter_by(device_id=id).first()

    def __init__(self, deviceinfo):
        self.__device = deviceinfo.getDevice()



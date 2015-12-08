# coding=utf-8
from app import db
from app.logs.logs import LendLog
from app.models import Devices

__author__ = 'hypo'


class DeviceInfo:

    """
    设备信息类
    用来创建新设备信息记录
    getNewDevice 获得新设备并持久化
    updateDevice 更新设备信息
    deleteDevice 删除设备
    """

    def __init__(self):
        pass

    __device_name = 'NONE'
    __device_type_id = 1
    __device_status = 0
    __school_id = -1
    __lend_log_id = -1

    def setName(self, name):
        self.__device_name = name

    def setStatus(self, status):
        self.__device_status = status

    def setSchool(self, schoolid):
        self.__school_id = schoolid

    def setLendLogId(self, logid):
        self.__lend_log_id = logid

    def getNewDevice(self):
        device = Devices()
        device.device_name = self.__device_name
        device.device_type_id = self.__device_type_id
        device.device_status = self.__device_status
        device.school_id = self.__school_id
        device.lend_log_id = self.__lend_log_id

        db.session.add(device)
        db.session.commit()

        return device

    def updateDevice(self, id):
        device = Devices.query.filter_by(device_id=id).first()

        device.device_name = self.__device_name
        device.device_type_id = self.__device_type_id
        device.device_status = self.__device_status
        device.school_id = self.__school_id
        device.lend_log_id = self.__lend_log_id

        db.session.add(device)
        db.session.commit()

    def deleteDevice(self, id):
        device = Devices.query.filter_by(device_id=id).first()

        db.session.delete(device)
        db.session.commiit()


class Device:

    """
    设备类
    用来处理借出，归还等业务逻辑
    lendDevice 借出设备
    returnDevice 归还设备
    """

    __device = 0

    def __init__(self, id):
        self.__device = Devices.query.filter_by(device_id=id).first()

    def lendDevice(self, lender, doer):
        lendlog = LendLog()
        lendlog.setDevice(self.__device.device_id)
        lendlog.setLender(lender)
        lendlog.setDoer(doer)
        lendlog.lendDevice()

    def returnDevice(self, lender, doer):
        lendlog = LendLog()
        lendlog.setDevice(self.__device.device_id)
        lendlog.setLender(lender)
        lendlog.setDoer(doer)
        lendlog.returnDevice(self.__device.lend_log_id)

        self.__device.lend_log_id = None
        db.session.add(self.__device)
        db.session.commit()

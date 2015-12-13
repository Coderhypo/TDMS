# coding=utf-8
from datetime import datetime
from app import db
from app.models import LendLogs, Logs

__author__ = 'hypo'


class LendLog:

    """
    借出记录类
    用来描述设备的借出记录日志 所有记录对设备负责
    lendDevice 借出设备登记
    returnDevice 归还设备更新登记
    """

    __device_id = None
    __lender_id = None
    __doer_id = None
    __lend_time = None

    def __init__(self):
        pass

    def setDevice(self, id):
        self.__device_id = id

    def setLender(self, id):
        self.__lender_id = id

    def setDoer(self, id):
        self.__doer_id = id

    def lendDevice(self):
        log = LendLogs()
        log.device_id = self.__device_id
        log.lender_id = self.__lender_id
        log.doer_id = self.__doer_id
        log.lend_time = datetime.utcnow()
        log.return_time = None

        db.session.add(log)
        db.session.commit()

        return log.log_id

    def returnDevice(self, logid):
        log = LendLogs.query.filter_by(log_id=logid).first()
        log.doer_id = self.__doer_id
        log.return_time = datetime.utcnow()

        db.session.add(log)
        db.session.commit()


class Log:

    """
    系统日记类
    用来记录所有的用户行为日志 所有记录对用户负责
    loginLog 用户登录日志
    addUser 添加用户日志
    updateUser 更新用户日志
    deleteUser 删除用户日志
    addDevice 添加设备日志
    updateDevice 更新设备日志
    deleteDevice 删除设备日志
    lendDevice 借出设备日志
    returnDevice 归还设备日志
    info 自定义日志信息
    """

    __user_id = None
    __device_id = None
    __log_type = 'NONE'
    __log_content = 'NONE'

    def __init__(self):
        pass

    def setUser(self, id):
        self.__user_id = id

    def setDevice(self, id):
        self.__device_id = id

    def setType(self, type):
        self.__log_type = type

    def setContent(self, content):
        self.__log_content = content

    def loginLog(self):
        log = Logs()

        log.user_id = self.__user_id
        log.log_type = 'LOGIN'
        log.log_content = '用户 ' + self.__user_id + ' 登录系统成功'
        log.log_time = datetime.utcnow()

        db.session.add(log)
        db.session.commit()

    def addUser(self, userid):
        log = Logs()

        log.user_id = self.__user_id
        log.log_type = 'ADDUSER'
        log.log_content = '用户 ' + self.__user_id + ' 新增用户 ' + userid
        log.log_time = datetime.utcnow()

        db.session.add(log)
        db.session.commit()

    def updateUser(self, userid):
        log = Logs()

        log.user_id = self.__user_id
        log.log_type = 'UPDATEUSER'
        log.log_content = '用户 ' + self.__user_id + ' 更新用户 ' + userid + ' 信息'
        log.log_time = datetime.utcnow()

        db.session.add(log)
        db.session.commit()

    def deleteUser(self, userid):
        log = Logs()

        log.user_id = self.__user_id
        log.log_type = 'DELETEUSER'
        log.log_content = '用户 ' + self.__user_id + ' 删除了用户 ' + userid
        log.log_time = datetime.utcnow()

        db.session.add(log)
        db.session.commit()

    def addDevice(self):
        log = Logs()

        log.user_id = self.__user_id
        log.device_id = self.__device_id
        log.log_type = 'ADDDEVICE'
        log.log_content = '用户 ' + self.__user_id + ' 新增设备 ' + self.__device_id
        log.log_time = datetime.utcnow()

        db.session.add(log)
        db.session.commit()

    def updateDevice(self):
        log = Logs()

        log.user_id = self.__user_id
        log.device_id = self.__device_id
        log.log_type = 'UPDATEDEVICE'
        log.log_content = '用户 ' + self.__user_id + ' 更新了设备 ' + self.__device_id + ' 信息'
        log.log_time = datetime.utcnow()

        db.session.add(log)
        db.session.commit()

    def deleteDevice(self):
        log = Logs()

        log.user_id = self.__user_id
        log.device_id = self.__device_id
        log.log_type = 'DELETEDEVICE'
        log.log_content = '用户 ' + self.__user_id + ' 删除了设备 ' + self.__device_id
        log.log_time = datetime.utcnow()

        db.session.add(log)
        db.session.commit()

    def lendDevice(self, lenderid):
        log = Logs()

        log.user_id = self.__user_id
        log.device_id = self.__device_id
        log.log_type = 'LENDDEVICE'
        log.log_content = '用户 ' + lenderid + ' 借用设备 ' + self.__device_id + ' 操作人 ' + self.__user_id
        log.log_time = datetime.utcnow()

        db.session.add(log)
        db.session.commit()

    def returnDevice(self, lenderid):
        log = Logs()

        log.user_id = self.__user_id
        log.device_id = self.__device_id
        log.log_type = 'RETURNDEVICE'
        log.log_content = '用户 ' + lenderid + ' 归还设备 ' + self.__device_id + ' 操作人 ' + self.__user_id
        log.log_time = datetime.utcnow()

        db.session.add(log)
        db.session.commit()

    def info(self):
        log = Logs()

        log.user_id = self.__user_id
        log.device_id = self.__device_id
        log.log_type = self.__log_type
        log.log_content = self.__log_content
        log.log_time = datetime.utcnow()

        db.session.add(log)
        db.session.commit()

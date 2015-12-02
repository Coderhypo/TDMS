# coding=utf-8
__author__ = 'hypo'

from app import db


class Devices(db.Model):
    """设备表"""

    __tablename__ = 'devices'
    device_id = db.Column(db.Integer, primary_key=True)
    device_name = db.Column(db.String(60), nullable=False)
    device_type_id = db.Column(db.Integer, nullable=False)
    device_status = db.Column(db.Integer, nullable=False)
    school_id = db.Column(db.Integer, nullable=False)
    lend_log_id = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<Devices %r>' % self.device_id


class DeviceTypes(db.Model):
    """设备表类型"""

    __tablename__ = 'device_types'
    device_type_id = db.Column(db.Integer, primary_key=True)
    device_type_name = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return '<DeviceTypes %r>' % self.device_type_id


class Users(db.Model):
    """用户表"""

    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    user_login = db.Column(db.String(60), nullable=False, unique=True)
    user_name = db.Column(db.String(60), nullable=False)
    user_pass = db.Column(db.String(128), nullable=False)
    user_phone = db.Column(db.String(60), nullable=False)
    school_id = db.Column(db.Integer, nullable=False)
    user_rule = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return '<Users %r>' % self.user_login


class Schools(db.Model):
    """学院表"""

    __tablename__ = 'schools'
    school_id = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return '<Schools %r>' % self.school_name



class Logs(db.Model):
    """程序日志表"""

    __tablename__ = 'logs'
    log_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(60), nullable=False, unique=True)
    device_id = db.Column(db.String(60), nullable=False)
    log_type = db.Column(db.String(60), nullable=False)
    log_content = db.Column(db.Integer, nullable=False)
    log_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Logs %r>' % self.log_id


class LendLogs(db.Model):
    """借还日志表"""

    __tablename__ = 'lend_logs'
    log_id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String(60), nullable=False)
    lender_id = db.Column(db.String(60), nullable=False, unique=True)
    doer_id = db.Column(db.String(60), nullable=False, unique=True)
    lend_time = db.Column(db.DateTime, nullable=False)
    return_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<LendLogs %r>' % self.log_id

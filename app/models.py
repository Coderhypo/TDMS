# coding=utf-8
import hashlib
from app import db

__author__ = 'hypo'


class Devices(db.Model):
    """设备表"""

    __tablename__ = 'devices'
    device_id = db.Column(db.Integer, primary_key=True)
    device_name = db.Column(db.String(60), nullable=False)
    device_type_id = db.Column(db.Integer, db.ForeignKey('device_types.device_type_id'))
    device_status = db.Column(db.Integer, nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey('schools.school_id'))
    lend_log_id = db.Column(db.Integer, nullable=True)

    logs = db.relationship('Logs', backref='devices')
    lend_logs = db.relationship('LendLogs', backref='devices')

    def __repr__(self):
        return '<Devices %r>' % self.device_id

    def to_json(self):
        return {'id': self.device_id, 'name': self.device_name, 'type_id': self.device_type_id,
                'status': self.device_status, 'school_id': self.school_id, 'log_id': self.lend_log_id}


class DeviceTypes(db.Model):
    """设备表类型"""

    __tablename__ = 'device_types'
    device_type_id = db.Column(db.Integer, primary_key=True)
    device_type_name = db.Column(db.String(60), nullable=False)

    devices = db.relationship('Devices', backref='device_types')

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
    school_id = db.Column(db.Integer, db.ForeignKey('schools.school_id'))
    user_rule = db.Column(db.String(60), nullable=False)

    logs = db.relationship('Logs', backref='users')
    lend_logs = db.relationship('LendLogs', backref='users')

    def __repr__(self):
        return '<Users %r>' % self.user_login

    def to_json(self):
        return {'id': self.user_id, 'login': self.user_login, 'name': self.user_name,
                'phone': self.user_phone, 'school_id': self.school_id, 'log_id': self.user_rule}

    def get_id(self):
        return self.user_id

    def verify_password(self, password):
        password = hashlib.md5(password).hexdigest()
        if password == self.user_pass:
            return True
        return False

    def update_pass(self, password):
        self.user_pass = hashlib.md5(password + self.user_email).hexdigest()

    def is_active(self):
        if self.user_pass is not None:
            return True
        return False

    def is_root(self):
        if self.user_rule == 'ROOT':
            return True
        return False

    def is_admin(self):
        if self.user_rule == 'ADMIN':
            return True
        return False


class Schools(db.Model):
    """学院表"""

    __tablename__ = 'schools'
    school_id = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(60), nullable=False)

    users = db.relationship('Users', backref='schools')
    devices = db.relationship('Devices', backref='schools')
    lendLogs = db.relationship('LendLogs', backref='schools')

    def __repr__(self):
        return '<Schools %r>' % self.school_name


class Logs(db.Model):
    """程序日志表"""

    __tablename__ = 'logs'
    log_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    device_id = db.Column(db.Integer, db.ForeignKey('devices.device_id'))
    log_type = db.Column(db.String(60), nullable=False)
    log_content = db.Column(db.Integer, nullable=False)
    log_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Logs %r>' % self.log_id

    def to_json(self):
        return {'id': self.log_id, 'user': self.user_id, 'device': self.device_id,
                'type': self.log_type, 'content': self.log_content, 'time': self.log_time}


class LendLogs(db.Model):
    """借还日志表"""

    __tablename__ = 'lend_logs'
    log_id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, db.ForeignKey('devices.device_id'))
    lender_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    doer_id = db.Column(db.String(60), nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey('schools.school_id'))
    lend_time = db.Column(db.DateTime, nullable=False)
    return_time = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return '<LendLogs %r>' % self.log_id

    def to_json(self):
        return {'id': self.log_id, 'device': self.device_id, 'lender': self.lender_id,
                'doer': self.doer_id, 'lend_time': self.lend_time, 'return_time': self.return_time}

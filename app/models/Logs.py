# coding=utf-8
__author__ = 'hypo'

from app import db


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

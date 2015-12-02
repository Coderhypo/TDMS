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

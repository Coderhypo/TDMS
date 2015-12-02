# coding=utf-8
__author__ = 'hypo'

from app import db


class Users(db.Model):
    """用户表"""

    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    user_login = db.Column(db.String(60), nullable=False, unique=True)
    user_name = db.Column(db.String(60), nullable=False)
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
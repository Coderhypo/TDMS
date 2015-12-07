# coding=utf-8
from app import db
from app.models import Users

__author__ = 'hypo'


class UserInfo:

    """
    用户信息类
    用来创建新用户信息记录
    getNewUser 获得新用户并持久化
    updateUser 更新用户信息
    deleteUser 删除用户
    """

    def __init__(self):
        pass

    __user_login = 'NONE'
    __user_name = 'NONE'
    __user_pass = 'NULL'
    __user_phone = 'NONE'
    __school_id = -1
    __user_rule = 'USER'

    def setLoginName(self, loginname):
        self.__user_login = loginname

    def setUsername(self, username):
        self.__user_name = username

    def setPass(self, password):
        self.__user_pass = password

    def setPhone(self, phone):
        self.__user_phone = phone

    def setSchool(self, schoolid):
        self.__school_id = schoolid

    def setRule(self, rule):

        if rule == 'ADMIN':
            self.__user_rule = rule
        else:
            self.__user_rule = 'USER'

    def getNewUser(self):

        user = Users()
        user.user_login = self.__user_login
        user.user_name = self.__user_name
        user.user_pass = self.__user_pass
        user.user_phone = self.__user_phone
        user.school_id = self.__school_id
        user.user_rule = self.__user_rule

        db.session.add(user)
        db.session.commit()

        return user

    def updateUser(self, id):

        user = Users.query.filter_by(user_id=id).first()

        user.user_login = self.__user_login
        user.user_name = self.__user_name
        user.user_pass = self.__user_pass
        user.user_phone = self.__user_phone
        user.school_id = self.__school_id
        user.user_rule = self.__user_rule

        db.session.add(user)
        db.session.commit()

    def deleteUser(self, id):

        user = Users.query.filter_by(user_id=id).first()

        db.session.delete(user)
        db.session.commit()

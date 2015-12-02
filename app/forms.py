# coding=utf-8
__author__ = 'hypo'

from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms import BooleanField, ValidationError, HiddenField
from wtforms import DateTimeField, SelectField, TextAreaField

from wtforms.validators import Required, Length, Email, Regexp, EqualTo


# 登陆表单
class LoginForm(Form):
    login = StringField(u'用户名', validators=[Required(), Length(1, 64)])
    password = PasswordField(u'密码', validators=[Required()])
    remberme = BooleanField(u'记住我', default=False)
    submit = SubmitField(u'登录')



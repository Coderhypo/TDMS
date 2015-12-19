# coding=utf-8
from app import app
from flask import render_template, request, redirect, url_for
from flask.ext.login import login_required, current_user

from app.models import Schools, Users

from .users import SchoolInfo, UserInfo

__author__ = 'hypo'


@app.route('/admin/users')
@login_required
def users():
    """用户管理界面"""

    list = []
    users = Users.query.all()

    for user in users:
        tmp = {'id': user.user_id, 'login': user.user_login, 'name': user.user_name, 'phone': user.user_phone}

        schoolid = user.school_id
        school = Schools.query.filter_by(school_id=schoolid).first()
        tmp['school'] = school.school_name

        list.append(tmp)

    slist = []
    schools = Schools.query.all()

    for school in schools:
        tmp = {'id': school.school_id, 'name': school.school_name}

        slist.append(tmp)

    return render_template('/admin/users/usermanage.html', list=list, schools=slist)


@app.route('/admin/adduser', methods=['GET', 'POST'])
@login_required
def addUser():
    if request.method == 'POST':
        doer = current_user
        user = UserInfo()
        user.setLoginName(request.form['login'])
        user.setUsername(request.form['name'])
        user.setPhone(request.form['phone'])
        user.setSchool(request.form['school'])

        user.getNewUser()

        return redirect(url_for('users'))

    list = []
    schools = Schools.query.all()

    for school in schools:
        tmp = {'id': school.school_id, 'name': school.school_name}

        list.append(tmp)

    return render_template('/admin/users/adduser.html', schools=list)


@app.route('/admin/updateuser', methods=['GET', 'POST'])
@login_required
def updateuser():
    """更新用户信息 管理员权限"""

    if request.method == 'POST':
        doer = current_user
        if 'update' == request.form['type']:
            id = request.form['editid']
            user = UserInfo()
            user.setLoginName(request.form['login'])
            user.setUsername(request.form['name'])
            user.setPhone(request.form['phone'])
            user.setSchool(request.form['school'])
            user.setRule(request.form['rule'])

            if request.form['pass'] is not None and len(request.form['pass']) > 0:
                user.setPass(request.form['pass'])

            user.updateUser(id)
        elif 'delete' == request.form['type']:
            id = request.form['delid']
            user = UserInfo()

            user.deleteUser(id)

    return redirect(url_for('users'))


@app.route('/admin/schools')
@login_required
def schools():
    """学院管理 管理员权限"""

    list = []
    schools = Schools.query.all()

    for school in schools:
        tmp = {'id': school.school_id, 'name': school.school_name}

        tmp['num'] = 0

        list.append(tmp)

    return render_template('/admin/users/schoolmanage.html', list=list)


@app.route('/admin/addschool', methods=['GET', 'POST'])
@login_required
def addSchool():
    """添加学院 管理员权限"""

    if request.method == 'POST':
        school = SchoolInfo()
        school.setSchoolName(request.form['name'])
        school.getNewSchool()

    return redirect(url_for('schools'))


@app.route('/admin/updateschool', methods=['GET', 'POST'])
@login_required
def updateschool():
    """更新学院信息 管理员权限"""

    if request.method == 'POST':
        if 'update' == request.form['type']:
            id = request.form['editid']
            school = SchoolInfo()
            school.setSchoolName(request.form['editname'])
            school.updateSchool(id)
        elif 'delete' == request.form['type']:
            id = request.form['delid']
            school = SchoolInfo()
            school.deleteSchool(id)

    return redirect(url_for('schools'))

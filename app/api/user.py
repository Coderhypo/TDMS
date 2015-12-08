# coding=utf-8
import json
from app import app
from app.models import Users
from flask import request

__author__ = 'hypo'


@app.route('/api/user', methods=['GET'])
def user():
    rnt = {}

    if request.method == 'GET':
        userid = request.args.get('uid', 0)
        userlogin = request.args.get('login', 0)
        username = request.args.get('name', 0)
        userrule = request.args.get('rule', 0)

        if userid != 0:
            user = Users.query.filter_by(user_id=userid).first()
            if user is not None:
                rnt = user.to_json()

        if userlogin != 0:
            user = Users.query.filter_by(user_login=userlogin).first()
            if user is not None:
                rnt = user.to_json()

        if username != 0:
            user = Users.query.filter_by(user_name=username).first()
            if user is not None:
                rnt = user.to_json()

        if userrule != 0:
            users = Users.query.filter_by(user_rule=userrule).all()
            rnt = []
            for user in users:
                tmp = user.to_json()
                rnt.append(tmp)

    return json.dumps(rnt)

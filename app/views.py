# coding=utf-8
__author__ = 'hypo'

from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/login')
def login():
    return render_template('base.html')


@app.route('/logout')
def logout():
    return render_template('base.html')


@app.route('/admin')
def admin():
    return render_template('/admin/index.html')


@app.route('/admin/lend')
def lend():

    return render_template('/admin/devices/lenddevice.html')


@app.route('/admin/return')
def reDevices():
    return render_template('/admin/devices/returndevice.html')


@app.route('/admin/devices')
def devices():
    return render_template('/admin/devices/devicemanage.html')


@app.route('/admin/users')
def users():
    return render_template('/admin/users/usermanage.html')


@app.route('/admin/lendlogs')
def lendLogs():
    return render_template('/admin/logs/lendlogs.html')


@app.route('/admin/schools')
def schools():
    return render_template('/admin/users/schoolmanage.html')


@app.route('/admin/logs')
def logs():
    return render_template('/admin/logs/logmanage.html')

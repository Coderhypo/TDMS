__author__ = 'hypo'

from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('base.html')
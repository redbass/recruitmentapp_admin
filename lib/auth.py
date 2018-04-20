from datetime import datetime, timedelta
from functools import wraps

import requests
from flask import render_template, request, jsonify, make_response, redirect, \
    url_for

from config import settings

API_URL_AUTH = '/token/auth'
COOKIE_MAX_AGE_delta = timedelta(minutes=60)


def login_get():
    return render_template("login.jinja2")


def login_post():
    username = request.form['username']
    password = request.form['password']

    response = request_jwt(username, password)

    if response.status_code is not 200:
        return jsonify({'error': 'wrong authentication'}), 402

    return create_login_response(response.json())


def create_login_response(jwt):
    resp = redirect(url_for('home'), code=302)
    resp.set_cookie('jwt', jwt.get('token'),
                    httponly=True, max_age=COOKIE_MAX_AGE_delta)
    resp.set_cookie('username', jwt.get('username'))
    return resp


def logout():
    resp = redirect(url_for('login_get'), code=302)
    resp.set_cookie('jwt', '', expires=0)
    return resp


def request_jwt(username, password):
    url = settings.API_URL_ROOT + API_URL_AUTH
    r = requests.post(url, json={'username': username, 'password': password})
    return r


def login_required(fn):

    @wraps(fn)
    def wrapper(*args, **kwargs):
        if 'jwt' in request.cookies:
            return fn(*args, **kwargs)

        return redirect(url_for('login_get'), code=302)

    return wrapper

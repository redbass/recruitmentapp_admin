import os
import requests
from flask import render_template, request, jsonify, make_response

from config import settings

API_URL_ROOT = os.environ.get('API_URL', 'http://localhost:5000')
API_URL_AUTH = '/token/auth'


def login_get():
    return render_template("login.jinja2")


def login_post():
    username = request.form['username']
    password = request.form['password']

    response = request_jwt(username, password)

    if response.status_code is not 200:
        return jsonify({'error': 'wrong authentication'}), 402

    return create_response(response.json())


def create_response(jwt):
    resp = make_response(jsonify({}))
    resp.set_cookie('jwt', jwt.get('token'), httponly=True)
    resp.set_cookie('username', jwt.get('username'))
    return resp


def request_jwt(username, password):
    url = settings.API_URL_ROOT + API_URL_AUTH
    r = requests.post(url, json={'username': username, 'password': password})
    return r

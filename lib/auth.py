from functools import wraps

import requests
from flask import render_template, request, session, redirect, url_for, \
    flash

from lib import template_list
from lib.errors import flash_exception
from lib.exceptions import AuthenticationError, APICallError
from lib.core_integration import request_access_jwt

SESSION_IS_LOGGED_IN = 'logged_in'
SESSION_USER = 'user'

ADMIN_ROLE = 'ADMIN'
HR_ROLE = 'HIRING_MANAGER'


def login_view():
    return render_template(template_list.LOGIN)


def login_post():
    log_out()
    username = request.form['username']
    password = request.form['password']

    try:
        respone = request_access_jwt(username, password)
        user = respone.json()

    except requests.exceptions.ConnectionError:
        raise APICallError()

    except AuthenticationError as e:
        flash_exception(e)
        return login_view()

    log_in(user)

    return redirect(url_for('home'), code=302)


def logout_view():
    log_out()
    flash('Logged out')
    return login_view()


def log_in(user):
    session[SESSION_IS_LOGGED_IN] = True
    session[SESSION_USER] = {
        "username": user.get('username'),
        "role": user.get('role'),
        "company_id": user.get('company_id')
    }
    print("log in:", session[SESSION_USER])


def get_logged_user():
    return session.get(SESSION_USER, {})


def log_out():
    session[SESSION_IS_LOGGED_IN] = False
    session[SESSION_USER] = {}


def is_logged_in(role=None):
    if role and session[SESSION_USER]['role'] != role:
        raise AuthenticationError()

    return session.get(SESSION_IS_LOGGED_IN, False)


def login_required(role=None):

    def decorator(fn):

        @wraps(fn)
        def wrapper(*args, **kwargs):
            if is_logged_in(role):
                return fn(*args, **kwargs)

            return redirect(url_for('login_view'), code=302)

        return wrapper

    return decorator

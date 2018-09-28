from functools import wraps

from flask import render_template, request, session, redirect, url_for, flash, \
    get_flashed_messages

from lib import template_list
from lib.exceptions import AuthenticationError
from lib.core_integration import request_access_jwt

SESSION_IS_LOGGED_IN = 'logged_in'
SESSION_USER = 'user'


def login_view():
    messages = get_flashed_messages()
    return render_template(template_list.LOGIN, messages=messages)


def login_post():
    log_out()
    username = request.form['username']
    password = request.form['password']

    try:
        respone = request_access_jwt(username, password)
        user = respone.json()
    except AuthenticationError as e:
        flash(str(e))
        return login_view()

    log_in(user.get('username'), user.get('role'))

    return redirect(url_for('home'), code=302)


def logout_view():
    log_out()
    flash('Logged out')
    return login_view()


def log_in(username, role):
    session[SESSION_IS_LOGGED_IN] = True
    session[SESSION_USER] = {
        "username": username,
        "role": role,
        "company_id": "0ccf647d7b1b474c825b55053386c417"
    }


def get_logged_user():
    return session.get(SESSION_USER, {})


def log_out():
    session[SESSION_IS_LOGGED_IN] = False


def is_logged_in():
    return session.get(SESSION_IS_LOGGED_IN, False)


def login_required(fn):

    @wraps(fn)
    def wrapper(*args, **kwargs):
        if is_logged_in():
            return fn(*args, **kwargs)

        return redirect(url_for('login_view'), code=302)

    return wrapper

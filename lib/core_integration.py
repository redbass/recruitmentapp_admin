from datetime import timedelta
from functools import wraps

import requests
from flask import session

from config import settings
from lib.exceptions import AuthenticationError, APICallError, \
    APIValidationError

API_URL_GET_ACCESS_TOKEN = '/token/auth'
API_URL_REFRESH_ACCESS_TOKEN = '/token/refresh'
COOKIE_MAX_AGE_delta = timedelta(minutes=60)
SESSION_ACCESS_TOKEN = 'jwt-access'
SESSION_REFRESH_TOKEN = 'jwt-refresh'


def request_access_jwt(username, password):
    url = settings.CORE_APP_URL + API_URL_GET_ACCESS_TOKEN
    request_json = {
        'username': username,
        'password': password
    }
    response = requests.post(url, json=request_json)

    if response.status_code is not 200:
        raise AuthenticationError("Invalid credentials")

    _set_session_login_data(response.json())

    return response


def refresh_access_token():
    url = settings.CORE_APP_URL + API_URL_REFRESH_ACCESS_TOKEN
    headers = _get_core_call_headers(is_refresh_token_call=True)
    response = requests.post(url, headers=headers)
    if response.status_code == 401:
        AuthenticationError("Failed to refresh the token")
    _set_session_login_data(response.json())


def _retry_if_token_expired(fn):

    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except AuthenticationError:
            refresh_access_token()
            return fn(*args, **kwargs)

    return wrapper


@_retry_if_token_expired
def get_json_from_core(path: str,
                       is_admin: bool = True):
    url = _get_api_url(is_admin, path)
    return _call_core_response(fn=requests.get, url=url, is_json=True)


@_retry_if_token_expired
def get_from_core(path: str,
                  is_admin: bool = True):
    url = _get_api_url(is_admin, path)
    return _call_core_response(fn=requests.get, url=url, is_json=False)


@_retry_if_token_expired
def post_json_to_core(path: str,
                      json: dict = None,
                      is_admin: bool = True):
    url = _get_api_url(is_admin, path)
    return _call_core_response(fn=requests.post, url=url, json=json)


@_retry_if_token_expired
def post_to_core(path: str,
                 is_admin: bool = True,
                 **kwargs):
    url = _get_api_url(is_admin, path)
    return _call_core_response(fn=requests.post, url=url, **kwargs)


def _get_api_url(is_admin, path):
    url = settings.CORE_APP_ADMIN_URL if is_admin else settings.CORE_APP_URL
    return url + path


def _call_core_response(fn, url, is_json=True, **kwargs):
    headers = _get_core_call_headers()

    try:
        response = fn(url, headers=headers, **kwargs)
        status_code = response.status_code
        body = response.json() if is_json else response.content

        if status_code == 200:
            return body

    except Exception as e:
        raise APICallError(str(e))

    msg = None

    if response.status_code == 401:
        raise AuthenticationError()

    elif isinstance(body, dict):
        if body.get('exception') == 'ValidationError':
            raise APIValidationError(core_response_body=body)

        msg = body.get('message')

    raise APICallError(msg or 'Unhandled error')


def _get_core_call_headers(is_refresh_token_call=False):
    access_token, refresh_token = _get_session_login_data()
    token = access_token if not is_refresh_token_call else refresh_token
    return {'Authorization': 'Bearer ' + token}


def _set_session_login_data(core_json_response):
    session[SESSION_ACCESS_TOKEN] = core_json_response['accessToken']
    refresh_token = core_json_response.get('refreshToken')
    if refresh_token:
        session[SESSION_REFRESH_TOKEN] = refresh_token


def _get_session_login_data():
    access_token = session.get(SESSION_ACCESS_TOKEN)
    refresh_token = session.get(SESSION_REFRESH_TOKEN)
    return access_token, refresh_token

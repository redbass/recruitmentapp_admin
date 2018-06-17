import requests
from flask import request

from config import settings


def make_core_api_call(path: str,
                       data: dict = None):
    jwt = request.cookies.get('jwt')
    url = settings.CORE_APP_URL + path
    headers = {'Authorization': 'Bearer ' + jwt}

    if data:
        return requests.post(url, headers=headers, json=data)

    return requests.get(url, headers=headers)

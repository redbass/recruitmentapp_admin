from json import dumps

import requests
from flask import render_template, request, redirect, url_for

from config import settings
from lib.auth import login_required


@login_required
def companies_view():

    response = make_core_api_call('/api/company')

    return render_template("companies.jinja2", companies=response.json())


@login_required
def create_company_view():
    return render_template("create_company.jinja2")


@login_required
def create_company_post():
    name = request.form.get('name')
    description = request.form.get('description')

    data = {
        'name': name,
        'description': description
    }

    make_core_api_call('/admin/api/company', data=data)

    return redirect(url_for('companies'))


def make_core_api_call(path,
                       data: dict = None):
    jwt = request.cookies.get('jwt')
    url = settings.CORE_APP_URL + path
    headers = {'Authorization': 'Bearer ' + jwt}

    if data:
        return requests.post(url, headers=headers, json=data)

    return requests.get(url, headers=headers)

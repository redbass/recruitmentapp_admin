from flask import render_template, request, redirect, url_for

from lib.auth import login_required
from lib.core_integration import make_admin_core_api_call


@login_required
def companies_view():

    response = make_admin_core_api_call('/api/company')

    return render_template("company/companies.jinja2",
                           companies=response.json())


@login_required
def create_company_view():
    return render_template("company/create_company.jinja2")


@login_required
def create_company_post():
    name = request.form.get('name')
    description = request.form.get('description')

    data = {
        'name': name,
        'description': description
    }

    make_admin_core_api_call('/api/company', data=data)

    return redirect(url_for('companies'))


@login_required
def edit_company_view(company_id):
    response = make_admin_core_api_call('/api/company/' + company_id)

    return render_template("company/edit_company.jinja2",
                           company=response.json())


@login_required
def edit_company_post(company_id):

    name = request.form.get('name')
    description = request.form.get('description')

    data = {
        'company_id': company_id,
        'name': name,
        'description': description
    }

    data = make_admin_core_api_call('/api/company/' + company_id, data=data)

    return redirect(url_for('companies'))

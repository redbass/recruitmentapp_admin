from flask import render_template, request, redirect, url_for

from lib.auth import login_required
from lib.core_integration import get_json_from_core, post_json_to_core


@login_required
def companies_view():
    companies = get_json_from_core('/api/company')
    return render_template("company/companies.jinja2", companies=companies)


@login_required
def edit_company_view(company_id):
    company = get_json_from_core('/api/company/' + company_id)

    return render_template("company/edit_company.jinja2",
                           company=company)


@login_required
def edit_company_post(company_id):

    name = request.form.get('name')
    description = request.form.get('description')

    data = {
        'company_id': company_id,
        'name': name,
        'description': description
    }

    post_json_to_core('/api/company/' + company_id, json=data)

    return redirect(url_for('companies'))

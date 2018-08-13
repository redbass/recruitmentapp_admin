from flask import request, render_template, redirect, url_for

from forms.company.form import CompanyForm
from lib.auth import login_required
from lib.core_integration import post_json_to_core, get_json_from_core
from lib.errors import flash_exception


@login_required
def create_company_view():
    form = CompanyForm(request.form)
    return render_template("company/create_company.jinja2", form=form)


@login_required
def create_company_post():
    form = CompanyForm(request.form)

    if form.validate_on_submit():

        try:
            data = form.create_company_core_from_form()
            post_json_to_core('/api/company', json=data)
            return redirect(url_for('companies'))

        except Exception as e:
            flash_exception(e)

    return render_template("company/create_company.jinja2", form=form)


@login_required
def edit_company_view(company_id):
    company = get_json_from_core('/api/company/' + company_id)

    form = CompanyForm(request.form)

    form.populate_form_from_core(company)

    return render_template("company/edit_company.jinja2", form=form,
                           company_id=company.get('_id'))


@login_required
def edit_company_post(company_id):

    form = CompanyForm(request.form)

    if form.validate_on_submit():

        try:
            data = form.create_company_core_from_form()
            post_json_to_core('/api/company/' + company_id, json=data)
            return redirect(url_for('companies'))

        except Exception as e:
            flash_exception(e)

    return render_template("company/edit_company.jinja2", form=form)

from flask import request, render_template, redirect, url_for

from lib import template_list
from routes.admin.company_form import CompanyForm
from lib.auth import login_required, ADMIN_ROLE
from lib.core_integration import post_json_to_core, get_json_from_core
from lib.errors import flash_exception, flash_error, flash_message
from routes.common.company import edit_company


@login_required(ADMIN_ROLE)
def create_company_view():
    form = CompanyForm(request.form)
    return render_template(template_list.ADMIN_CREATE_COMPANY, form=form)


@login_required(ADMIN_ROLE)
def create_company_post():
    form = CompanyForm(request.form)

    if form.validate_on_submit():

        try:
            data = form.create_company_core_from_form()
            post_json_to_core('/api/company', json=data)
            flash_message("Company created")
            return redirect(url_for('companies'))

        except Exception as e:
            flash_exception(e)

    return render_template(template_list.ADMIN_CREATE_COMPANY, form=form)


@login_required(ADMIN_ROLE)
def edit_company_view(company_id, form=None):
    company = get_json_from_core('/api/company/' + company_id)

    form = form if form else CompanyForm(request.form)

    form.populate_form_from_core(company)

    return render_template(template_list.COMMON_EDIT_COMPANY,
                           form=form,
                           company_id=company.get('_id'),
                           form_action='edit_company_post')


@login_required(ADMIN_ROLE)
def edit_company_post(company_id):
    form = CompanyForm(request.form)

    edited = edit_company(form, company_id)

    if edited:
        flash_message("Company updated")
        return redirect(url_for('companies'))

    flash_error("Company not saved")
    return edit_company_view(form)


@login_required(ADMIN_ROLE)
def companies_view():
    companies = get_json_from_core('/api/company')
    return render_template(template_list.ADMIN_COMPANY_LIST,
                           companies=companies)


@login_required(ADMIN_ROLE)
def enable_company_post(company_id, action):
    post_json_to_core('/api/company/{company_id}/{action}'
                      .format(company_id=company_id, action=action))
    return redirect(url_for('companies'))

from flask import request, render_template

from lib import template_list
from lib.auth import login_required, HR_ROLE, get_logged_user
from lib.core_integration import get_json_from_core
from routes.common.company import edit_company
from routes.hiring_manager.company_form import HMCompanyForm


@login_required(HR_ROLE)
def company_info():
    company_id = get_user_company_id()

    company = get_json_from_core('/api/company/' + company_id)

    form = HMCompanyForm(request.form)

    form.populate_form_from_core(company)

    return render_template(template_list.HM_EDIT_COMPANY, form=form,
                           company_id=company_id)


@login_required(HR_ROLE)
def company_info_post():
    company_form_class = HMCompanyForm
    success_end_point = 'hr_company_info'
    failure_template_name = template_list.HM_EDIT_COMPANY

    company_id = get_user_company_id()

    return edit_company(company_form_class, company_id, failure_template_name,
                        success_end_point)


def get_user_company_id():
    user = get_logged_user()
    return user['company_id']

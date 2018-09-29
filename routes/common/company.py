from flask import request, redirect, url_for, render_template

from lib.core_integration import post_json_to_core
from lib.errors import flash_exception


def edit_company(company_form_class, company_id, failure_template_name,
                 success_end_point):
    form = company_form_class(request.form)
    if form.validate_on_submit():

        try:
            data = form.create_company_core_from_form()
            post_json_to_core('/api/company/' + company_id, json=data)
            return redirect(url_for(success_end_point))

        except Exception as e:
            flash_exception(e)
    return render_template(failure_template_name, form=form)

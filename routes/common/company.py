from lib.core_integration import post_json_to_core
from lib.errors import flash_exception


def edit_company(form, company_id):

    if form.validate_on_submit():

        try:
            data = form.create_company_core_from_form()
            post_json_to_core('/api/company/' + company_id, json=data)
            return True

        except Exception as e:
            flash_exception(e)

    return False

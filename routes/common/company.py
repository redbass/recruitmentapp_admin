from io import BytesIO

from flask import request, jsonify, send_file

from config import APP_SRC
from lib.auth import login_required
from lib.core_integration import post_json_to_core, get_from_core, post_to_core
from lib.errors import flash_exception
from lib.exceptions import APICallError


def edit_company(form, company_id):

    if form.validate_on_submit():

        try:
            data = form.create_company_core_from_form()
            post_json_to_core('/api/company/' + company_id, json=data)
            return True

        except Exception as e:
            flash_exception(e)

    return False


@login_required()
def get_company_logo(company_id):
    try:
        url = '/api/company/{company_id}/logo'.format(company_id=company_id)
        image = get_from_core(is_admin=False, path=url)
        return send_file(
                BytesIO(image),
                mimetype='image/*'
            )
    except APICallError:
        return send_file(
            "{src}/img/empty.png".format(src=APP_SRC),
            mimetype='image/png'
        )


@login_required()
def post_company_logo(company_id):

    files = request.files

    try:
        post_to_core(
            is_admin=False,
            path='/api/company/{company_id}/logo'.format(
                company_id=company_id),
            files=files
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 400

    return jsonify(None)

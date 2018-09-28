from flask import jsonify

from lib.auth import login_required
from lib.core_integration import get_json_from_core


@login_required('ADMIN')
def get_postcode(postcode):

    url = '/api/postcode/' + postcode
    postcode = get_json_from_core(url, is_admin=False)

    return jsonify(postcode)

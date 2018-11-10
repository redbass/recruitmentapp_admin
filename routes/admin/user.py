from flask import render_template

from lib import template_list
from lib.auth import login_required, ADMIN_ROLE
from lib.core_integration import get_json_from_core


@login_required(ADMIN_ROLE)
def users_view():

    users = get_json_from_core('/api/user')

    return render_template(template_list.ADMIN_USERS, users=users)

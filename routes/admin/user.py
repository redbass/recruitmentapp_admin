from flask import render_template

from lib import template_list
from lib.auth import login_required, ADMIN_ROLE


@login_required(ADMIN_ROLE)
def users_view():

    return render_template(template_list.ADMIN_USERS)

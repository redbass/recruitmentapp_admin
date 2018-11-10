from flask import render_template

from lib import template_list
from lib.auth import login_required, ADMIN_ROLE
from lib.core_integration import get_json_from_core
from routes.admin.user_form import UserForm


@login_required(ADMIN_ROLE)
def users_view():

    users = get_json_from_core('/api/user')

    return render_template(template_list.ADMIN_USERS, users=users)


@login_required(ADMIN_ROLE)
def user_view(user_id):

    user = get_json_from_core('/api/user/' + user_id)
    form = UserForm()
    form.populate_form_from_core(user=user)

    return render_template(template_list.ADMIN_USER, form=form)

from flask import render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField, PasswordField

from lib import template_list
from lib.enums import TITLES
from lib.auth import login_required
from lib.core_integration import post_json_to_core
from lib.errors import flash_exception


class SignCompanyForm(FlaskForm):
    hm_username = StringField(
        'Email',
        validators=[validators.Length(min=1, max=25),
                    validators.DataRequired()])

    hm_password = PasswordField(
        'Password',
        validators=[validators.Length(min=6, max=12),
                    validators.DataRequired()])

    hm_confirm_password = PasswordField(
        'Password',
        validators=[validators.Length(min=6, max=12),
                    validators.DataRequired()])

    hm_title = SelectField('Title', choices=TITLES)

    hm_first_name = StringField(
        'First name',
        validators=[validators.Length(min=1, max=25),
                    validators.DataRequired()])

    hm_last_name = StringField(
        'Last Name',
        validators=[validators.Length(min=1, max=25),
                    validators.DataRequired()])

    company_name = StringField(
        'Company Name',
        validators=[validators.Length(min=1, max=25),
                    validators.DataRequired()])

    company_description = StringField(
        'Company Description',
        validators=[validators.Length(min=1, max=500),
                    validators.DataRequired()])

    def create_sign_in_company_core_from_form(self):
        return {
            "hm_email": self.data.get('hm_username'),
            "hm_password": self.data.get('hm_password'),
            "hm_first_name": self.data.get('hm_first_name'),
            "hm_last_name": self.data.get('hm_last_name'),
            "hm_title": self.data.get('hm_title'),
            "company_name": self.data.get('company_name'),
            "company_description": self.data.get('company_description'),
        }


@login_required('ADMIN')
def sign_in_company():
    form = SignCompanyForm(request.form)
    return render_template(template_list.SIGN_IN_COMPANY, form=form)


@login_required('ADMIN')
def sign_in_company_post():
    form = SignCompanyForm(request.form)

    if form.validate_on_submit():

        try:
            _validate_password(form)
            data = form.create_sign_in_company_core_from_form()
            post_json_to_core('/api/company', is_admin=False, json=data)
            return redirect(url_for('home'))

        except Exception as e:
            flash_exception(e)

    return render_template(template_list.SIGN_IN_COMPANY, form=form)


def _validate_password(form):
    if form.hm_password.data != form.hm_confirm_password.data:
        raise ValueError('The password does not match')

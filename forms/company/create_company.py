from flask import request, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, validators as Validators, \
    SelectField

from forms import TRADES_VALUES
from forms.widgets import LongStringField
from lib.auth import login_required
from lib.core_integration import post_json_to_core, APICallError
from lib.exceptions import AuthenticationError


class CreateCompanyForm(FlaskForm):
    validators = [Validators.Length(min=1, max=25),
                  Validators.DataRequired()]

    company_name = StringField(
        'Company Name',
        validators=[Validators.Length(min=1, max=25),
                    Validators.DataRequired()])

    company_description = LongStringField(
        'Company Description',
        validators=[Validators.Length(min=1, max=2000),
                    Validators.DataRequired()])

    trades = SelectField('Trades',
                         choices=TRADES_VALUES)

    # company_logo = FileInput(lable='Company Logo')

    address_number = StringField(
        'House or flat name or number',
        validators=[Validators.Length(min=1, max=100),
                    Validators.DataRequired()])

    address_street = StringField(
        'Company Name',
        validators=[Validators.Length(min=1, max=100),
                    Validators.DataRequired()])

    address_town = StringField(
        'Street',
        validators=[Validators.Length(min=1, max=100)])

    address_city = StringField(
        'City',
        validators=[Validators.Length(min=1, max=100)])

    address_postcode = StringField(
        'Postcode',
        validators=[Validators.Length(min=1, max=100)])

    company_vat = StringField(
        'Company Vat Number',
        validators=[Validators.Length(min=1, max=100)])


@login_required
def create_company_view():
    form = CreateCompanyForm(request.form)
    return render_template("company/create_company.jinja2", form=form)


@login_required
def create_company_post():
    form = CreateCompanyForm(request.form)

    if form.validate_on_submit():

        try:
            create_company_core(form)
        except [APICallError, AuthenticationError] as e:
            flash(str(e))
            return render_template("company/create_company.jinja2", form=form)

    return redirect(url_for('companies'))


def create_company_core(form):
    data = {
        'name': form.data.get('company_name'),
        'description': form.data.get('company_description')
    }

    post_json_to_core('/api/company', json=data)

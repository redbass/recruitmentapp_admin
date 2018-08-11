from flask_wtf import FlaskForm
from wtforms import validators as Validators, StringField, SelectMultipleField

from forms import TRADES_VALUES
from forms.widgets import LongStringField


class CompanyForm(FlaskForm):
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

    trades = SelectMultipleField('Trades', choices=TRADES_VALUES)

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

    def populate_form_from_core(self, company):
        self.company_name.data = company.get('name', '')
        self.company_description.data = company.get('description', '')

    def create_company_core_from_form(self):
        return {
            'name': self.data.get('company_name'),
            'description': self.data.get('company_description')
        }

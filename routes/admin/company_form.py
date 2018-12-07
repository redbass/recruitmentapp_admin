from flask_wtf import FlaskForm
from wtforms import validators, StringField

from lib.widgets import LongStringField, SelectMultipleFieldAsync
from lib.picklist import get_picklist_values


class CompanyForm(FlaskForm):

    name = StringField(
        'Company Name',
        validators=[validators.Length(min=1, max=25),
                    validators.DataRequired()])

    description = LongStringField(
        'Company Description',
        validators=[validators.Length(min=1, max=500),
                    validators.DataRequired()])

    trades = SelectMultipleFieldAsync(
        'Trades',
        choices_fn=lambda: get_picklist_values('company_trades'))

    vat = StringField(
        'Company Vat Number',
        validators=[validators.Length(min=1, max=100)])

    address_number = StringField(
        'House or flat name or number',
        validators=[validators.Length(min=1, max=25),
                    validators.DataRequired()])

    address_street = StringField(
        'Street',
        validators=[validators.Length(min=1, max=50),
                    validators.DataRequired()])

    address_town = StringField(
        'Town',
        validators=[validators.Length(min=1, max=25)])

    address_city = StringField(
        'City',
        validators=[validators.Length(min=1, max=50)])

    address_postcode = StringField(
        'Postcode',
        validators=[validators.Length(min=1, max=10)])

    email = StringField(
        'Email',
        validators=[validators.Length(min=1, max=25),
                    validators.DataRequired()])

    phone_number = StringField(
        'Phone number',
        validators=[validators.Length(min=1, max=25),
                    validators.DataRequired()])

    # company_logo = FileInput(lable='Company Logo')

    def populate_form_from_core(self, company):

        self.name.data = company.get('name', '')
        self.description.data = company.get('description', '')
        self.vat.data = company.get('vat', '')

        metadata = company.get('metadata', {})
        self.trades.data = metadata.get('trades', [])

        contacts = company.get('contacts', {})
        self.email.data = contacts.get('email')
        self.phone_number.data = contacts.get('phone_number', '')

        address = contacts.get('address', {})
        self.address_number.data = address.get('number', '')
        self.address_street.data = address.get('street', '')
        self.address_city.data = address.get('city', '')
        self.address_town.data = address.get('town', '')
        self.address_postcode.data = address.get('postcode', '')

    def create_company_core_from_form(self):
        return {
            "name": self.data.get('name'),
            "description": self.data.get('description'),
            "vat": self.data.get('vat'),
            "contacts": {
                "address": {
                    "number": self.data.get('address_number'),
                    "street": self.data.get('address_street'),
                    "city": self.data.get('address_city'),
                    "town": self.data.get('address_town'),
                    "postcode": self.data.get('address_postcode'),
                },
                "email": self.data.get('email'),
                "phone_number": self.data.get('phone_number'),
            },
            "metadata": {
                "trades": self.data.get('trades'),
            }
        }

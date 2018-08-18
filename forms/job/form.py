from flask_wtf import FlaskForm
from wtforms import StringField, validators

from forms.widgets import SelectFieldAsync, LongStringField
from lib.core_integration import get_json_from_core


def company_choices_fn():
    companies = get_json_from_core('/api/company')

    choices = [('', 'Please select a company...')]
    for company in companies:
        choices.append((company.get('_id'), company.get('name')))

    return choices



class JobForm(FlaskForm):

    company_name = SelectFieldAsync(
        'Company Name',
        choices_fn=company_choices_fn
    )

    name = StringField(
        'Company Name',
        validators=[validators.Length(min=1, max=25),
                    validators.DataRequired()])

    description = LongStringField(
        'Company Description',
        validators=[validators.Length(min=1, max=2000),
                    validators.DataRequired()])

    def populate_form_from_core(self, company):
        pass

    def create_company_core_from_form(self):
        return {}

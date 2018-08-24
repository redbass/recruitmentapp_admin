from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField, DecimalField, HiddenField
from wtforms.widgets import HiddenInput

from forms import DURATIONS
from forms.widgets import SelectFieldAsync, LongStringField
from lib.core_integration import get_json_from_core


def company_choices_fn():
    companies = get_json_from_core('/api/company')

    choices = [('', 'Please select a company...')]
    for company in companies:
        choices.append((company.get('_id'), company.get('name')))

    return choices


class JobForm(FlaskForm):

    company_id = SelectFieldAsync(
        'Company Name',
        choices_fn=company_choices_fn
    )

    title = StringField(
        'Job Title',
        validators=[validators.Length(min=1, max=25),
                    validators.DataRequired()])

    description = LongStringField(
        'Job Description',
        validators=[validators.Length(min=1, max=2000),
                    validators.DataRequired()])

    postcode = StringField(
        'Postcode',
        validators=[validators.DataRequired()])

    latitude = DecimalField(
        'Latitude',
        validators=[validators.DataRequired()],
        widget=HiddenInput())
    longitude = DecimalField(
        'Longitude',
        validators=[validators.DataRequired()],
        widget=HiddenInput())

    duration = SelectField(
        'Duration',
        choices=DURATIONS,
        coerce=lambda c: int(c) if c else None,
        validators=[validators.DataRequired()]
    )

    def populate_form_from_core(self, company):
        pass

    def create_job_core_from_form(self):
        job = {
            "company_id": self.data.get('company_id'),
            "title": self.data.get('title'),
            "description": self.data.get('description'),
            "location": {
                "lat": float(self.data.get('latitude')),
                "lng": float(self.data.get('longitude'))
            }
        }

        advert = {
            'duration': self.data.get('duration')
        }

        return job, advert

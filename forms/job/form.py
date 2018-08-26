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


class JobBaseForm(FlaskForm):

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

    def populate_form_from_core(self, company):
        self.company_id.data = company.get('company_id', '')
        self.title.data = company.get('title', '')
        self.description.data = company.get('description', '')

        location = company.get('location', {})
        self.postcode.data = location.get('postcode', '')

        coordinates = location.get('geo_location', {}).get('coordinates', [])
        self.latitude.data = coordinates[1]
        self.longitude.data = coordinates[0]

    def create_job_core_from_form(self):
        job = {
            "title": self.data.get('title'),
            "description": self.data.get('description'),
            "location": {
                "postcode": self.data.get('postcode'),
                "latitude": float(self.data.get('latitude')),
                "longitude": float(self.data.get('longitude'))
            }
        }

        job_not_implemented_fields = {
            "duration_days": 28,
            "metadata": {
                "trades": ["software_engineer"],
                "job_type": "developer"
            },
            "rate": {
                "type": "other",
                "units": "lines of code",
                "value": 0.1
            }
        }

        job.update(job_not_implemented_fields)

        return job


class JobCreateForm(JobBaseForm):

    company_id = SelectFieldAsync(
        'Company Name',
        choices_fn=company_choices_fn,
        validators=[validators.DataRequired()]
    )

    duration = SelectField(
        'Duration',
        choices=DURATIONS,
        coerce=lambda c: int(c) if c else None,
        validators=[validators.DataRequired()]
    )

    def populate_form_from_core(self, company):
        super().populate_form_from_core(company)

        adverts = company.get('adverts', [])
        if adverts:
            self.duration.data = adverts[0].get('duration', '')

    def create_job_core_from_form(self):
        job = super().create_job_core_from_form()

        job['company_id'] = self.data.get('company_id')

        advert = {
            'duration': self.data.get('duration')
        }

        return job, advert


class JobEditForm(JobBaseForm):

    pass

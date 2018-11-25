from flask_wtf import FlaskForm
from wtforms import StringField, validators, DecimalField
from wtforms.widgets import HiddenInput

from lib.core_integration import get_json_from_core
from lib.widgets import SelectFieldAsync, LongStringField
from routes.admin.settings import get_picklist_values


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
    admin_district = StringField(
        'Admin District',
        validators=[validators.DataRequired()],
        widget=HiddenInput())

    job_type = SelectFieldAsync(
        'Job title',
        choices_fn=lambda: get_picklist_values('job_titles'),
        validators=[validators.DataRequired()]
    )

    rate_type = SelectFieldAsync(
        'Rate type',
        choices_fn=lambda: get_picklist_values('job_rates'),
        validators=[validators.DataRequired()]
    )

    rate_value = DecimalField(
        'Rate value in £',
        places=2,
        default=0.00,
        validators=[validators.DataRequired()])

    def populate_form_from_core(self, job):
        self.title.data = job.get('title', '')
        self.description.data = job.get('description', '')

        location = job.get('location', {})
        self.postcode.data = location.get('postcode', '')

        coordinates = location.get('geo_location', {}).get('coordinates', [])
        self.latitude.data = coordinates[1]
        self.longitude.data = coordinates[0]
        self.admin_district.data = location.get('admin_district')

        rate = job.get('rate')
        self.rate_type.data = rate.get('type')
        self.rate_value.data = rate.get('value')

        metadata = job.get('metadata')
        self.job_type.data = metadata.get('job_type')

    def create_job_core_from_form(self):
        job = {
            "title": self.data.get('title'),
            "description": self.data.get('description'),
            "location": {
                "postcode": self.data.get('postcode'),
                "admin_district": self.data.get('admin_district'),
                "latitude": float(self.data.get('latitude')),
                "longitude": float(self.data.get('longitude'))
            },
            "duration_days": self.data.get('duration'),
            "rate": {
                "type": self.data.get('rate_type'),
                "value": float(self.data.get('rate_value'))
            },
            "metadata": {
                "job_type": self.data.get('job_type')
            }
        }

        job["metadata"]["trades"] = [""]

        return job


class JobCreateForm(JobBaseForm):

    company_id = SelectFieldAsync(
        'Company Name',
        choices_fn=company_choices_fn,
        validators=[validators.DataRequired()]
    )

    duration = SelectFieldAsync(
        'Duration',
        choices_fn=lambda: get_picklist_values('job_durations'),
        validators=[validators.DataRequired()]
    )

    def populate_form_from_core(self, company):
        super().populate_form_from_core(company)

        self.company_id.data = company.get('company_id', '')

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

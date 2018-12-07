from flask_wtf import FlaskForm
from wtforms import StringField, validators, DecimalField, IntegerField
from wtforms.widgets import HiddenInput

from lib.core_integration import get_json_from_core
from lib.widgets import SelectFieldAsync, LongStringField
from lib.picklist import get_picklist_values


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
        choices_fn=lambda: get_picklist_values(
            'job_titles',
            none_value="Please select job title"),
        validators=[validators.DataRequired()]
    )

    job_duration_weeks = IntegerField(
        'Job length (weeks)',
        validators=[validators.DataRequired()]
    )

    rate_type = SelectFieldAsync(
        'Rate type',
        choices_fn=lambda: get_picklist_values(
            'job_rates',
            none_value="Please select a job type"),
        validators=[validators.DataRequired()]
    )

    rate_value = DecimalField(
        'Rate value in £',
        places=2,
        validators=[validators.DataRequired()],
        render_kw={'placeholder': 0.00})

    def populate_form_from_core(self, job):
        self.title.data = job.get('title', '')
        self.description.data = job.get('description', '')

        location = job.get('location', {})
        self.postcode.data = location.get('postcode', '')

        coordinates = location.get('geo_location', {}).get('coordinates', [])
        self.latitude.data = coordinates[1]
        self.longitude.data = coordinates[0]
        self.admin_district.data = location.get('admin_district',
                                                "Not provided")

        rate = job.get('rate')
        self.rate_type.data = rate.get('type')
        self.rate_value.data = rate.get('value')

        metadata = job.get('metadata')
        self.job_type.data = metadata.get('job_type')
        self.job_duration_weeks.data = metadata.get('job_duration_days')

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
            "rate": {
                "type": self.data.get('rate_type'),
                "value": float(self.data.get('rate_value'))
            },
            "metadata": {
                "job_type": self.data.get('job_type'),
                "job_duration_days": int(self.data.get('job_duration_weeks'))
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
        'Publication Length',
        choices_fn=lambda: get_picklist_values(
            'job_durations',
            none_value="Please select the advert publication length"),
        validators=[validators.DataRequired()]
    )

    def populate_form_from_core(self, job):
        super().populate_form_from_core(job)

        self.company_id.data = job.get('company_id', '')

        adverts = job.get('adverts', [])
        if adverts:
            self.duration.data = adverts[0].get('duration', '')

    def create_job_core_from_form(self):
        job = super().create_job_core_from_form()

        job['company_id'] = self.data.get('company_id')

        advert = {
            'duration': int(self.data.get('duration'))
        }

        return job, advert


class JobEditForm(JobBaseForm):

    pass

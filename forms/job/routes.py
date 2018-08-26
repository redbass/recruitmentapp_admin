from flask import render_template, request, redirect, url_for

from forms.job.form import JobCreateForm, JobEditForm
from lib.auth import login_required
from lib.core_integration import post_json_to_core, get_json_from_core
from lib.errors import flash_exception


@login_required
def create_job(form=None):
    form = form or JobCreateForm(request.form)

    return render_template("job/create_job.jinja2", form=form)


@login_required
def create_job_post():
    form = JobCreateForm(request.form)

    if form.validate_on_submit():

        try:
            job, advert = form.create_job_core_from_form()
            new_job = post_json_to_core('/api/job', json=job)

            job_id = new_job['_id']
            post_json_to_core('/api/job/{job_id}/advert'
                              .format(job_id=job_id), json=advert)

            return redirect(url_for('edit_job', job_id=job_id))

        except Exception as e:
            flash_exception(e)

    return create_job(form=form)


@login_required
def edit_job_view(job_id, form=None):
    job = get_json_from_core('/api/job/' + job_id)
    adverts = job.get('adverts', [None])

    form = JobCreateForm(form or request.form)

    form.populate_form_from_core(job)

    return render_template("job/edit_job.jinja2",
                           job_id=job_id, advert=adverts[0], form=form)


@login_required
def edit_job_post(job_id):

    form = JobEditForm(request.form)

    if form.validate_on_submit():

        try:
            job = form.create_job_core_from_form()
            post_json_to_core('/api/job/' + job_id, json=job)

            return redirect(url_for('jobs'))

        except Exception as e:
            flash_exception(e)

    return edit_job_view(job_id, form)

from flask import render_template, request, redirect, url_for

from routes.admin.job.form import JobCreateForm, JobEditForm
from lib.auth import login_required, ADMIN_ROLE
from lib.core_integration import post_json_to_core, get_json_from_core
from lib.errors import flash_exception
from lib import template_list


@login_required(ADMIN_ROLE)
def create_job(form=None):
    form = form or JobCreateForm(request.form)

    return render_template(template_list.CREATE_JOB, form=form,
                           form_type='create_admin')


@login_required(ADMIN_ROLE)
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


@login_required(ADMIN_ROLE)
def edit_job_view(job_id, form=None):
    job = get_json_from_core('/api/job/' + job_id)
    adverts = job.get('adverts', [None])

    form = JobCreateForm(form or request.form)

    form.populate_form_from_core(job)

    return render_template(template_list.EDIT_JOB,
                           job_id=job_id, advert=adverts[0], form=form,
                           form_type='admin_edit')


@login_required(ADMIN_ROLE)
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


@login_required(ADMIN_ROLE)
def set_advert_status(job_id: str, advert_id: str, action: str):
    data = {'duration': request.form.get('duration')}
    publish_url = '/api/job/{job_id}/advert/{advert_id}/{action}'\
        .format(job_id=job_id, advert_id=advert_id, action=action)

    post_json_to_core(publish_url, json=data)

    return redirect(url_for('edit_job', job_id=job_id))


@login_required(ADMIN_ROLE)
def jobs_view():
    jobs = get_json_from_core('/api/job')

    return render_template(template_list.JOB_LIST, jobs=jobs)

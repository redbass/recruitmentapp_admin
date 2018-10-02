from flask import render_template, request, redirect, url_for

from routes.admin.job_form import JobCreateForm, JobEditForm
from lib.auth import login_required, ADMIN_ROLE
from lib.core_integration import get_json_from_core
from lib import template_list
from routes.common import job as common


@login_required(ADMIN_ROLE)
def create_job_view(form=None):
    form = form or JobCreateForm(request.form)

    return render_template(template_list.COMMON_CREATE_JOB,
                           form=form,
                           form_type='create_admin',
                           form_action='create_job_post')


@login_required(ADMIN_ROLE)
def create_job_post():
    form = JobCreateForm(request.form)

    job_id = common.create_job(form)

    if job_id:
        return redirect(url_for('edit_job', job_id=job_id))

    return create_job_view(form)


@login_required(ADMIN_ROLE)
def edit_job_view(job_id, form=None):
    job = get_json_from_core('/api/job/' + job_id)
    adverts = job.get('adverts', [None])

    form = JobEditForm(form or request.form)

    form.populate_form_from_core(job)

    return render_template(template_list.ADMIN_EDIT_JOB,
                           job_id=job_id, advert=adverts[0], form=form,
                           form_type='admin_edit')


@login_required(ADMIN_ROLE)
def edit_job_post(job_id):
    form = JobEditForm(request.form)
    edited = common.edit_job(form, job_id)

    return redirect(url_for('jobs')) if edited else \
        edit_job_view(job_id, form)


@login_required(ADMIN_ROLE)
def jobs_view():
    jobs = get_json_from_core('/api/job')

    return render_template(template_list.ADMIN_JOB_LIST, jobs=jobs)

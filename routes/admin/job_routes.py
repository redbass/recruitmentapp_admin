from flask import render_template, request, redirect, url_for

from lib.errors import flash_error, flash_message
from routes.admin.job_form import JobCreateForm, JobEditForm
from lib.auth import login_required, ADMIN_ROLE
from lib.core_integration import get_json_from_core
from lib import template_list
from routes.common import job as common
from routes.common.job import AdvertStatus


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

    job_id = common.create_job(form, approve=True)

    if job_id:
        flash_message("Job created")
        return redirect(url_for('edit_job', job_id=job_id))

    return create_job_view(form)


@login_required(ADMIN_ROLE)
def edit_job_view(job_id, form=None):
    job = get_json_from_core('/api/job/' + job_id)
    applications = get_json_from_core('/api/job/' + job_id + '/applications')
    adverts = job.get('adverts', [None])

    form = form if form else JobEditForm(request.form)

    form.populate_form_from_core(job)

    candidates = applications['candidates'] if applications else []
    return render_template(template_list.ADMIN_EDIT_JOB,
                           job_id=job_id,
                           advert=adverts[0],
                           form=form,
                           form_type='admin_edit',
                           form_action='edit_job_post',
                           candidates=candidates)


@login_required(ADMIN_ROLE)
def edit_job_post(job_id):
    form = JobEditForm(request.form)
    edited = common.edit_job(form, job_id)

    if edited:
        flash_message("Job updated")
        return redirect(url_for('jobs'))

    flash_error("Job not saved")
    return edit_job_view(job_id, form)


@login_required(ADMIN_ROLE)
def jobs_view():
    url = '/api/job?excludeDrafts=True'
    if request.args.get('filter') == 'approval':
        url += "&advertsStatusFilter={advert_status}"\
            .format(advert_status=AdvertStatus.REQUEST_APPROVAL)

    jobs = get_json_from_core(url)
    return render_template(template_list.ADMIN_JOB_LIST,
                           jobs=jobs,
                           archive_endpoint='set_advert_status',
                           edit_job_endpoint='edit_job')

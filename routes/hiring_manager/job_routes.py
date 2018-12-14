from flask import request, render_template, redirect, url_for

from lib import template_list
from lib.auth import login_required, HR_ROLE, get_logged_user
from lib.core_integration import get_json_from_core
from lib.errors import flash_error
from routes.common.advert import request_set_advert_status
from routes.common.job import edit_job, create_job
from routes.hiring_manager.job_form import HMJobCreateForm, HMJobEditForm


@login_required(HR_ROLE)
def edit_company_job_view(job_id, form=None):
    job = get_json_from_core('/api/job/' + job_id)
    adverts = job.get('adverts', [None])

    form = HMJobEditForm()

    form.populate_form_from_core(job)

    advert = adverts[0]
    form_type = 'hm_edit'
    disable_hm_editing = advert['status'] != 'DRAFT' and form_type == 'hm_edit'

    return render_template(template_list.COMMON_EDIT_JOB,
                           job_id=job_id,
                           advert=advert,
                           form=form,
                           form_type=form_type,
                           form_action='hr_edit_company_job_post',
                           disable_hm_editing=disable_hm_editing)


@login_required(HR_ROLE)
def edit_company_job_view_post(job_id):
    form = HMJobEditForm(request.form)
    edited = edit_job(form, job_id)

    return redirect(url_for('hr_company_jobs')) if edited else \
        edit_company_job_view(job_id, form)


@login_required(HR_ROLE)
def company_jobs():
    jobs = get_json_from_core('/api/hm/company/job', is_admin=False)

    return render_template(template_list.HM_JOB_LIST,
                           jobs=jobs,
                           edit_job_endpoint='hr_edit_company_job',
                           archive_endpoint='hr_set_advert_status')


@login_required(HR_ROLE)
def create_company_job(form=None):
    user = get_logged_user()

    form = form or HMJobCreateForm(request.form)
    form.company_id = user['company_id']

    return render_template(template_list.COMMON_CREATE_JOB,
                           form=form,
                           form_type='create_hr',
                           form_action='hr_create_company_job_post')


@login_required(HR_ROLE)
def create_company_job_post():
    user = get_logged_user()
    form = HMJobCreateForm(request.form)
    form.company_id.data = user['company_id']

    job_id = create_job(form)

    if job_id:
        return redirect(url_for('hr_edit_company_job', job_id=job_id))

    return create_company_job(form)


@login_required(HR_ROLE)
def archive_advert_post(job_id, advert_id, action):

    if action in ['archive', 'requestApproval']:
        request_set_advert_status(action, advert_id, job_id)
    else:
        flash_error('Action not allowed')

    return redirect(url_for('hr_company_jobs', job_id=job_id))

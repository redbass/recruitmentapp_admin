from flask import request, render_template

from lib import template_list
from lib.auth import login_required, HR_ROLE, get_logged_user
from lib.core_integration import get_json_from_core
from routes.hiring_manager.job_form import HMJobCreateForm


@login_required(HR_ROLE)
def edit_job_view(job_id, form=None):
    # job = get_json_from_core('/api/job/' + job_id)
    # adverts = job.get('adverts', [None])
    #
    # form = HRJobCreateForm(form or request.form)
    #
    # form.populate_form_from_core(job)
    #
    # return render_template(template_list.EDIT_JOB,
    #                        job_id=job_id, advert=adverts[0], form=form,
    #                        form_type='ht_edit')
    pass


@login_required(HR_ROLE)
def company_jobs():
    jobs = get_json_from_core('/api/hm/company/job', is_admin=False)

    return render_template(template_list.JOB_LIST, jobs=jobs)


@login_required(HR_ROLE)
def create_company_job():
    user = get_logged_user()

    form = HMJobCreateForm(request.form)
    form.company_id = user['company_id']

    return render_template(template_list.CREATE_JOB, form=form,
                           form_type='create_hr')

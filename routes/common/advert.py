from flask import request, redirect, url_for

from lib.auth import login_required, get_logged_user, ADMIN_ROLE
from lib.core_integration import post_json_to_core


@login_required(ADMIN_ROLE)
def set_advert_status(job_id: str, advert_id: str, action: str):
    data = {'duration': request.form.get('duration')}
    publish_url = '/api/job/{job_id}/advert/{advert_id}/{action}'\
        .format(job_id=job_id, advert_id=advert_id, action=action)

    post_json_to_core(publish_url, json=data)

    user = get_logged_user()

    redirect_endpoint_name = \
        'edit_job' if user['role'] == 'ADMIN' else 'hr_edit_company_job'

    return redirect(url_for(redirect_endpoint_name, job_id=job_id))

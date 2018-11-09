from flask import url_for, request, redirect

from lib.auth import login_required, ADMIN_ROLE
from routes.common.advert import request_set_advert_status


@login_required(ADMIN_ROLE)
def set_advert_status_post(job_id: str, advert_id: str, action: str):
    data = {'duration': request.form.get('duration')}

    request_set_advert_status(action, advert_id, job_id, data)

    return redirect(url_for('edit_job', job_id=job_id))

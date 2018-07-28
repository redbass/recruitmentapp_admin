from flask import request, redirect, url_for

from lib.core_integration import post_json_to_core


def create_advert_post(job_id: str):
    data = {'duration': request.form.get('duration')}

    post_json_to_core('/api/job/{job_id}/advert'.format(job_id=job_id),
                      json=data)

    return redirect(url_for('edit_job', job_id=job_id))


def publish_advert_post(job_id: str, advert_id: str):
    data = {'duration': request.form.get('duration')}
    publish_url = '/api/job/{job_id}/advert/{advert_id}/publish'\
        .format(job_id=job_id, advert_id=advert_id)

    response = post_json_to_core(publish_url, json=data)

    return redirect(url_for('edit_job', job_id=job_id))

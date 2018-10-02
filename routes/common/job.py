from lib.core_integration import post_json_to_core
from lib.errors import flash_exception


def edit_job(form, job_id):

    if form.validate_on_submit():

        try:
            job = form.create_job_core_from_form()
            post_json_to_core('/api/job/' + job_id, json=job)

            return True

        except Exception as e:
            flash_exception(e)

    return False


def create_job(form):

    if form.validate_on_submit():

        try:
            job, advert = form.create_job_core_from_form()
            new_job = post_json_to_core('/api/job', json=job)

            job_id = new_job['_id']
            post_json_to_core('/api/job/{job_id}/advert'
                              .format(job_id=job_id), json=advert)
            return job_id

        except Exception as e:
            flash_exception(e)

    return None

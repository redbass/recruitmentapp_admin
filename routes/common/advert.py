
from lib.core_integration import post_json_to_core


def request_set_advert_status(action, advert_id, job_id, data=None):
    publish_url = '/api/job/{job_id}/advert/{advert_id}/{action}' \
        .format(job_id=job_id, advert_id=advert_id, action=action)
    return post_json_to_core(publish_url, json=data)

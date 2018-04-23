import requests
from flask import render_template, request

from config import settings
from lib.auth import login_required


@login_required
def list_jobs():

    jwt = request.cookies.get('jwt')
    url = settings.API_URL_ROOT + '/api/job'
    jobs = requests.get(url,
                        headers={'Authorization': 'Bearer ' + jwt})

    return render_template("jobs.jinja2", jobs=jobs.json()['results'])

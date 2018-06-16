import requests
from flask import render_template, request

from config import settings
from lib.auth import login_required


@login_required
def jobs_view():

    jwt = request.cookies.get('jwt')
    url = settings.CORE_APP_URL + '/api/job'
    resopnse = requests.get(url,
                        headers={'Authorization': 'Bearer ' + jwt})

    return render_template("jobs.jinja2", jobs=resopnse.json())

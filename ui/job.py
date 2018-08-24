from flask import render_template

from lib.auth import login_required
from lib.core_integration import get_json_from_core


@login_required
def jobs_view():
    jobs = get_json_from_core('/api/job')

    return render_template("job/jobs.jinja2", jobs=jobs)



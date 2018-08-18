from flask import render_template, request

from forms.job.form import JobForm
from lib.auth import login_required


@login_required
def create_job():
    form = JobForm(request.form)

    return render_template("job/create_job.jinja2", form=form)

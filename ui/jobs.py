from flask import render_template

from lib.auth import login_required


@login_required
def list_jobs():
    return render_template("jobs.jinja2")
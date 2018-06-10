from flask import render_template

from lib.auth import login_required


@login_required
def home_page():
    return render_template("index.jinja2")

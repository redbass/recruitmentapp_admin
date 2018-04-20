from flask import render_template


def home_page():
    return render_template("jobs.jinja2")

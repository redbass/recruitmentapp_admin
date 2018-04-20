from flask import render_template

from lib.auth import login_get, login_post, logout
from ui.home import home_page
from ui.jobs import list_jobs


def add_routes(app):

    @app.route('/')
    def hello_world():
        return render_template("index.jinja2")

    app.add_url_rule('/login', 'login_get', login_get, methods=['GET'])
    app.add_url_rule('/login', 'login_post', login_post, methods=['POST'])
    app.add_url_rule('/logout', 'logout', logout, methods=['GET'])

    app.add_url_rule('/', 'home', home_page, methods=['GET'])

    app.add_url_rule('/jobs', 'list_jobs', list_jobs, methods=['GET'])

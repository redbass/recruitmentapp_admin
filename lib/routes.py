from flask import render_template

from lib.auth import login_get, login_post


def add_routes(app):

    @app.route('/')
    def hello_world():
        return render_template("index.jinja2")

    app.add_url_rule('/login', 'login_get', login_get, methods=['GET'])
    app.add_url_rule('/login', 'login_post', login_post, methods=['POST'])

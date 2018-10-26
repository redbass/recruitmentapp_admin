from flask import render_template

from lib.auth import login_view, login_post, logout_view
from lib.exceptions import BaseRecruitmentAppException
from routes.admin_routes import add_admin_routes
from routes.common_routes import add_common_routes
from routes.hm_routes import add_hm_routes
from routes.home import home_page
from routes.services_routes import add_services_routes


def add_routes(app):
    _add_base_routes(app)
    _register_error_handlers(app)

    add_services_routes(app)
    add_admin_routes(app)
    add_hm_routes(app)
    add_common_routes(app)


def _add_base_routes(app):

    app.add_url_rule('/', 'home', home_page, methods=['GET'])

    app.add_url_rule('/login', 'login_view', login_view, methods=['GET'])
    app.add_url_rule('/login', 'login_post', login_post, methods=['POST'])
    app.add_url_rule('/logout', 'logout', logout_view, methods=['GET'])


def _register_error_handlers(app):

    @app.errorhandler(BaseRecruitmentAppException)
    def generic_error(e):
        return render_template('error.jinja2', error=e), 404

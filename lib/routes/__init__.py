from lib.auth import login_view, login_post, logout_view
from lib.routes.admin_routes import _add_job_routes, _add_advert_routes, _add_company_routes, add_admin_routes
from lib.routes.hm_routes import add_hm_routes
from lib.routes.services_routes import add_services_routes
from ui.home import home_page


def add_routes(app):
    _add_base_routes(app)

    add_services_routes(app)
    add_admin_routes(app)
    add_hm_routes(app)


def _add_base_routes(app):

    app.add_url_rule('/', 'home', home_page, methods=['GET'])

    app.add_url_rule('/login', 'login_view', login_view, methods=['GET'])
    app.add_url_rule('/login', 'login_post', login_post, methods=['POST'])
    app.add_url_rule('/logout', 'logout', logout_view, methods=['GET'])
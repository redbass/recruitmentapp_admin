from lib.auth import login_view, login_post, logout_view
from routes.admin_routes import add_admin_routes
from routes.hm_routes import add_hm_routes
from routes.home import home_page
from routes.services_routes import add_services_routes


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

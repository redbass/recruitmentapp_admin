from lib.auth import login_get, login_post, logout
from ui.home import home_page
from ui.job import jobs_view, create_job, create_job_post
from ui.company import companies_view, create_company_view, create_company_post


def add_routes(app):

    app.add_url_rule('/', 'home', home_page, methods=['GET'])
    _add_login_routes(app)
    _add_job_routes(app)
    _add_company_routes(app)


def _add_login_routes(app):
    app.add_url_rule('/login', 'login_get',
                     login_get, methods=['GET'])
    app.add_url_rule('/login', 'login_post',
                     login_post, methods=['POST'])
    app.add_url_rule('/logout', 'logout',
                     logout, methods=['GET'])


def _add_job_routes(app):
    app.add_url_rule('/jobs', 'jobs',
                     jobs_view, methods=['GET'])
    app.add_url_rule('/jobs/add', 'create_job',
                     create_job, methods=['GET'])
    app.add_url_rule('/jobs/add', 'create_job_post',
                     create_job_post, methods=['POST'])


def _add_company_routes(app):
    app.add_url_rule('/companies', 'companies',
                     companies_view, methods=['GET'])
    app.add_url_rule('/companies/add', 'create_company',
                     create_company_view, methods=['GET'])
    app.add_url_rule('/companies/add', 'create_company_post',
                     create_company_post, methods=['POST'])

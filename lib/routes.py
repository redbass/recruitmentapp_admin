from forms.company.routes import create_company_view, create_company_post, edit_company_view, edit_company_post
from lib.auth import login_view, login_post, logout_view
from ui.advert import publish_advert_post
from ui.home import home_page
from ui.job import jobs_view, create_job, create_job_post, edit_job_view, \
    edit_job_post
from ui.company import companies_view



def add_routes(app):

    app.add_url_rule('/', 'home', home_page, methods=['GET'])
    _add_login_routes(app)
    _add_job_routes(app)
    _add_advert_routes(app)
    _add_company_routes(app)


def _add_login_routes(app):
    app.add_url_rule('/login', 'login_view',
                     login_view, methods=['GET'])
    app.add_url_rule('/login', 'login_post',
                     login_post, methods=['POST'])
    app.add_url_rule('/logout', 'logout',
                     logout_view, methods=['GET'])


def _add_job_routes(app):
    app.add_url_rule('/jobs', 'jobs',
                     jobs_view, methods=['GET'])

    app.add_url_rule('/jobs/add', 'create_job',
                     create_job, methods=['GET'])
    app.add_url_rule('/jobs/add', 'create_job_post',
                     create_job_post, methods=['POST'])

    app.add_url_rule('/jobs/<job_id>', 'edit_job',
                     edit_job_view, methods=['GET'])
    app.add_url_rule('/jobs/<job_id>', 'edit_job_post',
                     edit_job_post, methods=['POST'])


def _add_advert_routes(app):
    app.add_url_rule('/jobs/<job_id>/advert/<advert_id>/publish',
                     'publish_advert_post',
                     publish_advert_post, methods=['POST'])


def _add_company_routes(app):
    app.add_url_rule('/companies', 'companies',
                     companies_view, methods=['GET'])

    app.add_url_rule('/companies/add', 'create_company',
                     create_company_view, methods=['GET'])
    app.add_url_rule('/companies/add', 'create_company_post',
                     create_company_post, methods=['POST'])

    app.add_url_rule('/companies/<company_id>', 'edit_company',
                     edit_company_view, methods=['GET'])
    app.add_url_rule('/companies/<company_id>', 'edit_company_post',
                     edit_company_post, methods=['POST'])


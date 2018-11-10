from routes.admin.company_routes import create_company_view, \
    create_company_post, edit_company_view, edit_company_post, companies_view
from routes.admin.job_routes import create_job_post, \
    edit_job_view, edit_job_post, jobs_view, create_job_view
from routes.admin.user import users_view

ADMIN_USERS = '/admin/users'

ADMIN_JOBS = '/admin/jobs'
ADMIN_JOBS_ADD = '/admin/jobs/add'
ADMIN_JOB = '/admin/jobs/<job_id>'

ADMIN_COMPANIES = '/admin/companies'
ADMIN_ADD_COMPANY = '/admin/companies/add'
ADMIN_COMPANY = '/admin/companies/<company_id>'

ADMIN_SIGN_IN_COMPANY = '/admin/companies/sign_in'


def add_admin_routes(app):
    _add_job_routes(app)
    _add_company_routes(app)
    _add_user_routes(app)


def _add_user_routes(app):
    app.add_url_rule(ADMIN_USERS, 'admin_users',
                     users_view, methods=['GET'])


def _add_job_routes(app):
    app.add_url_rule(ADMIN_JOBS, 'jobs',
                     jobs_view, methods=['GET'])

    app.add_url_rule(ADMIN_JOBS_ADD, 'create_job',
                     create_job_view, methods=['GET'])
    app.add_url_rule(ADMIN_JOBS_ADD, 'create_job_post',
                     create_job_post, methods=['POST'])

    app.add_url_rule(ADMIN_JOB, 'edit_job',
                     edit_job_view, methods=['GET'])
    app.add_url_rule(ADMIN_JOB, 'edit_job_post',
                     edit_job_post, methods=['POST'])


def _add_company_routes(app):
    app.add_url_rule(ADMIN_COMPANIES, 'companies',
                     companies_view, methods=['GET'])

    app.add_url_rule(ADMIN_ADD_COMPANY, 'create_company',
                     create_company_view, methods=['GET'])
    app.add_url_rule(ADMIN_ADD_COMPANY, 'create_company_post',
                     create_company_post, methods=['POST'])

    app.add_url_rule(ADMIN_COMPANY, 'edit_company',
                     edit_company_view, methods=['GET'])
    app.add_url_rule(ADMIN_COMPANY, 'edit_company_post',
                     edit_company_post, methods=['POST'])

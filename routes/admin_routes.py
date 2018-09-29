from routes.admin.company.routes import create_company_view, \
    create_company_post, edit_company_view, edit_company_post, companies_view
from routes.admin.job.routes import create_job, create_job_post, \
    edit_job_view, edit_job_post, set_advert_status, jobs_view

ADMIN_JOBS = '/admin/jobs'
ADMIN_JOBS_ADD = '/admin/jobs/add'
ADMIN_JOB = '/admin/jobs/<job_id>'

ADMIN_CREATE_ADVERT = '/admin/jobs/<job_id>/advert/<advert_id>/<action>'

ADMIN_COMPANIES = '/admin/companies'
ADMIN_ADD_COMPANY = '/admin/companies/add'
ADMIN_COMPANY = '/admin/companies/<company_id>'

ADMIN_SIGN_IN_COMPANY = '/admin/companies/sign_in'


def add_admin_routes(app):
    _add_job_routes(app)
    _add_advert_routes(app)
    _add_company_routes(app)


def _add_job_routes(app):
    app.add_url_rule(ADMIN_JOBS, 'jobs',
                     jobs_view, methods=['GET'])

    app.add_url_rule(ADMIN_JOBS_ADD, 'create_job',
                     create_job, methods=['GET'])
    app.add_url_rule(ADMIN_JOBS_ADD, 'create_job_post',
                     create_job_post, methods=['POST'])

    app.add_url_rule(ADMIN_JOB, 'edit_job',
                     edit_job_view, methods=['GET'])
    app.add_url_rule(ADMIN_JOB, 'edit_job_post',
                     edit_job_post, methods=['POST'])


def _add_advert_routes(app):
    app.add_url_rule(ADMIN_CREATE_ADVERT,
                     'set_advert_status',
                     set_advert_status, methods=['POST'])


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

from routes.admin.company_routes import create_company_view, \
    create_company_post, edit_company_view, edit_company_post, \
    companies_view, enable_company_post
from routes.admin.job_routes import create_job_post, \
    edit_job_view, edit_job_post, jobs_view, create_job_view
from routes.admin.settings import settings_view, upload_picklist, \
    download_picklist
from routes.admin.user import users_view, user_view, update_user_password

ADMIN_SETTINGS = '/admin/settings'
ADMIN_UPLOAD_PICKLIST = '/admin/picklist'
ADMIN_DOWNLOAD_PICKLIST = '/admin/picklist/<name>'

ADMIN_USERS = '/admin/users'
ADMIN_USER = '/admin/users/<user_id>'

ADMIN_JOBS = '/admin/jobs'
ADMIN_JOBS_ADD = '/admin/jobs/add'
ADMIN_JOB = '/admin/jobs/<job_id>'

ADMIN_COMPANIES = '/admin/companies'
ADMIN_ADD_COMPANY = '/admin/companies/add'
ADMIN_COMPANY = '/admin/companies/<company_id>'
ADMIN_COMPANY_ACTIONS = '/admin/companies/<company_id>/<action>'

ADMIN_SIGN_IN_COMPANY = '/admin/companies/sign_in'


def add_admin_routes(app):
    _add_job_routes(app)
    _add_company_routes(app)
    _add_user_routes(app)

    app.add_url_rule(ADMIN_SETTINGS, 'admin_settings',
                     settings_view, methods=['GET'])

    app.add_url_rule(ADMIN_DOWNLOAD_PICKLIST, 'download_picklist',
                     download_picklist, methods=['GET'])

    app.add_url_rule(ADMIN_UPLOAD_PICKLIST, 'upload_picklist',
                     upload_picklist, methods=['POST'])


def _add_user_routes(app):
    app.add_url_rule(ADMIN_USERS, 'admin_users',
                     users_view, methods=['GET'])
    app.add_url_rule(ADMIN_USER, 'admin_user',
                     user_view, methods=['GET'])
    app.add_url_rule(ADMIN_USER, 'update_user_password',
                     update_user_password, methods=['POST'])


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
    app.add_url_rule(ADMIN_COMPANY_ACTIONS, 'company_actions_post',
                     enable_company_post, methods=['POST'])

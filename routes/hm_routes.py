from routes.hiring_manager.company_routes import company_info, \
    company_info_post
from routes.hiring_manager.job_routes import company_jobs, \
    create_company_job, create_company_job_post, edit_company_job_view, \
    edit_company_job_view_post, archive_advert_post

HM_COMPANY = '/hr/company'
HM_COMPANY_JOBS = '/hr/company/jobs'
HR_COMPANY_JOB = '/hr/company/job'
HR_COMPANY_JOB_EDIT = '/hr/company/job/<job_id>'
HR_COMPANY_ADVERT_APPROVAL = \
    '/hr/company/job/<job_id>/requestapproval/<advert_id>'
HR_COMPANY_SET_ADVERT_STATUS = \
    '/hr/company/job/<job_id>/advert/<advert_id>/<action>'


def add_hm_routes(app):
    app.add_url_rule(HM_COMPANY, 'hr_company_info',
                     company_info, methods=['GET'])
    app.add_url_rule(HM_COMPANY, 'hr_company_info_post',
                     company_info_post, methods=['POST'])

    app.add_url_rule(HM_COMPANY_JOBS, 'hr_company_jobs',
                     company_jobs, methods=['GET'])
    app.add_url_rule(HR_COMPANY_JOB, 'hr_create_company_job',
                     create_company_job, methods=['GET'])
    app.add_url_rule(HR_COMPANY_JOB, 'hr_create_company_job_post',
                     create_company_job_post, methods=['POST'])

    app.add_url_rule(HR_COMPANY_JOB_EDIT, 'hr_edit_company_job',
                     edit_company_job_view, methods=['GET'])
    app.add_url_rule(HR_COMPANY_JOB_EDIT, 'hr_edit_company_job_post',
                     edit_company_job_view_post, methods=['POST'])

    app.add_url_rule(HR_COMPANY_SET_ADVERT_STATUS, 'hr_set_advert_status',
                     archive_advert_post, methods=['POST'])

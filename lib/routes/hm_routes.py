HR_COMPANY = '/hr/company'
HR_COMPANY_JOBS = '/hr/company/jobs'
HR_COMPANY_JOB = '/hr/company/job'

from forms.hm_company.routes import company_info, company_jobs, create_company_job


def add_hm_routes(app):
    app.add_url_rule(HR_COMPANY, 'hr_company_info',
                     company_info, methods=['GET'])

    app.add_url_rule(HR_COMPANY_JOBS, 'hr_company_jobs',
                     company_jobs, methods=['GET'])

    app.add_url_rule(HR_COMPANY_JOB, 'hr_create_company_job',
                     create_company_job, methods=['GET'])
    pass
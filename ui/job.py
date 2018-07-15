from flask import render_template, request, url_for, redirect

from lib.auth import login_required
from lib.core_integration import make_admin_core_api_call


@login_required
def jobs_view():
    response = make_admin_core_api_call('/api/job')
    return render_template("job/jobs.jinja2", jobs=response.json())


@login_required
def create_job():
    response = make_admin_core_api_call('/api/company')
    return render_template("job/create_job.jinja2", companies=response.json())


@login_required
def create_job_post():
    
    data = {
        "company_id": request.form.get('company_id'),
        "title": request.form.get('title'),
        "description": request.form.get('description'),
        "location": {
            "lat": request.form.get('latitude'),
            "lng": request.form.get('longitude')
        }
    }

    make_admin_core_api_call('/admin/api/job', data=data)

    return redirect(url_for('jobs'))


@login_required
def edit_job_view(job_id):
    job = make_admin_core_api_call('/api/job/' + job_id).json()

    companies = make_admin_core_api_call('/api/company').json()
    company = next(company for company in companies
                   if company['_id'] == job['company_id'])

    initial_market_latlng = {
        'lat': job['location']['coordinates'][1],
        'lng': job['location']['coordinates'][0]
    }

    return render_template("job/edit_job.jinja2",
                           job=job,
                           initial_market_latlng=initial_market_latlng,
                           company=company)


@login_required
def edit_job_post(job_id):

    data = {
        "title": request.form.get('title'),
        "description": request.form.get('description'),
        "location": {
            "lat": request.form.get('latitude'),
            "lng": request.form.get('longitude')
        }
    }

    make_admin_core_api_call('/api/job/' + job_id, data=data)

    return redirect(url_for('jobs'))
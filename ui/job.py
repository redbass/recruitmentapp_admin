from flask import render_template, request, url_for, redirect

from lib.auth import login_required
from lib.core_integration import get_json_from_core, post_json_to_core


@login_required
def jobs_view():
    jobs = get_json_from_core('/api/job')
    return render_template("job/jobs.jinja2", jobs=jobs)


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

    new_job = post_json_to_core('/api/job', json=data)

    data = {'duration': request.form.get('duration')}
    job_id = new_job['_id']

    result = post_json_to_core('/api/job/{job_id}/advert'
                               .format(job_id=job_id), json=data)

    return redirect(url_for('edit_job', job_id=job_id))


@login_required
def edit_job_view(job_id):
    job = get_json_from_core('/api/job/' + job_id)
    companies = get_json_from_core('/api/company')

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

    post_json_to_core('/api/job/' + job_id, json=data)

    return redirect(url_for('jobs'))

from io import StringIO

from flask import render_template, request, Response
from flask.json import jsonify

from lib import template_list
from lib.auth import login_required, ADMIN_ROLE
from lib.core_integration import post_json_to_core
from lib.errors import flash_message
from lib.picklist import csv_to_json_values, json_values_to_csv, \
    get_picklist_values


@login_required(ADMIN_ROLE)
def settings_view():
    return render_template(
        template_list.ADMIN_SETTINGS,
        company_trades=get_picklist_values('company_trades'),
        job_title=get_picklist_values('job_titles'),
        job_duration=get_picklist_values('job_durations'),
        job_locations=get_picklist_values('job_locations'),
        job_rates=get_picklist_values('job_rates'))


@login_required(ADMIN_ROLE)
def upload_picklist():
    stream = request.files['file'].stream
    picklist_name = request.form['picklist_name']

    file_content = StringIO(stream.read().decode("utf-8"))

    result = csv_to_json_values(file_content)

    post_json_to_core(path='/api/picklist/' + picklist_name,
                      is_admin=False, json=result)

    flash_message("Upload Completed")

    return jsonify({})


@login_required(ADMIN_ROLE)
def download_picklist(name):
    values = get_picklist_values(entity_name=name)
    csv = json_values_to_csv(json_values=values)

    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename={name}.csv".format(name=name)})

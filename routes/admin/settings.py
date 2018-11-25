from flask import render_template

from lib import template_list
from lib.auth import login_required, ADMIN_ROLE
from lib.core_integration import get_json_from_core


def get_picklist_values(entity_name):
    entities = get_json_from_core(path='/api/picklist/' + entity_name,
                                  is_admin=False)

    return [(entity.get('key'), entity.get('value')) for entity in entities]


@login_required(ADMIN_ROLE)
def settings_view():
    return render_template(
        template_list.ADMIN_SETTINGS,
        company_trades=get_picklist_values('company_trades'),
        job_title=get_picklist_values('job_titles'),
        job_duration=get_picklist_values('job_durations'),
        job_rates=get_picklist_values('job_rates'))

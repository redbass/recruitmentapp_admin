from flask import render_template

from lib import template_list
from lib.auth import login_required, ADMIN_ROLE
from lib.enums import DURATIONS, JOB_TITLES, RATES, TRADES_VALUES


@login_required(ADMIN_ROLE)
def settings_view():

    return render_template(template_list.ADMIN_SETTINGS,
                           job_title=JOB_TITLES, company_trades=TRADES_VALUES,
                           job_duration=DURATIONS, job_rates=RATES)

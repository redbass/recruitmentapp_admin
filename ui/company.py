from flask import render_template

from lib.auth import login_required
from lib.core_integration import get_json_from_core


@login_required
def companies_view():
    companies = get_json_from_core('/api/company')
    return render_template("company/companies.jinja2", companies=companies)

from flask import request, url_for, redirect

from config import settings
from lib.auth import login_required
from lib.core_integration import post_json_to_core
from lib.errors import flash_exception
from lib.exceptions import APICallError

DEFAULT_CURRENCY = 'GBP'
DEFAULT_ADVERT_CHARGE = 2000
DEFAULT_CHARGE_DESCRIPTION = 'Single Payment'


def get_default_stripe_parameters():
    return {
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'default_currency': DEFAULT_CURRENCY,
        'default_advert_charge': DEFAULT_ADVERT_CHARGE
    }


@login_required()
def create_charge(job_id, advert_id):
    token = request.form['stripeToken']  # Using Flask
    data = {
        'job_id': job_id,
        'advert_id': advert_id,
        'token': token
    }

    try:
        post_json_to_core('/api/stripe/charge', json=data, is_admin=False)
    except APICallError as e:
        flash_exception(e)

    return redirect(url_for('hr_edit_company_job',
                            job_id=job_id,
                            advert_id=advert_id))

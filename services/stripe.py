import stripe
from flask import request, url_for, redirect

from config import settings
from lib.auth import login_required

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
    stripe.api_key = settings.STRIPE_SECRET_KEY

    token = request.form['stripeToken']  # Using Flask

    stripe.Charge.create(
        amount=DEFAULT_ADVERT_CHARGE,
        currency=DEFAULT_CURRENCY,
        description=DEFAULT_CHARGE_DESCRIPTION,
        source=token,
        metadata={
            'job_id': job_id,
            'advert_id': advert_id
        }
    )

    return redirect(url_for('hr_edit_company_job',
                            job_id=job_id,
                            advert_id=advert_id))

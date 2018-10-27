from flask_wtf import CSRFProtect

from services import stripe


def _protect_app_csrf(__app__):
    csrf = CSRFProtect(__app__)
    csrf.exempt(stripe.create_charge)
    return csrf

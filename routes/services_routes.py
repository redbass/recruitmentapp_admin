from services import postcode, stripe

POSTCODE_SEARCH = '/postcode/<postcode>'
STRIPE_PAY_ADVERT = '/admin/jobs/<job_id>/advert/<advert_id>/pay_advert'


def add_services_routes(app):

    app.add_url_rule(POSTCODE_SEARCH, 'postcode',
                     postcode.get_postcode, methods=['GET'])

    app.add_url_rule(STRIPE_PAY_ADVERT, 'stripe_charge',
                     stripe.create_charge, methods=['POST'])

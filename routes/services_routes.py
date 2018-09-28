from lib.services import get_postcode


def add_services_routes(app):
    app.add_url_rule('/postcode/<postcode>', 'postcode',
                     get_postcode, methods=['GET'])

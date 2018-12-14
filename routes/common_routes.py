from routes.common.company import get_company_logo, post_company_logo

COMMON_COMPANY_LOGO = '/company/<company_id>/logo'


def add_common_routes(app):
    app.add_url_rule(COMMON_COMPANY_LOGO,
                     'get_company_logo',
                     get_company_logo, methods=['GET'])

    app.add_url_rule(COMMON_COMPANY_LOGO,
                     'upload_company_logo',
                     post_company_logo, methods=['POST'])

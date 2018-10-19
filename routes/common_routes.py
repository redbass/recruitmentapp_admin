from routes.common.advert import set_advert_status
from routes.common.company import get_company_logo, post_company_logo

COMMON_SET_ADVERT_STATUS = '/admin/jobs/<job_id>/advert/<advert_id>/<action>'

COMMON_COMPANY_LOGO = '/company/<company_id>/logo'


def add_common_routes(app):
    app.add_url_rule(COMMON_SET_ADVERT_STATUS,
                     'set_advert_status',
                     set_advert_status, methods=['POST'])

    app.add_url_rule(COMMON_COMPANY_LOGO,
                     'get_company_logo',
                     get_company_logo, methods=['GET'])

    app.add_url_rule(COMMON_COMPANY_LOGO,
                     'upload_company_logo',
                     post_company_logo, methods=['POST'])

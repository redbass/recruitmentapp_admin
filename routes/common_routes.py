from routes.admin.common.routes import set_advert_status

COMMON_SET_ADVERT_STATUS = '/admin/jobs/<job_id>/advert/<advert_id>/<action>'


def add_common_routes(app):
    app.add_url_rule(COMMON_SET_ADVERT_STATUS,
                     'set_advert_status',
                     set_advert_status, methods=['POST'])

from time import strptime, strftime

from config import settings
from lib.auth import get_logged_user
from lib.picklist import get_picklist_values
from services.stripe import get_default_stripe_parameters


def register_filters(app):

    @app.template_filter('format_date')
    def format_date(date_str):
        datetime_object = strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')
        return strftime('%H:%M - %Y-%m-%d', datetime_object)

    @app.template_filter('map_picklist_value')
    def map_picklist_value(values, picklist_name):
        if not isinstance(values, list):
            values = [values]

        picklist = get_picklist_values(picklist_name, as_dict=True)

        result = []
        for val in values:
            label = _get_picklist_val(val, picklist)
            if label:
                result.append(label)

        return result

    def _get_picklist_val(val, picklist):
        return next((p[1] for p in picklist if p[0] == val), None)


def register_variables(app):

    @app.context_processor
    def variables():
        return {
            'user_info': get_logged_user(),
            'stripe_settings': get_default_stripe_parameters,
            'marketing_website_url': settings.MARKETING_WEBSITE_URL
        }

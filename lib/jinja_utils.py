from time import strptime, strftime

from lib.auth import get_logged_user


def register_filters(app):

    @app.template_filter('format_date')
    def format_date(date_str):
        datetime_object = strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')
        return strftime('%H:%M - %Y-%m-%d', datetime_object)


def register_variables(app):

    @app.context_processor
    def user_info():
        return {'user_info': get_logged_user()}

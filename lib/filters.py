from time import strptime, strftime


def register_filters(app):

    @app.template_filter('format_date')
    def format_date(date_str):
        datetime_object = strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')
        return strftime('%H:%M - %Y-%m-%d', datetime_object)


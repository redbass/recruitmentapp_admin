import os


class BaseConfig(object):
    DEBUG_MODE = False
    TEST = False

    DEFAULT_PORT = None

    LOGIN_REQUIRED = True

    MARKETING_WEBSITE_URL = os.environ.get('MARKETING_WEBSITE_URL', '#')

    CORE_APP_URL = os.environ.get('CORE_APP_URL', '')

    def __init__(self):
        self.CORE_APP_ADMIN_URL = self.CORE_APP_URL + "/admin"


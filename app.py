from flask import Flask

from config import settings
from lib.csrf import _protect_app_csrf
from lib.jinja_utils import register_filters, register_variables
from routes import add_routes

__app__ = None
__csrf__ = None


def get_app(*args, **kwarg) -> Flask:

    global __app__
    global __csrf__

    if not __app__:
        __app__ = Flask(__name__, *args, **kwarg)
        __app__.config.update(
            SECRET_KEY='secret_xxx'  # TODO: SET REAL ONE
        )
        add_routes(__app__)
        register_filters(__app__)
        register_variables(__app__)

        if settings.DEBUG_MODE:
            __app__.jinja_env.auto_reload = True

            __csrf__ = _protect_app_csrf(__app__)

    return __app__


if __name__ == '__main__':
    get_app().run(debug=settings.DEBUG_MODE, port=settings.DEFAULT_PORT)

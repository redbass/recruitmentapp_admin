from flask import Flask
from flask_wtf import CSRFProtect

from config import settings
from lib.jinja_utils import register_filters, register_variables
from lib.routes import add_routes

_app = None


def get_app(*args, **kwarg) -> Flask:

    global _app

    if not _app:
        _app = Flask(__name__, *args, **kwarg)
        _app.config.update(
            SECRET_KEY='secret_xxx'  # TODO: SET REAL ONE
        )
        add_routes(_app)
        register_filters(_app)
        register_variables(_app)

        if settings.DEBUG_MODE:
            _app.jinja_env.auto_reload = True

        CSRFProtect(_app)

    return _app


if __name__ == '__main__':
    get_app().run(debug=settings.DEBUG_MODE, port=settings.DEFAULT_PORT)

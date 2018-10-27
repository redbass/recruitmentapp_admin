from flask import Flask
from flask_wtf import CSRFProtect

from config import settings
from lib.jinja_utils import register_filters, register_variables
from routes import add_routes
from services.stripe import create_charge

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

        _csrf = CSRFProtect(_app)
        _csrf.exempt(create_charge)

    return _app


if __name__ == '__main__':
    get_app().run(debug=settings.DEBUG_MODE, port=settings.DEFAULT_PORT)

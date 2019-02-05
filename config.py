import os

from lib.base_config import BaseConfig

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_SRC = os.path.join(APP_ROOT, 'src')


class ProductionConfig(BaseConfig):
    pass


class StagingConfig(BaseConfig):
    pass


class DevConfig(BaseConfig):
    pass


class LocalConfig(BaseConfig):
    DEBUG_MODE = True
    DEFAULT_PORT = 5001


def _get_settings():
    app_env = os.environ.get('APP_ENV')

    app_configs = {
        'local': LocalConfig,
        'dev': DevConfig,
        'staging': StagingConfig,
        'production': ProductionConfig
    }

    if app_env not in app_configs.keys():
        raise Exception('APP_ENV "{app_env}" not supported'
                        .format(app_env=app_env))

    return app_configs.get(app_env)()


settings = _get_settings()

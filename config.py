import os

from lib.base_config import BaseConfig


class StagingConfig(BaseConfig):
    ENC_SEED = 'toBeUpdated'
    ENC_PSWD = None


class DevConfig(BaseConfig):
    DEBUG_MODE = True
    DEFAULT_PORT = 5001


def _get_settings():
    app_env = os.environ.get('APP_ENV')

    app_configs = {
        'dev': DevConfig,
        'staging': StagingConfig
    }

    if app_env not in app_configs.keys():
        raise Exception('APP_ENV "{app_env}" not supported'.format(app_env=app_env))

    return app_configs.get(app_env)()


settings = _get_settings()

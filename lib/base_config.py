import os
from Crypto.Cipher import AES


class BaseConfig(object):
    DEBUG_MODE = False
    TEST = False

    DEFAULT_PORT = None

    LOGIN_REQUIRED = True

    ENC_SEED = None
    ENC_PSWD = None

    STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY', None)

    def __init__(self):
        self.CORE_APP_URL = os.environ.get('CORE_APP_URL')
        self.CORE_APP_ADMIN_URL = self.CORE_APP_URL + "/admin"
        self.ENC_PSWD = os.environ.get('ENC_PSWD', None)

    def encrypt(self, msg: str):
        aes = AES.new(self.ENC_PSWD, AES.MODE_CBC, self.ENC_SEED)
        return aes.encrypt(msg).hex()

    def decrypt(self, cipher_hex: str):
        b_cipher_hex = bytes(bytearray.fromhex(cipher_hex))
        aes = AES.new(self.ENC_PSWD, AES.MODE_CBC, self.ENC_SEED)
        return aes.decrypt(b_cipher_hex).decode()

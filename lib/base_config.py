import os
from Crypto.Cipher import AES


class BaseConfig(object):
    DEBUG_MODE = False
    TEST = False

    DEFAULT_PORT = None

    LOGIN_REQUIRED = True

    ENC_SEED = None
    ENC_PSWD = None

    def __init__(self):
        self.API_URL_ROOT = os.environ.get('API_URL')
        self.ENC_PSWD = os.environ.get('ENC_PSWD', None)

    def encrypt(self, msg: str):
        aes = AES.new(self.ENC_PSWD, AES.MODE_CBC, self.ENC_SEED)
        return aes.encrypt(msg).hex()

    def decrypt(self, cipher_hex: str):
        b_cipher_hex = bytes(bytearray.fromhex(cipher_hex))
        aes = AES.new(self.ENC_PSWD, AES.MODE_CBC, self.ENC_SEED)
        return aes.decrypt(b_cipher_hex).decode()

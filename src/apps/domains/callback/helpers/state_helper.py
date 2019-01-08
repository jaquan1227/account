from datetime import datetime
from django.core.exceptions import PermissionDenied
from django.conf import settings
from lib.crypto.encrypt import CryptoHelper
import json

CRYPTO_KEY = settings.STATE_CRYPTO_KEY
EXPIRE_TIME = 10


class StateHelper:
    @staticmethod
    def create_encrypted_state(u_idx: str) -> str:
        state = {'time': datetime.now().timestamp(), 'u_idx': u_idx}
        return CryptoHelper(CRYPTO_KEY).encrypt(json.dumps(state))

    @staticmethod
    def _decrypt_state(state: str) -> dict:
        decrypted_str = CryptoHelper(CRYPTO_KEY).decrypt(state)
        if not decrypted_str:
            raise PermissionDenied()
        return json.loads(decrypted_str)

    @classmethod
    def validate_state(cls, state: str, u_idx: str):
        decrypted_data = cls._decrypt_state(state)
        if decrypted_data['u_idx'] != u_idx:
            raise PermissionDenied()
        if decrypted_data['time'] + EXPIRE_TIME < datetime.now().timestamp():
            raise PermissionDenied()
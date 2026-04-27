import abc
from functools import partial

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.hmac import HMAC

from noise.functions.hash import Hash

cryptography_backend = default_backend()


class CryptographyHash(Hash, metaclass=abc.ABCMeta):
    def hash(self, data):
        pass


class SHA256Hash(CryptographyHash):
    @property
    def fn(self):
        pass

    @property
    def hashlen(self):
        pass

    @property
    def blocklen(self):
        pass


class SHA512Hash(CryptographyHash):
    @property
    def fn(self):
        pass

    @property
    def hashlen(self):
        pass

    @property
    def blocklen(self):
        pass


class BLAKE2sHash(CryptographyHash):
    @property
    def fn(self):
        pass

    @property
    def hashlen(self):
        pass

    @property
    def blocklen(self):
        pass


class BLAKE2bHash(CryptographyHash):
    @property
    def fn(self):
        pass

    @property
    def hashlen(self):
        pass

    @property
    def blocklen(self):
        pass


def hmac_hash(key, data, algorithm):
    # Applies HMAC using the HASH() function.
    hmac = HMAC(key=key, algorithm=algorithm(), backend=cryptography_backend)
    hmac.update(data=data)
    return hmac.finalize()

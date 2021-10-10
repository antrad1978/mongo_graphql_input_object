import hashlib
import os


class HashHelper:
    @staticmethod
    def hashed(string: str) -> str:
        """Return the hash of string.
        >>> HashHelper.hashed("a")
        '499068847922a74b2c2cf35f3c23c6e7e5aff3f653b3ffaff2f9d4f543ad0ef175a490e3be17385faeb0460e9dcba301e55188d84a6d9095f3e202ae7b3a070c'
        >>> HashHelper.hashed(1)
        Traceback (most recent call last):
            ...
        AttributeError: 'int' object has no attribute 'encode'

        Factorials of floats are OK, but the float must be an exact integer:
        """
        salt = os.environ.get('SALT', 'bb044444a5678cae9a181fc5633c9fa1').encode('utf-8')
        return hashlib.sha512(bytearray(string.encode('utf-8')) + bytearray(salt)).hexdigest()

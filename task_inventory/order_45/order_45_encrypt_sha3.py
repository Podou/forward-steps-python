
import hashlib


class EncryptSha3(object):

    @staticmethod
    def sha3_224(text=''):
        sha224_hashlib = hashlib.sha3_224()
        sha224_hashlib.update(text.encode('utf8'))
        return sha224_hashlib.hexdigest()

    @staticmethod
    def sha3_256(text=''):
        sha256_hashlib = hashlib.sha3_256()
        sha256_hashlib.update(text.encode('utf8'))
        return sha256_hashlib.hexdigest()

    @staticmethod
    def sha3_384(text=''):
        sha384_hashlib = hashlib.sha3_384()
        sha384_hashlib.update(text.encode('utf8'))
        return sha384_hashlib.hexdigest()

    @staticmethod
    def sha3_512(text=''):
        sha512_hashlib = hashlib.sha3_512()
        sha512_hashlib.update(text.encode('utf8'))
        return sha512_hashlib.hexdigest()


import hashlib


class EncryptSha(object):

    @staticmethod
    def sha1(text=''):
        sha1_hashlib = hashlib.sha1()
        sha1_hashlib.update(text.encode('utf8'))
        return sha1_hashlib.hexdigest()

    @staticmethod
    def sha224(text=''):
        sha224_hashlib = hashlib.sha224()
        sha224_hashlib.update(text.encode('utf8'))
        return sha224_hashlib.hexdigest()

    @staticmethod
    def sha256(text=''):
        sha256_hashlib = hashlib.sha256()
        sha256_hashlib.update(text.encode('utf8'))
        return sha256_hashlib.hexdigest()

    @staticmethod
    def sha384(text=''):
        sha384_hashlib = hashlib.sha384()
        sha384_hashlib.update(text.encode('utf8'))
        return sha384_hashlib.hexdigest()

    @staticmethod
    def sha512(text=''):
        sha512_hashlib = hashlib.sha512()
        sha512_hashlib.update(text.encode('utf8'))
        return sha512_hashlib.hexdigest()

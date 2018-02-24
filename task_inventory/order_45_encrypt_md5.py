import hashlib


class EncryptMd5(object):

    @staticmethod
    def md5(text=''):
        md5_hashlib = hashlib.md5()
        md5_hashlib.update(text.encode('utf8'))
        return md5_hashlib.hexdigest()

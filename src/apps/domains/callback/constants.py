import typing

from lib.base.constants import BaseConstant

ROOT_DOMAIN_SESSION_KEY = 'root_domain'


class CookieRootDomains(BaseConstant):
    DEV_RIDI_COM = 0
    DEV_RIDI_IO = 1
    RIDI_IO = 2

    PROD_RIDI_COM = 10

    _LIST = [DEV_RIDI_COM, RIDI_IO, DEV_RIDI_IO, PROD_RIDI_COM]
    _STRING_MAP = {
        DEV_RIDI_COM: 'dev.ridi.com',
        DEV_RIDI_IO: 'dev.ridi.io',
        RIDI_IO: 'ridi.io',
        PROD_RIDI_COM: 'ridibooks.com'
    }

    @classmethod
    def get_root_whitelist(cls, debug: bool) -> typing.List[str]:
        if debug:
            return [cls.to_string(cls.DEV_RIDI_COM), cls.to_string(cls.RIDI_IO)]

        return [cls.to_string(cls.PROD_RIDI_COM)]

from django.urls import reverse

from infra.configure.config import GeneralConfig
from lib.cache.memorize import memorize
from lib.utils.url import generate_query_url


class UrlHelper:
    @staticmethod
    @memorize
    def get_callback_view_url() -> str:
        return f'https://{GeneralConfig.get_site_domain()}{reverse("ridi:callback")}'

    @classmethod
    @memorize
    def get_redirect_url(cls, in_house_redirect_uri: str, client_id: str) -> str:
        return generate_query_url(cls.get_callback_view_url(), {'in_house_redirect_uri': in_house_redirect_uri, 'client_id': client_id})

    @staticmethod
    @memorize
    def get_root_uri() -> str:
        return GeneralConfig.get_store_url()

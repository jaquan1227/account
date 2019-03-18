from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from oauth2_provider.models import AbstractApplication

from apps.domains.oauth2.models import Application
from lib.utils.url import is_same_url_until_domain, is_same_url


class ClientService:
    @classmethod
    def get_client(cls, client_id: str) -> Application:
        try:
            client = Application.objects.get(client_id=client_id)
        except ObjectDoesNotExist:
            raise PermissionDenied()

        if client.authorization_grant_type != AbstractApplication.GRANT_AUTHORIZATION_CODE:
            raise NotImplementedError()

        return client

    @classmethod
    def get_in_house_client(cls, client_id: str) -> Application:
        client = cls.get_client(client_id)

        if not client.is_in_house:
            raise PermissionDenied()

        return client

    @staticmethod
    def assert_in_house_client_redirect_uri(client: Application, redirect_uri: str):
        if not client.is_in_house:
            raise PermissionDenied()

        for client_redirect_uri in client.redirect_uris.split():
            if is_same_url_until_domain(redirect_uri, client_redirect_uri):
                return

        raise PermissionDenied()

    @classmethod
    def assert_house_client_redirect_uri(cls, client: Application, redirect_uri: str):
        if client.is_in_house:
            cls.assert_in_house_client_redirect_uri(client, redirect_uri)
            return

        for client_redirect_uri in client.redirect_uris.split():
            if is_same_url(redirect_uri, client_redirect_uri):
                return

        raise PermissionDenied()

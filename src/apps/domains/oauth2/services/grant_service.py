from apps.domains.oauth2.models import Application as Client
from apps.domains.oauth2.repositories.grant_repository import GrantRepository


class GrantService:
    @staticmethod
    def create_grant(client: Client, redirect_uri: str, u_idx: int, scope='all'):
        grant = GrantRepository.create_grant(client, redirect_uri, u_idx, scope)
        return grant
#

from typing import Tuple

import requests

from apps.domains.callback.dtos import TokenData
from apps.domains.callback.helpers.url_helper import UrlHelper
from apps.domains.oauth2.models import Application
from infra.configure.config import GeneralConfig


class TokenRequestHelper:
    @staticmethod
    def _generate_token_from_json(response_json: dict) -> Tuple[TokenData, TokenData]:
        access_token = response_json.get('access_token', None)
        access_token_expires_in = response_json.get('expires_in', None)

        refresh_token = response_json.get('refresh_token', None)
        refresh_token_expire_in = response_json.get('refresh_token_expires_in', None)

        return TokenData(access_token, access_token_expires_in), TokenData(refresh_token, refresh_token_expire_in)

    @classmethod
    def get_tokens(cls, grant_type: str, client: Application, **data) -> Tuple[TokenData, TokenData]:
        verify = not GeneralConfig.is_dev()
        req = requests.post(
            UrlHelper.get_oauth2_token_url(), data=cls._get_request_data(data, grant_type, client), verify=verify,
        )
        req.raise_for_status()

        json = req.json()
        return cls._generate_token_from_json(json)

    @staticmethod
    def _get_request_data(data: dict, grant_type: str, client: Application) -> dict:
        data['grant_type'] = grant_type
        data['client_id'] = client.client_id
        data['client_secret'] = client.client_secret
        return data
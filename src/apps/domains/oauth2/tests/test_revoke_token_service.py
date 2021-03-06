from datetime import datetime

from django.test import TestCase
from django_dynamic_fixture import G

from apps.domains.account.models import User
from apps.domains.oauth2.models import Grant, RefreshToken
from apps.domains.oauth2.services.revoke_token_service import RevokeTokenService


class RevokeTokenServiceTestCase(TestCase):
    def setUp(self):
        user = G(User, idx=1, id='testuser')
        G(RefreshToken, user=user, token='1234', expires=datetime(year=1970, month=1, day=1))
        G(Grant, user=user, code='1111', expires=datetime(year=1970, month=1, day=1))

    def test_token_expired(self):
        RevokeTokenService.revoke_expired()

        refresh_tokens = RefreshToken.objects.all()
        grants = Grant.objects.all()

        self.assertFalse(refresh_tokens.exists())
        self.assertFalse(grants.exists())

    def test_token_expire_specific_datetime(self):
        RevokeTokenService.revoke_by_expires(expires=datetime(year=1970, month=1, day=1))

        refresh_tokens = RefreshToken.objects.all()
        grants = Grant.objects.all()

        self.assertTrue(refresh_tokens.exists())
        self.assertTrue(grants.exists())

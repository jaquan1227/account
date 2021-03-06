# pylint: disable=protected-access
import json
from datetime import datetime

import requests_mock
from django.http import SimpleCookie
from django.test import Client, TestCase
from django.urls import reverse
from django_dynamic_fixture import G

from apps.domains.account.models import User
from apps.domains.ridi.helpers.url_helper import UrlHelper
from apps.domains.oauth2.models import Application, RefreshToken
from apps.domains.oauth2.token import JwtHandler
from infra.configure.config import GeneralConfig
from lib.ridibooks.api.store import StoreApi
from lib.ridibooks.common.constants import ACCESS_TOKEN_COOKIE_KEY, REFRESH_TOKEN_COOKIE_KEY


class InHouseCallbackTestCase(TestCase):
    """
    AuthorizeView 와 CallbackView를 함께 테스트한다.
    """
    pass


class TokenViewTestCase(TestCase):
    def setUp(self):
        self.user = G(User, idx=1, id='testuser')
        self.client = G(Application, skip_authorization=True, user=None, is_in_house=True)
        self.refresh_token = G(
            RefreshToken, user=self.user, application=self.client, token='refresh-token', expires=datetime(year=9999, month=12, day=31)
        )

    def test_no_cookie(self):
        response = Client().post(reverse('ridi:token'), HTTP_HOST=GeneralConfig.get_site_domain(), secure=True)

        self.assertEqual(response.status_code, 401)

        self.assertIn(ACCESS_TOKEN_COOKIE_KEY, response.cookies)
        self.assertIn(REFRESH_TOKEN_COOKIE_KEY, response.cookies)
        self.assertEqual(response.cookies[ACCESS_TOKEN_COOKIE_KEY]['max-age'], 0)
        self.assertEqual(response.cookies[REFRESH_TOKEN_COOKIE_KEY]['max-age'], 0)

    def test_refresh_success(self):
        api = StoreApi()
        with requests_mock.mock() as m:
            m.get(api._make_url(StoreApi.ACCOUNT_INFO), json={'result': {'idx': 1, 'id': 'testuser'}})

            response = Client().post(
                reverse('ridi:token'),
                HTTP_HOST=GeneralConfig.get_site_domain(),
                HTTP_COOKIE=SimpleCookie({'ridi-rt': self.refresh_token.token, 'ridi-al': '1'}).output(header='', sep='; '),
                secure=True
            )

        self.assertEqual(response.status_code, 200)

        data = json.dumps(response.content.decode('utf8'))
        self.assertIn('expires_at', data)
        self.assertIn('expires_in', data)

        self.assertIn(ACCESS_TOKEN_COOKIE_KEY, response.cookies)
        self.assertIn(REFRESH_TOKEN_COOKIE_KEY, response.cookies)

        self.assertGreater(response.cookies[ACCESS_TOKEN_COOKIE_KEY]['max-age'], 0)
        self.assertGreater(response.cookies[REFRESH_TOKEN_COOKIE_KEY]['max-age'], 0)

    def test_refresh_success_without_auto_login(self):
        api = StoreApi()
        with requests_mock.mock() as m:
            m.get(api._make_url(StoreApi.ACCOUNT_INFO), json={'result': {'idx': 1, 'id': 'testuser'}})
            response = Client().post(
                reverse('ridi:token'),
                HTTP_HOST=GeneralConfig.get_site_domain(),
                HTTP_COOKIE=SimpleCookie({'ridi-rt': self.refresh_token.token}).output(header='', sep='; '),
                secure=True
            )

        self.assertEqual(response.status_code, 200)

        data = json.dumps(response.content.decode('utf8'))
        self.assertIn('expires_at', data)
        self.assertIn('expires_in', data)

        self.assertIn(ACCESS_TOKEN_COOKIE_KEY, response.cookies)
        self.assertIn(REFRESH_TOKEN_COOKIE_KEY, response.cookies)

        self.assertEqual(response.cookies[ACCESS_TOKEN_COOKIE_KEY]['max-age'], '')
        self.assertEqual(response.cookies[ACCESS_TOKEN_COOKIE_KEY]['expires'], '')
        self.assertEqual(response.cookies[REFRESH_TOKEN_COOKIE_KEY]['max-age'], '')
        self.assertEqual(response.cookies[REFRESH_TOKEN_COOKIE_KEY]['expires'], '')

    def test_refresh_success_with_auto_login_is_zero(self):
        api = StoreApi()
        with requests_mock.mock() as m:
            m.get(api._make_url(StoreApi.ACCOUNT_INFO), json={'result': {'idx': 1, 'id': 'testuser'}})
            response = Client().post(
                reverse('ridi:token'),
                HTTP_HOST=GeneralConfig.get_site_domain(),
                HTTP_COOKIE=SimpleCookie({'ridi-rt': self.refresh_token.token, 'ridi-al': '0'}).output(header='', sep='; '),
                secure=True
            )

        self.assertEqual(response.status_code, 200)

        data = json.dumps(response.content.decode('utf8'))
        self.assertIn('expires_at', data)
        self.assertIn('expires_in', data)

        self.assertIn(ACCESS_TOKEN_COOKIE_KEY, response.cookies)
        self.assertIn(REFRESH_TOKEN_COOKIE_KEY, response.cookies)

        self.assertEqual(response.cookies[ACCESS_TOKEN_COOKIE_KEY]['max-age'], '')
        self.assertEqual(response.cookies[ACCESS_TOKEN_COOKIE_KEY]['expires'], '')

        self.assertEqual(response.cookies[REFRESH_TOKEN_COOKIE_KEY]['max-age'], '')
        self.assertEqual(response.cookies[REFRESH_TOKEN_COOKIE_KEY]['expires'], '')

    def test_not_refresh_but_success(self):
        class req:
            user = self.user
            client = self.client
            scopes = ['all']

        at = JwtHandler.generate(req)

        response = Client().post(
            reverse('ridi:token'),
            HTTP_HOST=GeneralConfig.get_site_domain(), HTTP_COOKIE=SimpleCookie({'ridi-at': at}).output(header='', sep='; '),
            secure=True
        )

        self.assertEqual(response.status_code, 200)

        data = json.dumps(response.content.decode('utf8'))
        self.assertIn('expires_at', data)
        self.assertIn('expires_in', data)


class LogoutViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_logout(self):
        response = self.client.get(
            reverse('ridi:logout') + '?return_url=https://test.com', HTTP_HOST=GeneralConfig.get_site_domain(), secure=True
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, 'https://test.com')

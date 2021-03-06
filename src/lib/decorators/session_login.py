from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponseRedirect
from django.urls import reverse

from lib.ridibooks.api.store import StoreApi
from lib.ridibooks.common.constants import PHP_SESSION_COOKIE_KEY
from lib.ridibooks.common.exceptions import RidibooksException
from lib.utils.url import generate_query_url


def ridibooks_session_login():
    def decorator(_func):
        def wrapper(self, request, *args, **kwargs):
            ridibooks_session_id = request.COOKIES.get(PHP_SESSION_COOKIE_KEY, None)
            user = AnonymousUser()

            if ridibooks_session_id is not None:

                try:
                    account_info = StoreApi(phpsession_id=ridibooks_session_id).get_account_info()

                except RidibooksException:
                    pass

                else:
                    user, _ = get_user_model().objects.get_or_create(idx=account_info['result']['idx'], id=account_info['result']['id'])

            request.user = user

            return _func(self, request, *args, **kwargs)

        return wrapper

    return decorator


def ridibooks_session_login_required():
    def decorator(_func):
        def wrapper(self, request, *args, **kwargs):
            ridibooks_session_id = request.COOKIES.get(PHP_SESSION_COOKIE_KEY, None)
            user = AnonymousUser()

            if ridibooks_session_id is not None:

                try:
                    account_info = StoreApi(phpsession_id=ridibooks_session_id).get_account_info()

                except RidibooksException:
                    pass

                else:
                    user, _ = get_user_model().objects.get_or_create(idx=account_info['result']['idx'], id=account_info['result']['id'])
            if not user.is_authenticated:
                redirect_uri = generate_query_url(reverse('account:login'), {'next': request.get_full_path()})
                return HttpResponseRedirect(redirect_uri)

            request.user = user

            return _func(self, request, *args, **kwargs)

        return wrapper

    return decorator

from django.contrib.auth import login
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from ridi.cms.cms_client import AdminAuth

from ridi.cms.login_session import COOKIE_CMS_TOKEN, LoginSession

from apps.domains.account.models import Staff
from lib.ridibooks_cms.config import CmsConfig


class AuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            return None

        config = CmsConfig.get_config()
        admin_auth = AdminAuth(config)
        token = request.cookies.get(COOKIE_CMS_TOKEN)

        login_session = LoginSession(config, token)

        if not admin_auth.authorize(login_session=login_session, check_url=request.path):
            login_url = admin_auth.getLoginUrl(request.path)
            return redirect(login_url)

        staff = Staff.objects.get_or_create(admin_id=login_session.getAdminId())
        login(request, staff)
        return None

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, JsonResponse
from django.views import View
from drf_yasg.utils import swagger_auto_schema
from requests import HTTPError
from rest_framework.views import APIView

from apps.domains.oauth2.exceptions import JwtTokenErrorException
from apps.domains.ridi.helpers.response_cookie_helper import ResponseCookieHelper
from apps.domains.ridi.helpers.token_helper import TokenHelper
from apps.domains.ridi.helpers.url_helper import UrlHelper
from apps.domains.ridi.response import InHouseHttpResponseRedirect
from apps.domains.ridi.schemas import TokenGetSchema
from apps.domains.ridi.services.token_refresh_service import TokenRefreshService
from apps.domains.ridi.services.authorization_code_service import AuthorizationCodeService
from apps.domains.oauth2.token import JwtHandler
from apps.domains.ridi.forms import AuthorizeForm, CallbackForm, TokenForm

from infra.network.constants.http_status_code import HttpStatusCodes
from lib.base.invalid_form_response import InvalidFormResponse
from lib.django.http.response import HttpResponseUnauthorized


class AuthorizeView(LoginRequiredMixin, View):
    def get(self, request):
        authorize_form = AuthorizeForm(request.GET)
        if not authorize_form.is_valid():
            return InvalidFormResponse(authorize_form)
        valid_data = authorize_form.clean()
        url = AuthorizationCodeService.get_oauth2_authorize_url(valid_data['client_id'], valid_data['redirect_uri'], request.user.idx)
        return HttpResponseRedirect(url)


class CallbackView(View):
    def get(self, request):
        data = request.GET.copy()
        data['u_idx'] = request.user.idx
        callback_form = CallbackForm(data)
        if not callback_form.is_valid():
            return InvalidFormResponse(callback_form)
        valid_data = callback_form.clean()
        try:
            access_token, refresh_token = AuthorizationCodeService.get_tokens(
                valid_data['code'], valid_data['client_id'], valid_data['in_house_redirect_uri']
            )
            root_domain = UrlHelper.get_root_domain(self.request)
            response = InHouseHttpResponseRedirect(valid_data['in_house_redirect_uri'])
            ResponseCookieHelper.add_token_cookie(
                response=response, access_token=access_token, refresh_token=refresh_token, root_domain=root_domain
            )
            return response

        except HTTPError as e:
            return JsonResponse(data=e.response.json(), status=e.response.status_code)


class CompleteView(View):
    def get(self, request):
        return JsonResponse(data={}, status=HttpStatusCodes.C_200_OK)


class TokenView(APIView):
    @swagger_auto_schema(**TokenGetSchema.to_swagger_schema())
    def post(self, request):
        token_form = TokenForm(TokenHelper.get_token_data_from_cookie(request.COOKIES))
        if not token_form.is_valid():
            return InvalidFormResponse(token_form)
        valid_data = token_form.clean()
        root_domain = UrlHelper.get_root_domain(self.request)
        try:
            access_token = JwtHandler.get_access_token(valid_data['access_token'])
        except JwtTokenErrorException:
            try:
                access_token, refresh_token = TokenRefreshService.get_tokens(valid_data['refresh_token'])
                data = TokenHelper.get_token_data_info(access_token)
                response = JsonResponse(data)
                ResponseCookieHelper.add_token_cookie(
                    response, access_token=access_token, refresh_token=refresh_token, root_domain=root_domain
                )
                return response
            except PermissionDenied:
                response = HttpResponseUnauthorized()
                ResponseCookieHelper.clear_token_cookie(response, root_domain)
                return response
            except HTTPError as e:
                return JsonResponse(data=e.response.json(), status=e.response.status_code)
        else:
            data = TokenHelper.get_token_info(access_token)
            response = JsonResponse(data)

            return response


class LogoutView(View):
    def get(self, request):
        root_domain = UrlHelper.get_root_domain(self.request)
        return_url = request.GET.get('return_url', None)
        if not return_url:
            return_url = f'https://{root_domain}'

        response = HttpResponseRedirect(return_url)
        ResponseCookieHelper.clear_token_cookie(response, root_domain)
        return response

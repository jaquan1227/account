from django.utils.decorators import decorator_from_middleware

from lib.ridibooks.internal_server_auth.middlewares import RidiInternalAuthMiddleware

ridi_internal_auth = decorator_from_middleware(RidiInternalAuthMiddleware)

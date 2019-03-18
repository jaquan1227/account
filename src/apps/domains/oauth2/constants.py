from lib.base.constants import BaseConstant

# pyJWT 라이브러리의 leeway 값은 토큰의 유효기간을 늘려주는 값이다.
JWT_VERIFY_MARGIN = -(60 * 10)  # -10분


class JwtAlg(BaseConstant):
    HS256 = 'HS256'
    RS256 = 'RS256'

    _LIST = [HS256, RS256, ]
    _STRING_MAP = {
        HS256: 'HS256',
        RS256: 'RS256',
    }


class GrantType(BaseConstant):
    AUTHORIZATION_CODE = 'authorization_code'
    PASSWORD = 'password'
    CLIENT_CREDENTIALS = 'client_credentials'
    REFRESH_TOKEN = 'refresh_token'

    _LIST = [AUTHORIZATION_CODE, PASSWORD, CLIENT_CREDENTIALS, REFRESH_TOKEN]


class ResponseType(BaseConstant):
    CODE = 'code'

    _LIST = [CODE]

from lib.base.constants import BaseConstant


class SiteType:
    WWW = 'www'
    TEST = 'test'


class LogLevel:
    CRITICAL = 'CRITICAL'
    ERROR = 'ERROR'
    WARNING = 'WARNING'
    INFO = 'INFO'
    DEBUG = 'DEBUG'
    NOTSET = 'NOTSET'


class SecretKeyName(BaseConstant):
    # static member
    ENVIRONMENT = 'environment'

    SECRET_KEY = 'secret_key'

    CACHE_LOCATION = 'cache_location'

    WRITE_DB_HOST = 'write_db_host'
    WRITE_DB_ACCOUNT = 'write_db_account'
    WRITE_DB_PASSWORD = 'write_db_password'

    READ_DB_HOST = 'read_db_host'
    READ_DB_ACCOUNT = 'read_db_account'
    READ_DB_PASSWORD = 'read_db_password'

    SENTRY_DSN = 'sentry_dsn'

    RIDI_CLIENT_ID = 'ridi_client_id'
    RIDI_CLIENT_SECRET = 'ridi_client_secret'
    RIDI_JWT_SECRET = 'ridi_jwt_secret'

    RIDI_INTERNAL_AUTH_ACCOUNT_TO_STORE = 'ridi_internal_auth_account_to_store'

    STATE_CRYPTO_KEY = 'state_crypto_key'

    SITE_DOMAIN = 'site_domain'
    STORE_URL = 'store_url'
    STORE_API_URL = 'store_api_url'
    RIDIBOOKS_LOGIN_URL = 'ridibooks_login_url'
    ALLOWED_HOSTS = 'allowed_hosts'
    CORS_ORIGIN_REGEX_WHITELIST = 'cors_origin_regex_whitelist'

    COOKIE_ROOT_DOMAIN = 'cookie_root_domain'

    SSO_OTP_KEY = 'sso_otp_key'
    SSO_REDIRECT_ROOT_DOMAIN = 'sso_redirect_root_domain'
    SSO_STORE_LOGIN_URL = 'sso_store_login_url'

    _LIST = [
        ENVIRONMENT, SECRET_KEY, CACHE_LOCATION, WRITE_DB_HOST, WRITE_DB_ACCOUNT, WRITE_DB_PASSWORD, READ_DB_HOST, READ_DB_ACCOUNT,
        READ_DB_PASSWORD, SENTRY_DSN, RIDI_INTERNAL_AUTH_ACCOUNT_TO_STORE, STATE_CRYPTO_KEY, SITE_DOMAIN, STORE_URL,
        RIDIBOOKS_LOGIN_URL, ALLOWED_HOSTS, CORS_ORIGIN_REGEX_WHITELIST, COOKIE_ROOT_DOMAIN, STORE_API_URL
    ]


class FileLockKeyName(BaseConstant):
    SET_USER_MODIFIED_HISTORY_ORDER = 'set_user_modified_history_order'
    CRAWL_STORE_USER = 'crawl_store_user'

    _LIST = [
        SET_USER_MODIFIED_HISTORY_ORDER, CRAWL_STORE_USER
    ]

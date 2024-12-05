"""
Django settings for settings project.

Generated by 'django-admin startproject' using Django 5.0.1.
"""

from pathlib import Path
import os
import certifi
import dotenv
import dj_database_url

# MacOS SSL Certificates
os.environ['SSL_CERT_FILE'] = certifi.where()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

dotenv.read_dotenv(os.path.join(BASE_DIR, ".env"))

ENVIRONMENT = os.environ.get('ENVIRONMENT')

LOAD_ENVS_FROM_FILE = os.environ.get("LOAD_ENVS_FROM_FILE", "False") == "True"


###
# Security Key CHECK FOR PRODUCTION
###
SECRET_KEY = os.environ.get("SECRET_KEY")

###
# Debug  HECK FOR PRODUCTION
###
DEBUG = True


###
# Frontend URL
###
FE_URL = os.environ.get('FE_URL')
FE_IP = os.environ.get('FE_IP')


###
# Allowed Hosts CHECK FOR PRODUCTION
###
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    FE_IP,
]


###
# CorsHeader CHECK FOR PRODUCTIONß
###
CORS_ALLOWED_ORIGINS = [
    FE_URL,
]


###
# Application definition
###
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django.contrib.sites",

    # Apps
    "app.accounts",
    "app.carwash",

    # Helpers
    "helpers.timestamp",

    # CorsHeaders
    "corsheaders",

    # Rest Framework
    "rest_framework",
    "rest_framework.authtoken",

    # Rest Auth
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "allauth",
    "allauth.account",

    # Swagger
    'drf_yasg',
]


###
# Middleware
###
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]


###
# Root URL
###
ROOT_URLCONF = 'settings.urls'


###
# Templates
###
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'app.accounts.context_processors.frontend_url',
            ],
        },
    },
]

WSGI_APPLICATION = 'settings.wsgi.application'


###
# Database
###
DATABASE_URL = os.environ.get('DATABASE_URL')
DATABASES = {'default': dj_database_url.parse(DATABASE_URL)}
DATABASES['default']['ATOMIC_REQUESTS'] = True


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


###
# Static Files
###
STATIC_URL = '/static/'


###
# PK Auto Field
###
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


###
# Rest Auth
###
AUTH_USER_MODEL = "accounts.User"

ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
SITE_ID = 1

REST_AUTH = {
    "REGISTER_SERIALIZER": "app.accounts.api.v1.serializers.accounts.default.CustomRegisterSerializer",
    "USER_DETAILS_SERIALIZER": "app.accounts.api.v1.serializers.accounts.default.CustomUserDetailsSerializer",
    "OLD_PASSWORD_FIELD_ENABLED": True,
    "USE_JWT": True,
    "JWT_AUTH_HTTPONLY": False,
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)


###
# E-mail settings .env file
###
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND')
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
ACCOUNT_EMAIL_SUBJECT_PREFIX = os.environ.get('ACCOUNT_EMAIL_SUBJECT_PREFIX')

###
# Rest Framework
###
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated"
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 25,
}


###
# Celery and Redis Configuration
###
REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = os.environ.get('REDIS_PORT', '6379')
REDIS_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}/1'
CELERY_DEFAULT_QUEUE = os.environ.get('CELERY_DEFAULT_QUEUE', 'scheduler')

BROKER_URL = REDIS_URL
VISIBILITY_TIMEOUT = os.environ.get('VISIBILITY_TIMEOUT', 86400)
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': VISIBILITY_TIMEOUT}
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
ACCEPT_CONTENT = ['json']
TASK_SERIALIZER = 'json'
RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE

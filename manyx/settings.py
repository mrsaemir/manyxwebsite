import os
import json

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# For Keeping security key a secret, it is set as environment variable.
SECRET_KEY = os.environ.get('SECRET_KEY')


# Our Allowed Hosts
ALLOWED_HOSTS = json.loads(os.environ.get('ALLOWED_HOSTS'))


# Maintenance
# Note : setting MAINTENANCE=ON will override DEBUG=True for DEBUG_IPS
MAINTENANCE_ENVVAR = os.environ.get('MAINTENANCE')
# because an envvar is just a string and each string is considered True
# in python we have to determine if the boolean is True or False
if MAINTENANCE_ENVVAR == "True":
    MAINTENANCE = True
else:
    MAINTENANCE = False


# a list of allowed ips to see debug info in maintenance mode
DEBUG_IPS = json.loads(os.environ.get('DEBUG_IPS'))


# Debug Info
# never use DEBUG=True in production mode, instead use MAINTENANCE.
DEBUG_ENVVAR = os.environ.get('DEBUG')
# because an envvar is just a string and each string is considered True
# in python we have to determine if the boolean is True or False
if DEBUG_ENVVAR == "True":
    DEBUG = True
else:
    DEBUG = False


# AUTH USER MODEL
AUTH_USER_MODEL = "manyx.ManyxUser"


# Application definition
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    # handling cors headers for django
    'corsheaders',
    # Jalali datetime model field
    'django_jalali',
    # Jalai datetime views to convert datetime
    'jalali_date',
    'manyx',
    'blog',
    'website',
]

MIDDLEWARE = [
    # does some action if the site is under maintenance.
    'manyx.middleware.MaintenanceMode',
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# cors headers
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = (
    '192.168.43.65',
)
CORS_ORIGIN_REGEX_WHITELIST = (
    '192.168.43.65',
)

ROOT_URLCONF = 'manyx.urls'

# DB configurations
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'manyx.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'fa-IR'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = False

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = os.environ.get('STATIC_URL')
MEDIA_URL = os.environ.get('MEDIA_URL')

STATIC_ROOT = os.environ.get('STATIC_ROOT')
MEDIA_ROOT = os.environ.get('MEDIA_ROOT')


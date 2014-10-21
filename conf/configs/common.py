"""
Common settings shared between environments.
"""

# Import system modules
import os

__author__ = 'Alex Laird'
__copyright__ = 'Copyright 2014, Innovative Software Engineering'
__version__ = '0.0.1'


# Define the base working directory of the application
BASE_DIR = os.path.normpath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../'))


# ############################
# Project configuration
# ############################

# Version information
PROJECT_NAME = 'ClockIt'
PROJECT_VERSION = '0.0.1'


#############################
# Default lists for host-specific configurations
#############################

DEFAULT_INSTALLED_APPS = (
    # Django modules
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    # Project modules
    'clockit',
    'timecard',
)

DEFAULT_MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

DEFAULT_TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'conf.processors.template',
)

#############################
# Django configuration
#############################

# Application definition

SITE_ID = 1
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
AUTH_USER_MODEL = 'clockit.User'
LOGIN_URL = '/login'
LOGOUT_URL = '/logout'
ROOT_URLCONF = 'conf.urls'
WSGI_APPLICATION = 'conf.wsgi.application'

# Internationalization

LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_THOUSAND_SEPARATOR = True
USE_TZ = True
HE_DATE_STRING = "%Y-%m-%d"
HE_TIME_STRING = "%H:%M:%S"
HE_DATE_TIME_STRING = HE_DATE_STRING + " " + HE_TIME_STRING

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

# Email settings

EMAIL_USE_TLS = True
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = "ClockIt <clockit@iseinc.biz>"
EMAIL_HOST = 'smtp.iseinc.biz'
EMAIL_HOST_USER = 'clockit@iseinc.biz'
EMAIL_HOST_PASSWORD = 'clockit_password'

SERVER_EMAIL = 'it@iseinc.biz'
ADMINS = (
    ('Alex Laird', 'alexlaird@iseinc.biz'),
)
MANAGERS = ADMINS
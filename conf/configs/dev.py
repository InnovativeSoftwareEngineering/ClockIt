"""
Settings for development.
"""

# Import system modules
import os

# Import project modules
from conf.configs.common import DEFAULT_TEMPLATE_CONTEXT_PROCESSORS, DEFAULT_MIDDLEWARE_CLASSES, DEFAULT_INSTALLED_APPS

__author__ = 'Alex Laird'
__copyright__ = 'Copyright 2014, Innovative Software Engineering'
__version__ = '0.0.1'


# Define the base working directory of the application
BASE_DIR = os.path.normpath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../'))


# Application definition

INSTALLED_APPS = DEFAULT_INSTALLED_APPS + (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES = DEFAULT_MIDDLEWARE_CLASSES + (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.debug',
)


#############################
# Django configuration
#############################

# Security

SECRET_KEY = 'ui(0mu1=%8pfnnuy0i&8dlf*whlfo4_u6&4mlm)c90aoj1_etn'
CSRF_MIDDLEWARE_SECRET = '7A0+@mDw*5hA=Bzh${L%r;7Hbcut|.7_#)BJcZi{)IGN?Z^1Ya'
ALLOWED_HOSTS = ['localhost']
INTERNAL_IPS = (
    '127.0.0.1',
)

# Logging

DEBUG = True
TEMPLATE_DEBUG = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'clockit_log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'clockit_log'),
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'timecard_log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'timecard_log'),
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'WARN',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
        'clockit': {
            'handlers': ['console', 'clockit_log'],
            'level': 'DEBUG',
        },
        'timecard': {
            'handlers': ['console', 'timecard_log'],
            'level': 'DEBUG',
        },
    }
}

# Email settings

# The dev SMTP server can be started with the following command:
# python -m smtpd -n -c DebuggingServer localhost:1025
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
DEFAULT_FROM_EMAIL = "ClockIt <clockit@iseinc.biz>"

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
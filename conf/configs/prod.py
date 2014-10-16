"""
Settings for production.
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

INSTALLED_APPS = DEFAULT_INSTALLED_APPS

MIDDLEWARE_CLASSES = DEFAULT_MIDDLEWARE_CLASSES

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_TEMPLATE_CONTEXT_PROCESSORS


#############################
# Django configuration
#############################

# Security

ALLOWED_HOSTS = ['www.timecard.iseinc.biz',
                 'timecard.iseinc.biz']

SECRET_KEY = 'ui(0mu1=%8pfnnuy0i&8dlf*whlfo4_u6&4mlm)c90aoj1_etn'
CSRF_MIDDLEWARE_SECRET = '7A0+@mDw*5hA=Bzh${L%r;7Hbcut|.7_#)BJcZi{)IGN?Z^1Ya'
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Logging

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
        'django_log': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'django_log'),
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'clockit_log': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'clockit_log'),
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'timecard_log': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'timecard_log'),
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'email_backend': 'django.core.mail.backends.smtp.EmailBackend',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['django_log', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'clockit': {
            'handlers': ['clockit_log', 'mail_admins'],
            'level': 'INFO',
        },
        'timecard': {
            'handlers': ['timecard_log', 'mail_admins'],
            'level': 'INFO',
        },
    }
}

# Database

DATABASES = {
    'default': {
        'NAME': 'clockit',
        'ENGINE': 'sqlserver_ado',
        'HOST': 'timecard.iseinc.biz\\clockit',
        'USER': 'clockit',
        'PASSWORD': 'clockit_password',
    }
}
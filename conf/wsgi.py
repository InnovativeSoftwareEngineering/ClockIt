"""
WSGI configuration.
"""

import os

__author__ = 'Alex Laird'
__copyright__ = 'Copyright 2014, Innovative Software Engineering'
__version__ = '0.0.1'

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

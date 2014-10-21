"""
Helper template tag functions.
"""

# Import Django modules
from django import template

__author__ = 'Alex Laird'
__copyright__ = 'Copyright 2014, Innovative Software Engineering'
__version__ = '0.0.1'

register = template.Library()


@register.simple_tag
def active(request, pattern):
    if request.path.startswith(pattern):
        return 'active'
    return ''
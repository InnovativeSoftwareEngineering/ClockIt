"""
The model for an Activity.

An Activity can be used to further refine what a user was doing when charging to a Project/Deliverable. Activities are
generic and used system-wide, so they can be accessed by any user, should be broad in scope, and do not require any
special permissions to appear.
"""

# Import system modules
import logging

# Import Django modules
from django.db import models

__author__ = 'Alex Laird'
__copyright__ = 'Copyright 2014, Innovative Software Engineering'
__version__ = '0.0.1'

logger = logging.getLogger(__name__)


class Activity(models.Model):
    """
    The model for an Activity.
    """
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
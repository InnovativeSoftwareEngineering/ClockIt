"""
The model for a Project.

A user is given permissions to charge to a particular project and a Deliverable within that
Project. A Project requires at least one Deliverable to be able to be charged to.
"""

# Import system modules
import logging

# Import Django modules
from django.db import models

__author__ = 'Alex Laird'
__copyright__ = 'Copyright 2014, Innovative Software Engineering'
__version__ = '0.0.1'

logger = logging.getLogger(__name__)


class Project(models.Model):
    """
    The model for a Project.
    """
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)

    # A Project can only be charged to if the user is in this relationship
    allowed_users = models.ManyToManyField('User')
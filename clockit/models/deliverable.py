"""
The model for a Deliverable.

A Deliverable is a sub-component of a Project. A Project must have at least one Deliverable to function properly.
Deliverables will show up in the list of items a user can charge to if the user has permission to charge to a Project,
and the Deliverable will show up as follows:

Project 1 - Deliverable 1
Project 1 - Deliverable 2
Project 2 - Deliverable 1
"""

# Import system modules
import logging

# Import Django modules
from django.db import models

__author__ = 'Alex Laird'
__copyright__ = 'Copyright 2014, Innovative Software Engineering'
__version__ = '0.0.1'

logger = logging.getLogger(__name__)


class Deliverable(models.Model):
    """
    The model for a Deliverable.
    """
    group_name = models.CharField(max_length=255)
    group_description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)

    # Foreign keys
    project = models.ForeignKey('Project')

    # A Deliverable can only be charged to if the user is in this relationship
    allowed_users = models.ManyToManyField('User')
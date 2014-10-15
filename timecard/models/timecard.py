"""
The model for a Task.
"""

# Import system modules
import logging

# Import Django modules
from django.db import models

__author__ = 'Alex Laird'
__copyright__ = 'Copyright 2014, Innovative Software Engineering'
__version__ = '0.0.1'

logger = logging.getLogger(__name__)


class TimeCard(models.Model):
    """
    The model for a Task.
    """
    begin = models.DateTimeField()
    end = models.DateTimeField()
    record_status = models.PositiveIntegerField()
    description = models.CharField(max_length=300, null=True, blank=True)

    # Foreign keys
    user = models.ForeignKey('User')
    project = models.ForeignKey('Project')
    deliverable = models.ForeignKey('Deliverable', null=True, blank=True)
    activity = models.ForeignKey('Activity', null=True, blank=True)
    task = models.ForeignKey('Task', null=True, blank=True)
    approved_by = models.ForeignKey('User', related_name='approved_by_user', null=True, blank=True)
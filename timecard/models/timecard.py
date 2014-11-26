"""
The model for a TimeCard.

A TimeCard is the aggregate of all Tasks a user has charged to within a window of time. Depending on the submission
window, a TimeCard must be submitted at the end of the window, then a new TimeCard will be created.
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
    The model for a TimeCard.
    """
    start = models.DateTimeField()
    end = models.DateTimeField()
    submitted = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)

    # Foreign keys
    user = models.ForeignKey('clockit.User')
    approved_by = models.ForeignKey('clockit.User', related_name='approved_by_user', null=True, blank=True)
"""
The model for a Task.

Tasks make up the contents of a TimeCard. A Task is an individual chargeable portion of time to a particular
Project/Deliverable, and Tasks are ultimately what is submitted for evaluation with the TimeCard.
"""

# Import system modules
import logging

# Import Django modules
from django.db import models

__author__ = 'Alex Laird'
__copyright__ = 'Copyright 2014, Innovative Software Engineering'
__version__ = '0.0.1'

logger = logging.getLogger(__name__)


class Task(models.Model):
    """
    The model for a Task.
    """
    begin = models.DateTimeField()
    end = models.DateTimeField()
    description = models.TextField(null=True, blank=True)

    # Foreign keys
    project = models.ForeignKey('clockit.Project')
    deliverable = models.ForeignKey('clockit.Deliverable')
    activity = models.ForeignKey('clockit.Activity')
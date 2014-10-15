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


class Project(models.Model):
    """
    The model for a Task.
    """
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    default = models.BooleanField(default=False)

    # Foreign keys
    customer = models.ForeignKey('Customer')
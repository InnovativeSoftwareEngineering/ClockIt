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


class Customer(models.Model):
    """
    The model for a Task.
    """
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    address1 = models.CharField(max_length=50, null=True, blank=True)
    address2 = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    fax = models.CharField(max_length=12, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    contact1 = models.CharField(max_length=50, null=True, blank=True)
    contact2 = models.CharField(max_length=50, null=True, blank=True)
    account_code = models.CharField(max_length=20, null=True, blank=True)
    active = models.BooleanField(default=True)
"""
View entrance functions.
"""

# Import system modules
import logging

# Import Django modules
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

__author__ = 'Alex Laird'
__copyright__ = 'Copyright 2014, Innovative Software Engineering'
__version__ = '0.0.1'

logger = logging.getLogger(__name__)


@login_required
def timecard(request):    
    return render(request, "timecard.html")
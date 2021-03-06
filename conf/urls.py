"""
Base URLs.
"""

# Import Django modules
from django.conf.urls import include, url

# Import project modules
from clockit.admin import clockit_admin_site
from clockit.views import *
from timecard.views import *

__author__ = 'Alex Laird'
__copyright__ = 'Copyright 2014, Innovative Software Engineering'
__version__ = '0.0.1'

urlpatterns = [
    # Admin URLs
    url(r'^admin/', include(clockit_admin_site.urls), name='admin'),

    # Base URL
    url(r'^$', home, name='home'),
    
    # Authentication URLs
    url(r'^login$', login, name='login'),
    url(r'^logout', logout, name='logout'),
    url(r'^forgot$', forgot, name='forgot'),
    
    # Authenticated URLs
    url(r'^timecard$', timecard, name='timecard'),
    url(r'^settings$', settings, name='settings'),

    # API URLs
    url(r'^events_feed$', events_feed, name='events_feed'),
    url(r'^event/(\d+)$', event, name='event'),
    url(r'^event/add$', add_event, name='add_event'),
    url(r'^event/edit/(\d+)$', edit_event, name='edit_event'),
    url(r'^event/delete/(\d+)$', delete_event, name='delete_event'),
]

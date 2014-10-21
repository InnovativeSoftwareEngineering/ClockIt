"""
Define the Admin site.
"""

# Import Django modules
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.admin import UserAdmin
from django.conf import settings

# Import project modules
from clockit.models import *
from timecard.models import *
from forms import UserChangeForm, UserCreationForm

__author__ = 'Alex Laird'
__copyright__ = 'Copyright 2014, Innovative Software Engineering'
__version__ = '0.0.1'


class TimecardUserAdmin(UserAdmin):
    """
    Definition for a Timecard user in the Admin area.
    """
    # The forms to add and change user details
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the table of users
    list_display = ('username', 'email', 'is_admin')
    # Items that are filterable on the admin page
    list_filter = ('is_admin',)
    # Fieldsets displayed in the admin, order matters
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'last_login')}),
        ('Permissions', {'fields': ('is_admin', 'is_active', 'security_level')}),
        ('Personal Info', {'fields': (
            'first_name',
            'last_name',
            'hire_date',
            'ssn'
        )}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'security_level')}
        ),
    )
    # Fields on which the admin can search
    search_fields = ('username', 'email',)
    # Ordering of fields
    ordering = ('username', 'email',)
    filter_horizontal = ()


class ClockItAdminSite(AdminSite):
    """
    Definition for the Admin site for the project.
    """
    site_header = settings.PROJECT_NAME + ' Administration'
    site_title = site_header
    index_title = settings.PROJECT_NAME
    login_template = 'login.html'

# Instantiate the Admin site
clockit_admin_site = ClockItAdminSite()

# Register the models in the Admin
clockit_admin_site.register(Activity)
clockit_admin_site.register(Deliverable)
clockit_admin_site.register(Project)
clockit_admin_site.register(Task)
clockit_admin_site.register(TimeCard)
clockit_admin_site.register(User, TimecardUserAdmin)
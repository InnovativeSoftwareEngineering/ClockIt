"""
Form for user modification.
"""

# Import Django modules
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

# Import project modules
from clockit.models import User

__author__ = 'Alex Laird'
__copyright__ = 'Copyright 2014, Innovative Software Engineering'
__version__ = '0.0.1'


class UserChangeForm(forms.ModelForm):
    """
    Form for user modification.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        """
        Define metadata for this model.
        """

        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'security_level', 'password', 'is_active', 'is_admin')

    def clean_password(self):
        """
        Regardless of what the user provides, return the initial value. This is done here, rather than on the field,
        because the field does not have access to the initial value.
        """
        return self.initial["password"]
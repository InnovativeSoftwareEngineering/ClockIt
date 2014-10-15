"""
The User Manager for a User.
"""

# Import system modules
import logging

# Import Django modules
from django.contrib.auth.models import BaseUserManager

__author__ = 'Alex Laird'
__copyright__ = 'Copyright 2014, Innovative Software Engineering'
__version__ = '0.0.1'

logger = logging.getLogger(__name__)


class UserManager(BaseUserManager):
    """
    The Manager for a User.
    """
    
    # Security levels
    USER = 0
    MANAGER = 1
    TIMECARD_ADMIN = 2
    SYSTEM_ADMIN = 3
    SECURITY_LEVELS = (
        (USER, 'User'),
        (MANAGER, 'Manager'),
        (TIMECARD_ADMIN, 'Timecard Admin'),
        (SYSTEM_ADMIN, 'System Admin')
    )

    def create_user(self, username, email, first_name, last_name, security_level, password=None):
        """
        Create a new user with the given username, password, and email.

        :param username: the username for the new user
        :param email: the email for the new user
        :param first_name: the first name for the user
        :param last_name: the last name for the user
        :param security_level: the security level for the user
        :param password: the password for the new user
        :return: the created object
        """
        if not username:
            raise ValueError('Users must have a username')
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            security_level=security_level,
        )

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, first_name, last_name, security_level, password):
        """
        Create a new super user with admin privileges.

        :param username: the username for the new user
        :param email: the email for the new user
        :param first_name: the first name for the user
        :param last_name: the last name for the user
        :param security_level: the security level for the user
        :param password: the password for the new user
        :return: the created object
        """
        user = self.create_user(username=username,
                                email=email,
                                first_name=first_name,
                                last_name=last_name,
                                security_level=security_level,
                                password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

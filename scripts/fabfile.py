#!/usr/bin/env python

"""
Fabric deployment script for ClockIt.
"""

# Import system modules
import datetime
import getpass
import os
import socket
import sys

# Import third-party modules
from fabric.context_managers import cd, prefix
from fabric.contrib import django
from fabric.contrib.console import confirm
from fabric.contrib.files import exists
from fabric.operations import prompt, local, sudo, run
from fabric.state import env
from fabric.utils import abort, warn
from fabric.network import ssh

__author__ = 'Alex Laird'
__copyright__ = 'Copyright 2014, Innovative Software Engineering'
__version__ = '0.0.1'

ssh.util.log_to_file("paramiko.log", 10)

HOST_REPO_URL = 'git@github.com:InnovativeSoftwareEngineering/ClockIt.git'
DEV_SERVER = 'clockit.iseinc.biz'
DEV_SERVER_PATH = '/opt/clockit'


def dev():
    """
    Deploy a tag or "master" to the dev server.
    """
    env.host_string = DEV_SERVER
    env.user = raw_input('Enter the username on %s: ' % env.host_string)
    env.password = getpass.getpass('Enter the password on %s for the user "%s": ' % (env.host_string, env.user))
    
    tag = prompt(
        'Enter a tag "origin" you wish to deploy (ex. 1.0.3), or enter "master" to stage the latest unstable code to the dev server:')
    if tag != 'master':
        is_tag_valid = local('git tag -l %s' % tag, capture=True)
        if is_tag_valid == '':
            abort('You must enter a tag to release.')
    path = DEV_SERVER_PATH

    sys.path.insert(0, os.path.abspath(os.path.join('.', '..')))
    django.settings_module('conf.settings')

    if confirm(
                    'You are about to release ClockIt v%s to the dev server, which will erase all previous ClockIt versions in staging folders. Are you sure you want to continue?' % tag,
                    default=False):

        # Ensure the environment on the server is ready for us
        if not exists(path):
            with os.path.join(path, '..'):
                name = path[path.rfind('/') + 1:]
                sudo('pip install virtualenv')
                sudo('virtualenv ' + name)
                sudo('chown -R ' + env.user + ':' + env.user + ' ' + name)
        
        # Remove and replace everything currently in the staging area
        with cd(path):
            # Backup old logs first
            today = datetime.datetime.now().strftime('%m-%d-%Y_%H_%M')
            run('mkdir archived_logs', warn_only=True)
            run('mkdir archived_logs/' + today, warn_only=True)
            run('cp -R clockit/logs/* archived_logs/' + today + '/', warn_only=True)

            run('rm -rf staging', warn_only=True)

            # Clone the Git repository
            run('git clone %s staging' % (HOST_REPO_URL))

        if tag != 'master':
            # Checkout the given tag, then do away with the Git configuration
            with cd(path + '/staging'):
                run('git checkout tags/%s' % tag)
        else:
            # Ensure we're at the latest revision on the "master" branch for our current version branch
            with cd(path + '/staging'):
                run('git checkout master')

        with cd(path + '/staging'):
            with prefix('source ' + path + '/bin/activate'):
                # Run the requirements file to ensure all dependencies are met
                run('pip install -r scripts/reqs.txt')

                # Collect static files
                run('python manage.py collectstatic --noinput')

                # Execute test cases (since this is a dev environment, failure is tolerated)
                if run('python manage.py test', warn_only=True).failed:
                    warn('Tests failed, but since this is a dev deployment we\'ll let it slide.')
                
                # Stop the services that will be modified with migrations to prevent issues
                sudo('service apache2 stop')

                # Execute migrations
                run('python manage.py migrate')

        # If we're deploying a tag, generate documentation for this versioned release
        if tag != 'master':
            with cd(path + '/staging/docs'):
                with prefix('source ' + path + '/bin/activate'):
                    from django.conf import settings

                    # Generate documentation and put it into place
                    run('make html')

                    version_path = '../../docs/%s' % tag

                    # Move generated documentation into place
                    run('mkdir ../../docs', warn_only=True)
                    run('rm -rf %s' % version_path)
                    run('mkdir %s' % version_path)
                    run('mv build/html/* %s' % version_path)
                    sudo('chown -R ' + env.user + ':' + WEB_SERVER_USERNAME + ' ../../docs')

        # Move folders into place and update permissions
        with cd(path):
            run('rm -rf last_release', warn_only=True)
            run('mv %s %s' % ('clockit', 'last_release'), warn_only=True)
            run('mv %s %s' % ('staging', 'clockit'))

            sudo('chown -R ' + env.user + ':' + WEB_SERVER_USERNAME + ' clockit')

        # Restart necessary services
        sudo('service apache2 start')


if __name__ == '__main__':
    print 'Oops, this file is not executable, it\'s meant to be used by Fabric. To execute its functionality, use the "fab" command.'
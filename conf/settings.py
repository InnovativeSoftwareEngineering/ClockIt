"""
Django settings for project.
"""

# Import system modules
import socket
import sys

__author__ = 'Alex Laird'
__copyright__ = 'Copyright 2014, Innovative Software Engineering'
__version__ = '0.0.1'

common_conf_module = __import__('conf.common', globals(), locals(), 'clockit')

# Load common conf properties into the local scope
for setting in dir(common_conf_module):
    if setting == setting.upper():
        locals()[setting] = getattr(common_conf_module, setting)

if 'test' not in sys.argv:
    # Available environments for conf files are keyed by hostname
    confs = {
        'timecard.iseinc.biz': 'prod',
    }

    # If the hostname is not in the list of confs, use 'dev' conf
    hostname = socket.gethostname()
    conf_module = __import__('conf.%s' % (confs[hostname] if hostname in confs.keys() else 'dev'),
                             globals(),
                             locals(), 'clockit')

    # Load the conf properties into the local scope
    for setting in dir(conf_module):
        if setting == setting.upper():
            locals()[setting] = getattr(conf_module, setting)
# If we're running tests, run a streamlined settings file for efficiency
else:
    test_conf_module = __import__('conf.test', globals(), locals(), 'clockit')

    # Load test conf properties into the local scope
    for setting in dir(test_conf_module):
        if setting == setting.upper():
            locals()[setting] = getattr(test_conf_module, setting)
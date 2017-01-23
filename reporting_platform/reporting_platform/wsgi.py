"""
WSGI config for reporting_platform project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys

path = '/home/janejl/reporting_platform'  # use your own PythonAnywhere username here
if path not in sys.path:
    sys.path.append(path)

# os.environ['DJANGO_SETTINGS_MODULE'] = 'reporting_platform.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "reporting_platform.settings")

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())
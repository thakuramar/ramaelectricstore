"""
WSGI config for ramaelectricstore project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
import sys

sys.path.insert(0, '/opt/python/current/app')


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ramaelectricstore.settings')

application = get_wsgi_application()

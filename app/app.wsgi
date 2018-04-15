import os
import sys

APP_PATH = os.path.dirname(os.path.abspath(__file__))
AUX_LIBS_PATH = os.path.join(APP_PATH, 'libs')
sys.path.extend([APP_PATH, AUX_LIBS_PATH])

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

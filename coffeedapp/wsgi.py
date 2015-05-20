"""
WSGI config for coffeedapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# added for heroku
from dj_static import Cling

application = Cling(get_wsgi_application())
# end heroku addition

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coffeedapp.settings")

# application = get_wsgi_application()

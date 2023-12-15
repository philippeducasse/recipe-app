"""
Thisi s for local development, mnot production.
WSGI config for recipe_project project.
web server gateway interface
It exposes the WSGI callable as a module-level variable named ``application``.

The Procfile declares the process type and entry popnt of the application

web: gunicorn recipe_project.wsgi --log-file - (from the Procfile) tells heroku
that tihs is a web dyno and can be sent http traffic (dynos are lightwieght Linux containers
to run Heroku apps.)

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipe_project.settings.prod')

application = get_wsgi_application()

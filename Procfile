web: gunicorn bookstore.wsgi --log-file -
web: python manage.py migrate --settings=recipe_project.settings.prod && gunicorn --env DJANGO_SETTINGS_MODULE=recipe_project.settings.prod
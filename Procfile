release: python manage.py migrate --settings=recipe_project.settings.prod
web: gunicorn recipe_project.wsgi --log-file -

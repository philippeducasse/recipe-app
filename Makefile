dev-start:
	python manage.py runserver --settings=recipe_project.settings.dev

prod-start:
	python manage.py runserver --settings=recipe_project.settings.prod

dev-makemigrations:
	python manage.py makemigrations --settings=recipe_project.settings.dev

dev-migrate:
	python manage.py migrate --settings=recipe_project.settings.dev

prod-migrate:
	heroku run python manage.py migrate --settings=recipe_project.settings.prod

# This file specifies the URL that will be used to call the landing page view

from django.urls import path
from .views import home

# required for path to work, corresponds to "path('', include('recipes.urls'))" in recipe_project/urls.py
app_name = 'recipes'

urlpatterns = [
    path('', home)
]
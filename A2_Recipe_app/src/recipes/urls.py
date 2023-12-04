# This file specifies the URL that will be used to call the landing page view

from django.urls import path
from .views import home, RecipeListView, RecipeDetailView, create

# required for path to work, corresponds to "path('', include('recipes.urls'))" in recipe_project/urls.py
app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'), #name acts as ID for the path
    path('list/', RecipeListView.as_view(), name='list'),
    path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
    path('create/', create, name='create'),
]
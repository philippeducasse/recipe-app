# This file specifies the URL that will be used to call the landing page view

from django.urls import path
from .views import home, RecipeListView, RecipeDetailView, create, search, delete_recipe, udpate_recipe, update_success, create_success, delete_success
from django.conf import settings
from django.conf.urls.static import static


# required for path to work, corresponds to "path('', include('recipes.urls'))" in recipe_project/urls.py
app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'), #name acts as ID for the path
    path('list/', RecipeListView.as_view(), name='list'),
    path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
    path('create/', create, name='create'),
    path('create_success/', create_success, name='create_success'),
    path('search/', search, name = 'search'),
    path('delete/<pk>', delete_recipe, name = 'delete'),
    path('delete/', delete_success, name = "delete_success"),
    path('update/<pk>', udpate_recipe, name= 'update'),
    path('update_success/', update_success, name= 'update_success'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
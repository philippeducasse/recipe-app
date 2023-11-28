from django.shortcuts import render
from django.views.generic import ListView, DetailView   #to display lists & details
from .models import Recipe                #to access Book model
# Create your views here.

def home(request):
    # Enter the url request
    return render(request, 'recipes/home.html')

class RecipeListView(ListView):           #class-based view
   model = Recipe                         #specify model
   template_name = 'recipes/list.html'    #specify template 

class RecipeDetailView(DetailView):

    model = Recipe
    template_name = 'recipes/detail.html'
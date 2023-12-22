from typing import Any
from django.db import models
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView   #to display lists & details
from .models import Recipe                #to access recipe model
from django.contrib.auth.decorators import login_required
from .forms import RecipeSearchForm, CreateRecipeForm
import pandas as pd
from .utils import get_recipename_from_id, get_chart
import random

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


class RecipeDeleteView(DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipes/list.html')
    template_name = 'recipes/delete.html'
        

#keep protected
@login_required # redirects to login view if user is not loggedin, (from settings.py)
def create(request):
    if request.method == 'POST':
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data if it's valid
            # Redirect or perform any other action after successful form submission
            return redirect('/create_success')  # Redirect to the same page after form submission
    else:
        form = CreateRecipeForm()

    context = {'form': form}
    return render(request, 'recipes/create.html', context)
def create_success(request):
    return render(request, 'recipes/create_success.html')

#Update Recipe
@login_required
def udpate_recipe(request, pk):
    recipe = Recipe.objects.get(id = pk)
    if request.method == 'POST':
        # instance sends all info of recipe in the fields
        form = CreateRecipeForm(request.POST, instance = recipe)
        if form.is_valid():
                form.save()  # Save the form data if it's valid
                # Redirect or perform any other action after successful form submission
                return redirect('/update_success')  # Redirect to list page after form submission
    else:
        form = CreateRecipeForm(instance=recipe)
    context = {
        'form': form,
               }
    return render(request, 'recipes/update.html', context)
    # form = UpdateRecipeForm(request.POST or None)

def update_success(request):
    return render(request, 'recipes/update_success.html')

# Delete Recipe
@login_required
def delete_recipe(request, pk):
    recipe = Recipe.objects.get(id = pk)
    recipe.delete()
    return redirect('/delete')

def delete_success(request):
    return render(request, 'recipes/delete.html')

def search(request):
    form = RecipeSearchForm(request.POST or None)
    recipe_data =  {}#initialize dataframe to None
    charts = set()
    recipes = []

    if request.method == 'POST':
        #read the recipe_name and chart_type
        search_type = request.POST.get('search_type')
        # apply filter to extract data
        if search_type == '#1':
            recipe_name = request.POST.get('search_value')
            #icontains is the Django lookup fucntions
            qs = Recipe.objects.filter(name__icontains = recipe_name)
            recipes = qs
            if qs: #if data found
                    #convert the ID to Name of recipe
                    #get ingredients_lis
                for recipe in qs:
                    recipe_data = list(qs.values())  # Convert queryset values to a list of dictionaries
                    labels = recipe.formatted_ingredients.split(', ')
                    title = recipe.name 
                    # create a random number for each ingredient to display in the pie chart
                    ingredients_val = [] 
                    for ingredient in labels:
                            ingredients_val.append(random.randint(1,20))

                    chart = get_chart(search_type, ingredients_val, labels=labels, title= title)
                    charts.add(chart)

                recipe_df = pd.DataFrame(recipe_data)  # Create DataFrame from the list of dictionaries
                    # convert the queryset values to pandas dataframe
                    # Convert DataFrame to list of dictionaries
            else:
                print('No recipes found.')

        if search_type == '#2':
            target_ingredient = request.POST.get('search_value')
            recipes = Recipe.objects.all()
            # Have to access it this way because the Django lookip __icontains 
            # cannot access getter methods necessary for the _formatted ingredients
            qs = [
                recipe for recipe in recipes if target_ingredient.lower() in recipe.formatted_ingredients.lower() 
            ]
            recipes = qs
            if qs:
                for recipe in qs:
                    recipe_data = [obj.__dict__ for obj in qs]
                    recipe_names = []
                    cooking_times = []
                    for data in recipe_data:
                        recipe_instance = Recipe.objects.get(pk=data['id'])  # Fetch the Recipe instance
                        data['formatted_ingredients'] = recipe_instance.formatted_ingredients  # Calculate formatted ingredients
                        data['difficulty'] = recipe_instance.difficulty  
                        data['url'] = recipe_instance.get_absolute_url()# Call get_absolute_url() on the instance
                        recipe_names.append(recipe_instance.name)
                        cooking_times.append(recipe_instance.cooking_time)
                        
                        
                chart = get_chart(search_type, recipe_names, cooking_times= cooking_times)
                charts.add(chart)

                recipe_df = pd.DataFrame(recipe_data)  # Create DataFrame from the list of dictionaries
                    # convert the queryset values to pandas dataframe
                    # Convert DataFrame to list of dictionaries
                recipe_data = recipe_df.to_dict('records')



    context = {
        'form' : form,
        'recipe_data': recipe_data,
        'charts': list(charts),
        'recipes': recipes,
        }

    return render(request, 'recipes/search.html', context)

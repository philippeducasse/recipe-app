from django.shortcuts import render
from django.views.generic import ListView, DetailView   #to display lists & details
from .models import Recipe                #to access recipe model
from django.contrib.auth.decorators import login_required
from .forms import RecipeSearchForm
import pandas as pd
from .utils import get_recipename_from_id, get_chart

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

#keep protected
@login_required # redirects to login view if user is not loggedin, (from settings.py)
def create(request):
    return render(request, 'recipes/create.html')

def search(request):
    form = RecipeSearchForm(request.POST or None)
    recipe_data =  {}#initialize dataframe to None
    charts = set()

    if request.method == 'POST':
        #read the recipe_name and chart_type
        search_type = request.POST.get('search_type')
        # apply filter to extract data
        if search_type == '#1':
            recipe_name = request.POST.get('search_value')
            #icontains is the Django lookup fucntions
            qs = Recipe.objects.filter(name__icontains = recipe_name)
            if qs: #if data found
                    #convert the ID to Name of recipe
                    #get ingredients_lis
                for recipe in qs:
                    recipe_data = list(qs.values())  # Convert queryset values to a list of dictionaries
                    for data in recipe_data:
                        recipe_instance = Recipe.objects.get(pk=data['id'])  # Fetch the Recipe instance
                        data['formatted_ingredients'] = recipe_instance.formatted_ingredients  # Calculate formatted ingredients
                        data['difficulty'] = recipe_instance.difficulty  
                        data['url'] = recipe_instance.get_absolute_url()# Call get_absolute_url() on the instance
                        title = data['name'] 
                        labels= recipe_instance.formatted_ingredients.split(', ')
                        ingredients_val = []
                        # here we just want to get an array of numbers for each ingredient. 
                        # Since the labels is in the right format im using that
                        for ingredient in labels:
                            ingredients_val.append(1)
                        chart = get_chart(search_type, ingredients_val, labels=labels, title= title)
                        charts.add(chart)

                    recipe_df = pd.DataFrame(recipe_data)  # Create DataFrame from the list of dictionaries
                    # convert the queryset values to pandas dataframe
                    # Convert DataFrame to list of dictionaries
                    recipe_data = recipe_df.to_dict('records')
                    print(recipe_data)
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
            print(qs)
            if qs:
                for recipe in qs:
                    recipe_data = [obj.__dict__ for obj in qs]
                    for data in recipe_data:
                        recipe_instance = Recipe.objects.get(pk=data['id'])  # Fetch the Recipe instance
                        data['formatted_ingredients'] = recipe_instance.formatted_ingredients  # Calculate formatted ingredients
                        data['difficulty'] = recipe_instance.difficulty  
                        data['url'] = recipe_instance.get_absolute_url()# Call get_absolute_url() on the instance
                        title = data['name'] 
                        labels= recipe_instance.formatted_ingredients.split(', ')
                        alignment = []
                        
                        ingredients_val = []
                        # here we just want to get an array of numbers for each ingredient. 
                        # Since the labels is in the right format im using that
                        for ingredient in labels:
                            ingredients_val.append(1)
                        chart = get_chart(search_type, ingredients_val, labels=labels, title= title)
                        charts.add(chart)

                    recipe_df = pd.DataFrame(recipe_data)  # Create DataFrame from the list of dictionaries
                    # convert the queryset values to pandas dataframe
                    # Convert DataFrame to list of dictionaries
                    recipe_data = recipe_df.to_dict('records')
                    print(recipe_data)



    context = {
        'form' : form,
        'recipe_data': recipe_data,
        'charts': list(charts),
        }

    return render(request, 'recipes/search.html', context)

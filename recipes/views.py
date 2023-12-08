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
    recipe_df = None #initialize dataframe to None
    recipe_url = None #initialize url to None
    charts = set()

    if request.method == 'POST':
        #read the recipe_name and chart_type
        search_type = request.POST.get('search_type')
        # apply filter to extract data
        if search_type == '#1':
            recipe_name = request.POST.get('search_value')
            #icontains is the Django lookup fucntions
            qs = Recipe.objects.filter(name__icontains = recipe_name)
            print('qs: ',qs)
            if qs: #if data found
                    #convert the ID to Name of recipe
                    #get ingredients_lis
                for recipe in qs:
                    recipe_data = list(qs.values())  # Convert queryset values to a list of dictionaries
                    for data in recipe_data:
                        recipe_instance = Recipe.objects.get(pk=data['id'])  # Fetch the Recipe instance
                        data['_formatted_ingredients'] = recipe_instance.formatted_ingredients  # Calculate formatted ingredients
                        data['_difficulty'] = recipe_instance.difficulty  
                        title = data['name'] 
                        labels= recipe_instance.formatted_ingredients.split(', ')
                        ingredients_val = []
                        # here we just want to get an array of numbers for each ingredient. 
                        # Since the labels is in the right format im using that
                        for ingredient in labels:
                            ingredients_val.append(1)
                        chart = get_chart(search_type, ingredients_val, labels=labels, title= title)
                        charts.add(chart)

                        # You might need to do something similar for 'difficulty' if it's a calculated property
                    recipe_url = recipe_instance.get_absolute_url()  # Call get_absolute_url() on the instance

                    recipe_df = pd.DataFrame(recipe_data)  # Create DataFrame from the list of dictionaries
                    print(recipe_df)
                    # convert the queryset values to pandas dataframe
                    recipe_df['id']=recipe_df['id'].apply(get_recipename_from_id)
                    print(labels)
                    print(title)
                    #convert the dataframe to HTML
                    
                    recipe_df=recipe_df.to_html()
            else:
                print('No recipes found.')
        elif search_type == '#2':
            ingredients = request.POST.get('search_value')
            qs = Recipe.objects.filter(ingredients = ingredients)
            print(qs)
            recipe_df = pd.DataFrame(qs.values())
            print(recipe_df)
            recipe_ingredients = len(recipe_df['ingredients'])
            print(recipe_ingredients)
            #call get_chart by passing chart_type from user input, sales dataframe and labels
            chart=get_chart(recipe_df, labels=ingredients)
            recipe_df=recipe_df.to_html()
           #pack up data to be sent to template in the context dictionary
        elif search_type == '#3':
            qs = Recipe.objects.all()
            print(qs)
            recipe_df = pd.DataFrame(qs.values())
            chart = get_chart(search_type, recipe_df)
        else:
            print('No recipes found.')
    context = {
        'form' : form,
        'recipe_df': recipe_df,
        'recipe_url': recipe_url,
        'charts': list(charts),
        }
    
    for i, chart1 in enumerate(charts):
        for j, chart2 in enumerate(charts):
            if i != j and chart1 == chart2:
                print(f"Chart at index {i} is equal to chart at index {j}")

    return render(request, 'recipes/search.html', context)

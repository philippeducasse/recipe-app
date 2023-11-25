from django.shortcuts import render

# Create your views here.

def home(request):
    # Enter the url request
    return render(request, 'recipes/recipes_home.html') 
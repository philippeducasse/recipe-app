from typing import Any
from django import forms #import django forms
from django.forms import ModelForm
from .models import Recipe, Ingredient


SEARCH__CHOICES = (          #specify choices as a tuple
   ('#1', 'Recipe Name'),    
   ('#2', 'Ingredient'),
#    ('#3', 'Cooking time')
   )

#define class-based Form imported from Django forms
class RecipeSearchForm(forms.Form):
    search_value = forms.CharField(max_length=120)
    search_type = forms.ChoiceField(choices = SEARCH__CHOICES)
   
## create recipe form
class CreateRecipeForm(ModelForm):
   ingredients_input = forms.CharField(label='Ingredients', max_length=120)
   class Meta:
        model = Recipe
        fields = ['name', 'cooking_time', 'image', 'user_id']
        # Exclude 'ingredients' as it will be handled separately
        exclude = ['ingredients']
        # change the default input of ingredients from multiple choice to charfield

    # Set placeholder values as help text
   def __init__(self, *args, **kwargs):
        super(CreateRecipeForm, self).__init__(*args, **kwargs)
        self.fields['ingredients_input'].widget.attrs['placeholder'] = 'separated by commas'
        self.fields['cooking_time'].widget.attrs['placeholder'] = 'in minutes'
        self.fields['image'].widget.attrs['placeholder'] = 'enter image url'



   def save(self, commit = True):
      # Save the Recipe instance without committing to the database yet
        instance = super().save(commit=False)

        # Process and handle ingredients manually
        ingredients_input = self.cleaned_data.get('ingredients_input')
        print(ingredients_input)
        ingredients_list = [ingredient.strip() for ingredient in ingredients_input.split(',')]
        print(ingredients_list)
        
        # Process the ingredients_list and relate them to the Recipe instance
        # For example:
        
        if commit:
            instance.save()
            # Save the relationship between Recipe and ingredients
            for ingredient in ingredients_list:
                # Check if the ingredient already exists in the database
               ingredient_obj, created = Ingredient.objects.get_or_create(name=ingredient)
               instance.ingredients.add(ingredient_obj)

        return instance
   
# class UpdateRecipeForm(CreateRecipeForm):
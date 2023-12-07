from django import forms #import django forms

SEARCH__CHOICES = (          #specify choices as a tuple
   ('#1', 'Recipe Name'),    
   ('#2', 'Ingredient'),
   ('#3', 'Cooking time')
   )

#define class-based Form imported from Django forms
class RecipeSearchForm(forms.Form):
    search_value = forms.CharField(max_length=120)
    search_type = forms.ChoiceField(choices = SEARCH__CHOICES)
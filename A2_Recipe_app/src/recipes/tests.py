from django.test import TestCase
from .models import Recipe

# Create your tests here.
class RecipeModelTest(TestCase):
    def setUpTestData():
       # Set up non-modified objects used by all test methods
        Recipe.objects.create(name= 'Test Recipe', cooking_time= 5, ingredients= 'ingredient list') 
    def test_user_username(self):
        #get user object
        recipe = Recipe.objects.get(id = 1)
        #get metadata
        field_label = recipe._meta.get_field('name').verbose_name
        #compare both valules
        self.assertEqual(field_label, 'name')
    def test_user_cooking_time(self):
        recipe = Recipe.objects.get(id = 1)
        field_label = recipe._meta.get_field('cooking_time').verbose_name
        self.assertEqual(field_label, 'cooking time')
    def test_user_ingredients(self):
        ingredients = Recipe.objects.get(id = 1)
        field_label = ingredients._meta.get_field('ingredients').verbose_name
        self.assertEqual(field_label, 'ingredients')
        
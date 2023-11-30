from django.test import TestCase
from .models import Recipe
from django.contrib.auth.models import User

# Create your tests here.
class RecipeModelTest(TestCase):
    def setUpTestData():
       # Set up non-modified objects used by all test methods
        user = User.objects.create_user(username="kevin", password="kevin")
        Recipe.objects.create(
            name="Test Recipe",
            cooking_time=5,
            ingredients="Lettuce, Tomatoes, Olive Oil, Salt",
            user_id=user,
        ) 
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

    # Tests URL for details page
    def test_get_absolute_url(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.get_absolute_url(), '/list/1')
        
    # Tests Ingredients value
    def test_ingredients_list(self):
        recipe = Recipe.objects.get(id=1)
        ingredients = recipe.ingredients
        self.assertEqual(ingredients, 'Lettuce, Tomatoes, Olive Oil, Salt')
    
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
    
class Ingredient(models.Model):
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name
    

class Recipe(models.Model):
    name = models.CharField(max_length=120)
    cooking_time = models.PositiveIntegerField()
    ingredients = models.ManyToManyField(Ingredient)
    # Adds creator user id to recipe
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.URLField(max_length=200)
    #underscore makes property protected
    _difficulty = models.CharField(max_length=50, null = True, blank = True, editable = False)
    _formatted_ingredients = models.CharField(max_length=50, null = True, blank = True, editable = False)


    ## formats ingredients list so that they are accessibly without having to run the forloop each time
    
    @property
    def formatted_ingredients(self):
        if self._formatted_ingredients is None:
           self._formatted_ingredients = ', '.join([ingredient.name for ingredient in self.ingredients.all()])
        return self._formatted_ingredients
    
    @formatted_ingredients.setter
    def formatted_ingredients(self, formatted_ingredients):
        self._formatted_ingredients = formatted_ingredients

    def calculate_difficulty(self):
        ingredient_count = len(self.ingredients.all())
        if self.cooking_time <= 5 and ingredient_count < 4:
            self.difficulty = "Easy" ## these are accessing the setter function on line 42
        elif self.cooking_time < 10 and ingredient_count >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and ingredient_count < 4:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"

    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse("recipes:detail", kwargs={"pk": self.pk}) # reverse takes the name and returns the full path
    
    def get_absolute_url_delete(self):
        return reverse("recipes:delete", kwargs= {"pk": self.pk})
    
    def get_absolute_url_update(self):
        return reverse("recipes:update", kwargs= {"pk": self.pk})
    
    # getter (refers to the {{object.difficulty}})
    @property
    def difficulty(self):
        if self._difficulty is None:
            self.calculate_difficulty()
        return self._difficulty

    # setter
    @difficulty.setter
    def difficulty(self, difficulty):
        self._difficulty = difficulty
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
    
class Recipe(models.Model):
    name = models.CharField(max_length=120)
    cooking_time = models.PositiveIntegerField(help_text='in minutes')
    ingredients = models.CharField(max_length=120, help_text='separated by a comma')
    # Adds creator user id to recipe
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='recipes', default= 'no_picture.jpg')
    #underscore makes property protected
    _difficulty = models.CharField(max_length=50, null = True, blank = True, editable = False)

    def calculate_difficulty(self):
        ingredient_arr = self.ingredients.split(', ')
        ingredient_count = len(ingredient_arr)
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
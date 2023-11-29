from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

# Create your models here.
    
class Recipe(models.Model):
    name = models.CharField(max_length=120)
    cooking_time = models.PositiveIntegerField(help_text='in minutes')
    ingredients = models.TextField(help_text='separated by a comma')
    # Adds creator user id to recipe
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='recipes', default= 'no_picture.jpg')

    def calculate_difficulty(self):
        ingredient_count = len(self.ingredients)
        if self.cooking_time <= 5 and ingredient_count < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and ingredient_count >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and ingredient_count < 4:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"

    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse("recipes:detail", kwargs={"pk": self.pk})

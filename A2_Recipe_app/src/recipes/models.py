from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=120)
    cooking_time = models.PositiveIntegerField(help_text='in minutes')
    ingredients = models.CharField(max_length= 50, help_text='one at a time')

    def __str__(self):
        return str(self.name)
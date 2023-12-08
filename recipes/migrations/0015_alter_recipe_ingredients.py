# Generated by Django 4.2.8 on 2023-12-08 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0014_remove_recipe_ingredients_recipe_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(related_name='ingredients', to='recipes.ingredient'),
        ),
    ]
# Generated by Django 4.2.8 on 2023-12-08 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0017_recipe_formated_ingredients'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='formated_ingredients',
            new_name='_formatted_ingredients',
        ),
    ]

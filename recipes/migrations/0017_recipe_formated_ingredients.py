# Generated by Django 4.2.8 on 2023-12-08 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0016_alter_recipe_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='formated_ingredients',
            field=models.CharField(blank=True, editable=False, max_length=50, null=True),
        ),
    ]

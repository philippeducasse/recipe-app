# Generated by Django 4.2.7 on 2023-11-28 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_alter_recipe_image_remove_recipe_ingredients_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='no_picture.jpg', upload_to='recipes'),
        ),
    ]
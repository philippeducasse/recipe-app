# Generated by Django 4.2.7 on 2023-11-28 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_alter_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='no_picture.jpg', upload_to='media'),
        ),
    ]
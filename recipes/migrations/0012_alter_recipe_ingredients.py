# Generated by Django 4.2.8 on 2023-12-04 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_recipe__difficulty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.CharField(help_text='separated by a comma', max_length=120),
        ),
    ]
# Generated by Django 4.0.6 on 2023-09-02 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_remove_recipe_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.CharField(choices=[('Appetizers', 'Appetizers'), ('Maincourses', 'Maincourses'), ('Desserts', 'Desserts'), ('Drinks', 'Drinks'), ('Breakfast', 'Breakfast')], max_length=30),
        ),
    ]

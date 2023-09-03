from django.db import models
from django.contrib.auth.models import User
class Recipe(models.Model):
      Category =(
        ('Appetizers', 'Appetizers'),
        ('MainCourse', 'MainCourse'),
        ('Desserts', 'Desserts'),
        ('Drinks', 'Drinks'),
        ('Breakfast', 'Breakfast'),
      )
      title = models.CharField(max_length=200)
      ingredients = models.TextField()
      instructions = models.TextField()
      image = models.ImageField(upload_to='recipes/images/')
      category = models.CharField(max_length=30, choices=Category)

      def __str__(self):
          return self.title
        
      

      
      



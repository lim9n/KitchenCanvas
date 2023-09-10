from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_recipe, name='submit_recipe'),
    path('<str:category>/', views.display_recipes, name='display_recipes'),
    path('search/', views.search_posts, name='searchposts'),
    
]

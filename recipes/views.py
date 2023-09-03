from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm
from .models import Recipe


@login_required
def submit_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save()
            return redirect('index')
    else:
        form = RecipeForm()
    return render(request, 'recipes/submit_recipe.html', {'form': form})


@login_required
def display_recipes(request, category=None):
    recipes = Recipe.objects.filter(category=category)

    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

@login_required
def search_recipes(request):
    keyword = ''
    keyword = request.GET['q']
    print(keyword)
    if keyword:
        ingredients = keyword.split(',')
        search_recipes = Recipe.objects.filter(ingredients__icontains=ingredients[0].strip())
        for ingredient in ingredients[1:]:
            search_recipes = search_recipes | Recipe.objects.filter(ingredients__icontains=ingredient.strip())
    else:
        search_recipes = Recipe.objects.all()
        
        
    context={'search_recipes': search_recipes, 'keyword': keyword}
    return render(request, 'recipes/search.html', context)

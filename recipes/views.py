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

def search_posts(request):
    query = request.GET.get('q', '')
    results = []  

    if query:
        results = Recipe.objects.filter(title__icontains=query)

    context = {
        'results': results,
        'submitbutton': 'Search',
    }

    return render(request, 'search.html', context)



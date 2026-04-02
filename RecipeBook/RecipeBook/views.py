from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.models import Recipe, Favourite, Like, comment
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect


def home(request):
    return render(request, 'home.html',{"user": request.user})

def myrecipe(request):
    recipes = Recipe.objects.filter(user=request.user)
    print(recipes)
    data = {'recipes': recipes}
    return render(request, 'myrecipe.html', data)

@login_required(login_url='login')
def add_recipe(request):
    user = request.user
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        ingredients = request.POST.get('ingredients')
        category = request.POST.get('category')
        steps = request.POST.get('steps')
        image = request.FILES.get('image')

        # Here you would typically save the recipe to the database
        # For now, we'll just print the data to the console (or handle it as needed)
        print(f"Title: {title}")
        print(f"Description: {description}")
        print(f"Ingredients: {ingredients}")
        print(f"Category: {category}")
        print(f"Steps: {steps}")
        print(f"Image: {image}")
        print(f"User: {user.username}")

        # Redirect or render a success message after saving
        
        newrecipe = Recipe.objects.create(
            title=title,
            description=description,
            ingredients=ingredients,
            category=category,
            steps=steps,
            image=image,
            user=user
        )   
        newrecipe.save()
        messages.success(request, 'Recipe added successfully!')
        return redirect('recipes')
    return render(request, 'addrecipe.html')
    
        
@login_required(login_url='login')
def recipes(request, post=None):
        search_query = request.GET.get('search')
        cat_wise = request.GET.get('cat_wise')

        if cat_wise:
            category = request.GET.get('search')
            recipes = Recipe.objects.filter(category=category)
        elif search_query:
            recipes = Recipe.objects.filter(title__icontains=search_query)
        else:
            recipes = Recipe.objects.all()
        

        data = {'recipes': recipes}
        return render(request, 'recipes.html', data)

@login_required(login_url='login')
def myrecipes(request):
    allrecipes = Recipe.objects.filter(user = request.user)
    data = {'recipes': allrecipes}
    return render(request, 'myrecipes.html', data)

@login_required(login_url='login')
def recipedetails(request, id):
    if request.method == 'POST' and 'comment_submit' in request.POST:
        comment_text = request.POST.get('comment_text')
        if comment_text:
            recipe = Recipe.objects.get(id=id)
            new_comment = comment.objects.create(
                recipe=recipe,
                user=request.user,
                text=comment_text
            )
            new_comment.save()
            messages.success(request, 'Comment added successfully!')
            return redirect('recipedetails', id=id)
    post = Recipe.objects.get(id=id)  
    like = Like.objects.filter(recipe=post).count()
    favourites = Favourite.objects.filter(recipe=post).count()
    comments = comment.objects.filter(recipe=post)
    data = {'post': post, 'like': like, 'favourites': favourites, 'comments': comments}
    return render(request, 'recipedetails.html',data)

@login_required(login_url='login')
def favourites(request):
    favourites = Favourite.objects.filter(user=request.user)
    data = {'favourites': favourites}
    return render(request, 'favourites.html', data)

@login_required(login_url='login')
def like_post(request, id):
    
    post = get_object_or_404(Recipe, id=id)
    like = Like.objects.filter(recipe=post, user=request.user)

    if like.exists():
        like.delete()   # Unlike
    else:
        Like.objects.create(recipe=post, user=request.user)  # Like

    if like is not None:
        already_liked = Like.objects.filter(recipe=post, user=request.user)
        if not already_liked.exists():
            like = Like.objects.create(recipe=post, user=request.user)
            like.save()

            post.likes += 1
            post.save()
            messages.success(request, 'Post unliked successfully!')
            return redirect('recipedetails', id=id) 
        else:
            like = Like.objects.filter(recipe=post, user=request.user)
            like.delete()   # Unlike
            post.likes -= 1
            post.save()
            messages.success(request, 'Post liked successfully!')
            return redirect('recipedetails', id=id)
    elif 'commentbtn' in request.POST:
        comment_text = request.POST.get('comment')
        if comment_text is not None:
                newcomment = comment.objects.create( recipe=post,user=request.user,text=comment_text)
                messages.success(request, 'Comment added successfully!')
                return redirect('recipedetails', id=id)
        else:
            messages.error(request, 'Comment cannot be empty.')
            return redirect('recipedetails', id=id)

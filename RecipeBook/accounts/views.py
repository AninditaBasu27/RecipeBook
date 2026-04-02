from operator import pos
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Like, Recipe, Favourite

# Create your views here.

def login_handler(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            # If credentials are valid, log in
            login(request, user)
            messages.success(request, f'Welcome {username}, logged in successfully!')
            return redirect('home')
        else:
            # Invalid credentials
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html')

    
    return render(request, 'login.html')

def register_handler(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')   
        password = request.POST.get('password')
        
        if User.object.filter(email=email).exists():
            messages.error(request, "Email already registered!")
        
        else:
            newuser = User(username=name, email=email, password=password)
            newuser.save()
            messages.success(request,"Registration successful.")
            return redirect('login')
        return render(request, 'register.html')
    
def register_handler(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm-password')

        # 1. Check required fields
        if not username or not email or not password1 or not password2:
            messages.error(request, "All fields are required!")
            return render(request, 'register.html')

        # 2. Check password match
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return render(request, 'register.html')

        # 3. Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return render(request, 'register.html')

        # 4. Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return render(request, 'register.html')

        # 5. Create user
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        # 6. Auto login after registration
        # login(request, user)
        # messages.success(request, f"Welcome {username}, your account has been created!")
        # return redirect('home')
    
    return render(request, 'register.html')

def logout_handler(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login')

def searchbar(request):
    query = request.GET.get('q')  # get the text from input field
    # later: filter recipes from DB
    return render(request, 'search_results.html', {'query': query})

def likedrecipes(request, id):
    print("recipie id",id)
    recipe = Recipe.objects.get(id=id)
    Like.objects.create(recipe=recipe, user=request.user)
    messages.success(request, 'Recipe liked successfully!')
    return redirect('recipedetails', id=id)

def addToFavouriterecipes(request, id):
    recipe = Recipe.objects.get(id=id)
    Favourite.objects.create(recipe=recipe, user=request.user)
    messages.success(request, 'Recipe Favourited successfully!')
    return redirect('favourites')

def recipedelete(request,id):
    Recipe.objects.filter(id=id).delete()
    messages.success(request, 'Recipe deleted successfully!')
    return redirect('myrecipe') 

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name='home'),   
    path("myrecipe/",views.myrecipe, name='myrecipe'),
    path("accounts/", include('accounts.urls'), name='accounts'),
    path("addrecipe/",views.add_recipe, name='addrecipe'),
    path("myrecipe/",views.myrecipe, name='myrecipe'),
    path("favourites/",views.favourites, name='favourites'),
    path("recipes ",views.recipes, name='recipes'),
    path("<int:id>/", views.recipedetails, name='recipedetails'),
    path("<int:id>/like/", views.like_post, name="like_post"),
    
      
       
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


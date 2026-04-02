

from django.urls import path, include
from . import views

urlpatterns = [
    path("login/", views.login_handler, name='login'),
    path("register/", views.register_handler, name='register'),
    path("logout/", views.logout_handler, name='logout'),
    path('search/', views.searchbar, name='search'),
    path('likedrecipes/<int:id>/',views.likedrecipes, name='liked_recipes'),
    path("addToFavouriterecipes/<int:id>/", views.addToFavouriterecipes, name='addToFavouriterecipes'),
    path('recipedelete/<int:id>/', views.recipedelete, name='recipedelete'), 
]

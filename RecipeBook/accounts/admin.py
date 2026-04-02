from django.contrib import admin
from .models import Recipe, Favourite, Like, comment, User

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Favourite)
admin.site.register(Like)
admin.site.register(comment)


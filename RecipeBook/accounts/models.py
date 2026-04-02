from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    CATEGORY_CHOICES = [
       ('Healthy Salads', 'Healthy Salads'),
       ('Desserts & Sweets', 'Desserts & Sweets'),
       ('Quick Snacks', 'Quick Snacks'),
       ('Drinks & Beverages', 'Drinks & Beverages'),
       ('Non-Vegetarian', 'Non-Vegetarian'),
       ('Vegetarian & Vegan', 'Vegetarian & Vegan'),

        ]
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    steps = models.TextField()
    image = models.ImageField(upload_to='recipeIMGS/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes', null=True)
    description = models.TextField(default="No description provided.")

    def __str__(self):
        return self.title
    
class comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.recipe.title}"
    
class Like(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='like')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like')
    # recipe.recipe_likes.count()
    def is_liked_by(self, user):
        if user.is_authenticated:
            return self.likes.filter(user=user).exists()
        return False


    def meta():
        unique_together = ('recipe', 'user') 

    def __str__(self):
        return f"Like by {self.user.username} likes {self.recipe.title}"

class Favourite(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='favourites')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourites')
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Favourite: {self.recipe.title}"
    

# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comments")
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Comment by {self.user.username} on {self.recipe.title}"
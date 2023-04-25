from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    ingredients = models.JSONField()
    preparation_steps = models.TextField()
    cooking_time = models.IntegerField()
    nutrition_info = models.JSONField()


class Rating(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
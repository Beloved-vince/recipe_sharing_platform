from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.
class Recipe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    author = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    ingredients = models.JSONField()
    preparation_steps = models.TextField()
    cooking_time = models.IntegerField()
    nutrition_info = models.JSONField()


class Rating(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    fullname = models.CharField(max_length=100)

class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
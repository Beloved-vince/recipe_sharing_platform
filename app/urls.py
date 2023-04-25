from django.urls import path
from .views import RecipeList, RecipeDetail, RatingCreate, CommentCreate

urlpatterns = [
    path('recipes/', RecipeList.as_view()),
    path('recipes/<int:pk>/', RecipeDetail.as_view()),
    path('ratings/', RatingCreate.as_view()),
    path('comments/', CommentCreate.as_view()),
]

from django.urls import path
from .views import RecipeList, RecipeDetail, CommentCreate, RatingCreate
from . import views

urlpatterns = [
    path('recipes/', RecipeList.as_view()),
    path('recipes/<uuid:pk>/', RecipeDetail.as_view()),
    path('ratings/<uuid:pk>', RatingCreate.as_view()),
    path('comments/<uuid:pk>', CommentCreate.as_view()),
]

from django.shortcuts import render
from rest_framework import generics
from .models import Recipe, Comment, Rating
from .serializers import RecipeSerializer, RatingSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

# Create your views here.
class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def post(self, request):
        author_name = request.user.first_name
        recipe = Recipe.objects.create(
            author=author_name,
            name=request.data['name'],
            ingredients=request.data['ingredients'],
            preparation_steps=request.data['preparation_steps'],
            cooking_time=request.data['cooking_time'],
            nutrition_info=request.data['nutrition_info']
        )
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)
    
class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class RatingCreate(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class CommentCreate(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

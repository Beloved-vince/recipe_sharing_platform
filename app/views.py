from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import Recipe, Comment, Rating
from .serializers import RecipeSerializer, RatingSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status



class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        """Read permission allowed to any request but 
            would be set to allow GET, PUT, HEAD, Or OPTIONS request 
        """
        if request.method in ['GET', 'PATCH' 'HEAD', 'OPTIONS']:
            return True
        
        return obj.author == request.user.username
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
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    authentication_classes = [TokenAuthentication]
    
    def perform_create(self, serializer):
        author = self.request.user.first_name
        recipe = serializer.save(author=author)
        return Response(self.serializer_class(recipe).data)


class RatingCreate(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
     
    def post(self, request, pk):
        if request.user is IsAuthorOrReadOnly:
            return Response({'error': 'Not authorised to rate your recipe'})
        
        firstname = request.user.first_name
        lastname = request.user.last_name
        
        fullname = firstname + ' '+  lastname
        user = request.user
        recipe_id = get_object_or_404(Recipe, id=pk)
        score = request.data.get('score')
        
        rating = Rating.objects.create(recipe=recipe_id, user=user, score=score, fullname=fullname)
        serializer = RatingSerializer(rating)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CommentCreate(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


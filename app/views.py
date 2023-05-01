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
    """
        Returns all recipes and their details present in the
        database
        args: 
            queryset: get all the recipe present in the database
            serializer_class: serializes only what must be return after
                validation
            permission_classes: check if requested user is authenticated
                it returns 401 error if requested user is not authenticated
            authentication_classes: Check if requested user user include the ApI
                token into the header before performing any operations else it 
                returns 403 forbidden error
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


    def post(self, request):
        """"
            Accept post request only to allow user to upload recipe
            and returns all recipes available
            Args:
                author_name: get the authenticated requested user name
                recipe: getting the following as a respond to the server
                    name: recipe name
                    ingredients: recipe ingredients in dictionary format
                    preparation_steps: In a text format
                    cooking_time: In integer type
                    nutrition_info: in dictionary format
        """
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
    """
        Returns all recipes and their details present in the
        database
        args: 
            queryset: get all the recipe present in the database
            serializer_class: serializes only what must be return after
                validation
            permission_classes: check if requested user is authenticated
                it returns 401 error if requested user is not authenticated
            authentication_classes: Check if requested user include the ApI
                token into the header before performing any operations else it 
                returns 403 forbidden error and if the requested user is the author
                of the recipe before performing operation else return error 403
    """
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
       
        user = request.user
        recipe_id = get_object_or_404(Recipe, id=pk)
        score = request.data.get('score')
        
        rating = Rating.objects.create(recipe=recipe_id, user=user, score=score, fullname=fullname)
        serializer = RatingSerializer(rating)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CommentCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request, *args, **kwargs):
         
        firstname = request.user.first_name
        lastname = request.user.last_name
        
        fullname = firstname + ' '+  lastname
        user = request.user
        recipe_id = get_object_or_404(Comment, id=args)
        text = request.data.get('text')
        
        rating = Rating.objects.create(recipe=recipe_id, user=user, text=text, fullname=fullname)
        serializer = RatingSerializer(rating)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

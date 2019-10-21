# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from recipes.models import User, Step, Ingredient, Recipe
from recipes.serializers import UserSerializer, StepSerializer, IngredientSerializer, RecipeSerializer


class RecipeList(APIView):
    """List all recipes, or create a new recipe."""
    def get(self, request, format=None):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRecipesList(APIView):
    """List all recipes by a particular user"""
    def get(self, request, user_id, format=None):
        recipes = Recipe.objects.filter(user__id=user_id)
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)
        
class RecipeDetail(APIView): 
    """Retrieve, update or delete a recipe instance."""
    def get_object(self, user_id): 
        try: 
            return Recipe.objects.get(user__id=user_id)
        except Recipe.DoesNotExist:
            raise Http404
    
    def get(self, request, user_id, format=None): 
        recipe = self.get_object(user_id)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    def put(self, request, user_id, format=None): 
        recipe = self.get_object(user_id)
        serializer = RecipeSerializer(recipe, data=request.data)  
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id, format=None): 
        recipe = self.get_object(user_id); 
        print("deleting the recipe", recipe)
        recipe.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)




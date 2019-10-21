from django.contrib.auth import get_user_model
from rest_framework import serializers

from recipes.models import User, Ingredient, Recipe, Step

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class RecipeSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Recipe
        fields = ('id', 'name', 'user', 'steps', 'ingredients')


class StepSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Step
        fields = ('id', 'step_text')


class IngredientSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Ingredient
        fields = ('id', 'text')
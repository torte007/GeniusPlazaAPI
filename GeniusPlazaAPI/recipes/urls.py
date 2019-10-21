from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from recipes import views

urlpatterns = [
    path('recipes/', views.RecipeList.as_view()),                   # List all the recipes
    path('recipes/user/<int:user_id>/', views.UserRecipesList.as_view()),# List all the recipes by the user with id = user_id
    path('recipes/<int:user_id>/', views.RecipeDetail.as_view())    # Get a single recipe 
]

urlpattherns = format_suffix_patterns(urlpatterns)
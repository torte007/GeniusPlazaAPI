# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=100, null=False, blank=False, unique=True)

class Recipe(models.Model): 
    """A Recipe must have: a name(string, not null), a user(one to one relationship), some ingredients, and some steps."""
    name = models.CharField(max_length=150, null=False)
    # Consider changing to one to many so that each user can have more than one recipe. 
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='recipes')

    def __str__(self): 
        return self.name

class Step(models.Model):
    step_text = models.TextField(null=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='steps')

    def __str__(self): 
        return self.step_text 

class Ingredient(models.Model): 
    text = models.TextField(null=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')

    def __str__(self): 
        return self.text
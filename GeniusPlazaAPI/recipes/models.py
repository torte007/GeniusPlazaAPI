# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User:
    """ A user has the following attributes: username(unique field), email(unique field), first_name,
        last_name, and password. """
    pass

class Step:
    """A step must have: step_text(string field, not null)"""
    pass

class Ingredient: 
    """An Ingredient must have: text(not null, string)"""
    pass

class Recipe: 
    """A Recipe must have: a name(string, not null), a user(one to one relationship), some ingredients, and some steps."""
    pass
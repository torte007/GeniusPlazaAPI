# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import User

class Test_User(TestCase): 
    def test_str(self): 
        user = User(username='toms', email='tomasvortegar@gmail.com')
        self.assertEqual(str(user), 'toms')
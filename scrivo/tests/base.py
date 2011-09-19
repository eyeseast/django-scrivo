import os

from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase

from scrivo.models import Post

f = lambda fn: os.path.abspath(os.path.join(os.path.dirname(__file__), fn))

class BlogPostTest(TestCase):
    
    def create_post(self, **kwargs):
        defaults = {
            "title"   : "This is a test",
            "content" : "This is only a test."
        }
        defaults.update(kwargs)
        return Post.objects.create(**kwargs)
    
    def create_user(self, **kwargs):
        defaults = {
            'username': 'guynoir', 
            'email': 'guy@example.com',
            'password': None
        }
        defaults.update(kwargs)
        return User.objects.create_user(
            defaults['username'], 
            defaults['email'], 
            defaults['password']
        )

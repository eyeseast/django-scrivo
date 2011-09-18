import datetime
import os

from django.conf import settings
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
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

class SimplePostTest(BlogPostTest):
    
    def setUp(self):
        self.user = self.create_user()
        self.post = self.create_post(author=self.user)
    
    def test_slugify(self):
        """
        Ensure a post has a slug, and that it's the slugified title
        """
        self.assertEqual(self.post.slug, slugify(self.post.title))
    
    def test_publish(self):
        """
        Ensure publishing a post sets the right date
        """
        self.post.publish()
        self.assertEqual(self.post.status, Post.STATUS.public)
        self.assertEqual(
             self.post.published.date(), 
             datetime.datetime.now().date()
        )

class PostContentTest(BlogPostTest):
    
    def setUp(self):
        DEFAULT_SPLIT_MARKER = "<!-- split -->"
        self.SPLIT_MARKER = getattr(settings, 'SPLIT_MARKER', DEFAULT_SPLIT_MARKER)
        
        # read in post text (from ipsum.txt) and ensure the right
        # split marker is used (user can customize this)
        self.post_text = open(f('ipsum.txt')).read().replace(
            DEFAULT_SPLIT_MARKER, 
            self.SPLIT_MARKER
        )
        
        self.user = self.create_user()
        self.post = self.create_post(
            author = self.user,
            content = self.post_text
        )
    
    def test_split_content(self):
        self.assertEqual(unicode(self.post.content), self.post_text)
        
        excerpt, rest = self.post_text.split(self.SPLIT_MARKER)
        self.assertEqual(self.post.content.excerpt.strip(), excerpt.strip())

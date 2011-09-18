from django.test import TestCase

from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from scrivo.models import Post

class BlogPostTest(TestCase):
    
    def create_post(self, **kwargs):
        defaults = {
            "title"   : "This is a test",
            "content" : "This is only a test."
        }
        defaults.update(kwargs)
        return Post.objects.create(**kwargs)
    
    def setUp(self):
        self.user = User.objects.create_user('guynoir', 'guy@example.com')
        self.post = self.create_post(author=self.user)
    
    def test_slugify(self):
        """
        Ensure a post has a slug, and that it's the slugified title
        """
        self.assertEqual(self.post.slug, slugify(self.post.title))
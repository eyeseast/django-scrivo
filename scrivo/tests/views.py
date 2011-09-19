import datetime
import os

from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from scrivo.models import Post
from scrivo.tests.base import BlogPostTest, f

class PostViewTest(BlogPostTest):

    def setUp(self):
        
        self.user = self.create_user()
        # let's make 100 fake posts
        date = datetime.datetime(2011, 1, 1)
        for i in range(100):
            self.create_post(
                title="Test %s" % i,
                author = self.user,
                published = date,
                status = Post.STATUS.public
            )
            
            # incriment the date
            date += datetime.timedelta(days=1)
        
    def test_year_archive(self):
        response = self.client.get(reverse('scrivo_year_archive', args=[2011]))
        self.assertEqual(response.status_code, 200)
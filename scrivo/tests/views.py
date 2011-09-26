import datetime
import os

from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from scrivo.models import Post
from scrivo.settings import DEFAULT_PAGINATE_BY, INDEX_POST_COUNT
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
    
    def test_archive_index(self):
        response = self.client.get(reverse('scrivo_archive_index'))
        self.assertEqual(response.status_code, 200)
        
        posts = response.context.get('object_list')
        if not posts:
            self.fail("No posts in context")
        
        self.assertEqual(posts.count(), INDEX_POST_COUNT)
                
        
    def test_year_archive(self):
        response = self.client.get(reverse('scrivo_year_archive', args=[2011]))
        self.assertEqual(response.status_code, 200)
        
        posts = response.context.get('object_list')
        if not posts:
            self.fail("No posts in context")
        
        paginator = response.context.get('paginator')
        if not paginator:
            self.fail("Not paginated")
        
        # check that we're paginating right
        self.assertEqual(posts.count(), DEFAULT_PAGINATE_BY)
        
        # and that we have the right total
        self.assertEqual(paginator.count, 100)
    
    def test_month_archive(self):
        response = self.client.get(reverse('scrivo_month_archive', args=[2011, 'jan']))
        self.assertEqual(response.status_code, 200)
        
        posts = response.context.get('object_list')
        if not posts:
            self.fail("No posts in context")
        
        paginator = response.context.get('paginator')
        if not paginator:
            self.fail("Not paginated")
    
        self.assertEqual(len(posts), DEFAULT_PAGINATE_BY)
        self.assertEqual(paginator.count, 31) # for january
    
    def test_day_archive(self):
        response = self.client.get(reverse('scrivo_day_archive', args=[2011, 'jan', 5]))
        self.assertEqual(response.status_code, 200)
        
        posts = response.context.get('object_list')
        if not posts:
            self.fail("No posts in context")
        
        # since we're doing one post per day
        self.assertEqual(len(posts), 1)
        
        
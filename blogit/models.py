import datetime
from django.contrib.auth.models import User
from django.db import models

from model_utils import Choices
from model_utils.fields import MonitorField, SplitField, StatusField
from model_utils.managers import PassThroughManager
from model_utils.models import TimeStampedModel

from bloggit.managers import PostQuerySet

class PostBase(TimeStampedModel):
    """
    Base class for Post-like models
    
    This class defines basic fields and logic for a blog post,
    including author, title, status (whether it's published or not)
    and content.
    
    By default, it uses an InheritanceManager, allowing subclasses
    to be included in a queryset.
    
    Taxonomies (such as tags and categories) are deliberately excluded
    from the base class to allow more control over how this blog
    fits into a larger site.
    """
    STATUS = Choices(
        ('draft', 'Draft'),
        ('public', 'Public'),
        ('hidden', 'Hidden'),
    )
    
    # metadata
    author = models.ForeignKey(User)
    published = models.DateTimeField(blank=True, null=True)
    status = StatusField(default=STATUS.draft)
    status_changed = MonitorField(monitor='status')
    
    # content
    excerpt = models.TextField(blank=True,
        help_text="Add a manual excerpt")
    body = SplitField(blank=True)
    
    # manager
    objects = PassThroughManager(PostQuerySet)
    
    class Meta:
        abstract = True
        ordering = ('-published', '-created')
    
    def __unicode__(self):
        return self.title
    
    def publish(self):
        if not self.published:
            self.published = datetime.datetime.now()
        self.status = self.STATUS.public
        self.save()
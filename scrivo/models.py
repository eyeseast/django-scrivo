import datetime
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify

from model_utils import Choices
from model_utils.fields import MonitorField, SplitField, StatusField
from model_utils.managers import PassThroughManager
from model_utils.models import TimeStampedModel
from revisions.shortcuts import TrashableVersionedModel
from taggit.managers import TaggableManager

from scrivo.managers import PostQuerySet
from scrivo.utils import get_post_base

class PostBase(TimeStampedModel):
    """
    Base class for Post-like models
    
    This class defines basic fields and logic for a blog post,
    including author, title, status (whether it's published or not)
    and content, plus timestamp fields.
    
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
    status_changed = MonitorField(monitor='status', editable=False)
    
    # content
    title = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255)
    excerpt = models.TextField(blank=True,
        help_text="Add a manual excerpt")
    content = SplitField(blank=True)
    
    # manager
    objects = PassThroughManager(PostQuerySet)
    
    class Meta:
        abstract = True
        get_latest_by = "published"
        ordering = ('-published', '-created')
    
    def __unicode__(self):
        return self.title
    
    def publish(self):
        if not self.published:
            self.published = datetime.datetime.now()
        self.status = self.STATUS.public
        self.save()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title or self.id)
        super(PostBase, self).save(*args, **kwargs)


class VersionedPostBase(PostBase, TrashableVersionedModel):
    """
    A Post ancestor that includes version control and delete safety
    """
    
    class Meta(PostBase.Meta):
        abstract = True


class Post(get_post_base()):
    """
    A basic blog post:
     - tags provided by django-taggit
     - versioning provided by django-revisions
    """
    allow_comments = models.BooleanField(default=True)
    tags = TaggableManager(blank=True)
    
    @models.permalink
    def get_absolute_url(self):
        return ('scrivo_post_detail', None, {'year': self.published.strftime('%Y'),
                                             'month': self.published.strftime('%b').lower(),
                                             'day': self.published.stftime('%d'),
                                             'slug': self.slug})


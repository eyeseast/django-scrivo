from django.views.generic import dates
from scrivo.models import Post

class PostArchiveMixin(object):
    """
    Mixin to add common archive view attributes
    """
    date_field = "published"
    queryset = Post.objects.public()
    

class PostArchive(PostArchiveMixin, dates.ArchiveIndexView):
    pass

class PostYearArchive(PostArchiveMixin, dates.YearArchiveView):
    pass

class PostMonthArchive(PostArchiveMixin, dates.MonthArchiveView):
    pass

class PostDayArchive(PostArchiveMixin, dates.DayArchiveView):
    pass

class PostDetail(PostArchiveMixin, dates.DateDetailView):
    pass
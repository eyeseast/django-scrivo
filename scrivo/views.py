from django.views.generic import dates
from scrivo.models import Post
from scrivo.settings import DEFAULT_PAGINATE_BY, INDEX_POST_COUNT

class PostArchiveMixin(object):
    """
    Mixin to add common archive view attributes
    """
    date_field = "published"
    queryset = Post.objects.public()
    paginate_by = DEFAULT_PAGINATE_BY

class PostArchive(PostArchiveMixin, dates.ArchiveIndexView):
    paginate_by = INDEX_POST_COUNT

class PostYearArchive(PostArchiveMixin, dates.YearArchiveView):
    make_object_list = True

class PostMonthArchive(PostArchiveMixin, dates.MonthArchiveView):
    pass

class PostDayArchive(PostArchiveMixin, dates.DayArchiveView):
    pass

class PostDetail(PostArchiveMixin, dates.DateDetailView):
    pass
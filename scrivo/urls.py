from django.conf.urls.defaults import patterns, url
from scrivo import views

urlpatterns = patterns('',
    url(r'^$', 
        views.PostArchive.as_view(), 
        name="scrivo_archive_index"),
    
    url(r'^(?P<year>\d{4})/$', 
        views.PostYearArchive.as_view(), 
        name="scrivo_year_archive"),
        
    url(r'^(?P<year>\d{4})/(?P<month>[A-Za-z]{3})/$',
        views.PostMonthArchive.as_view(),
        name="scrivo_month_archive"),
    
    url(r'^(?P<year>\d{4})/(?P<month>[A-Za-z]{3})/(?P<day>\d{1,2})/$',
        views.PostDayArchive.as_view(),
        name="scrivo_day_archive"),
    
    url(r'^(?P<year>\d{4})/(?P<month>[A-Za-z]{3})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',
        views.PostDetail.as_view(),
        name="scrivo_post_detail"),
)
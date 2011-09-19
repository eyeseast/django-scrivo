from django.conf import settings

POST_BASE_MODEL = getattr(settings, 'SCRIVO_POST_BASE_MODEL', 
    'scrivo.models.VersionedPostBase') 

DEFAULT_PAGINATE_BY = getattr(settings, 'SCRIVO_DEFAULT_PAGINATE_BY', 15)

INDEX_POST_COUNT = getattr(settings, 'SCRIVO_INDEX_POST_COUNT', DEFAULT_PAGINATE_BY)

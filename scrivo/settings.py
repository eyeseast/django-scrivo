from django.conf import settings

POST_BASE_MODEL = getattr(settings, 'SCRIVO_POST_BASE_MODEL', 
    'scrivo.models.VersionedPostBase') 


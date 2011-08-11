from django.conf import settings

POST_BASE_MODEL = getattr(settings, 'SCRIVO_POST_BASE_MODELS', 
    'scrivo.models.VersionedPostBase') 


from django.core.exceptions import ImproperlyConfigured
from scrivo.settings import POST_BASE_MODEL

try:
    import importlib
except ImportError:
    from django.utils import importlib


def get_post_base():
    try:
        mod_name, cls_name = POST_BASE_MODEL.rsplit('.', 1)
    except ValueError:
        raise ImproperlyConfigured("%s isn't a post class" % POST_BASE_MODEL)

    try:
        mod = importlib.import_module(mod_name)
    except ImportError, e:
        raise ImproperlyConfigured("Couldn't import module %s: %s" % (mod_name, e))

    try:
        return getattr(mod, cls_name)
    except AttributeError:
        raise ImproperlyConfigured("%s doesn't define a %s class" % (mod_name, cls_name))
    

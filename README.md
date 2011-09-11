Django Scrivo
=============

Scrivo is a simple, pluggable blog engine that can be dropped into a larger Django project.

Scrivo is not a WordPress clone, not is it meant to be your whole site. If your site *is* a blog, use WordPress (or one of the many Django-powered alternatives, if that's your thing). If you want your site to *have* a blog, drop in Scrivo and you should be good to go.

Quick Start
------------

For fastest results, do the usual Django installation:

    pip install django-scrivo (coming soon)

Add `scrivo` to your `INSTALLED_APPS` and run

    $ python manage.py syncdb


Almost-as-quick start
---------------------

Scrivo is built to play nicely with other apps, and many of its features can be used or discarded as needed. Scrivo only defines one model, `Post`. The `Post` model descends from several base classes, which can be swapped out or replaced altogether.

By default, `Post` descends from `scrivo.models.VersionedPostBase`. The default model includes tags (from [django-taggit][taggit]) and versioning (from [django-versioning][versioning]).

 [taggit]: http://django-taggit.readthedocs.org/en/latest/
 [versioning]: http://stdbrouw.github.com/django-revisions/

To use a different parent class, use the setting `SCRIVO_POST_BASE_MODEL` with the path to a new parent. If you just want to add a few more fields, descend from `scrivo.models.VersionedPostBase`.

Categories aren't required, but can be added via [django-categories][categories], which will let you define relations in `settings.py`.

 [categories]: http://pypi.python.org/pypi/django-categories/0.6

Dependencies
------------

Scrivo relies heavily on third-party apps. It lives in the Django ecosystem and tries not to reinvent wheels where possible (and yes, I realize this is yet another Django blog). Here's what we use:

- django>=1.3
- django-markitup
- django-model-utils
- django-taggit
- django-revisions
- markdown

### About the name ###
In Italian, "scrivo" means "I write." It was the cleverest thing I could come up with.
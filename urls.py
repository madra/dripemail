from __future__ import absolute_import

import django
from django.conf.urls import url
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.cache import never_cache

from . import views

"""
if django.VERSION >= (1, 8):
    urlpatterns = [
        url(r'^add_dripemail/', staff_member_required(views.add_dripemail),
            name='add_dripemail'),
        url(r'^browse/', never_cache(staff_member_required(views.browse)),
            name='ckeditor_browse'),
    ]
else:
    from django.conf.urls import patterns
    urlpatterns = patterns(
        '',
        url(r'^upload/', staff_member_required(views.upload),
            name='ckeditor_upload'),
        url(r'^browse/', never_cache(staff_member_required(views.browse)),
            name='ckeditor_browse'),
    )
"""
if django.VERSION >= (1, 8):
    from django.conf.urls import patterns

urlpatterns = patterns(
    '',
    url(r'^add_dripemail/', views.add_dripemail,
        name='add_dripemail'),

    url(r'^dripemail/(\w+)/subscribe$', views.subscribe,
        name='subscribe_url'),

    url(r'^dripemail/(\w+)/unsubscribe$', views.unsubscribe,
        name='unsubscribe_url'),

)

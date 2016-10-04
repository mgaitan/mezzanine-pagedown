from django import VERSION

from .views import MarkupPreview


if VERSION[1] > 9:
    from django.conf.urls import url
    urlpatterns = (
        url(r'^preview/$', MarkupPreview.as_view(), name='preview'),
    )    
    
else:
    from django.conf.urls import patterns, url
    urlpatterns = patterns('',
        url(r'^preview/$', MarkupPreview.as_view(), name='preview'),
    )


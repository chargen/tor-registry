from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'userregistry.views.index'),
    url(r'^captcha/', include('captcha.urls')),
)

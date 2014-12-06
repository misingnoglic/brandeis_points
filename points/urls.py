__author__ = 'arya'
from django.conf.urls import patterns, url

from points import views

urlpatterns = patterns('',
    url(r'^points', views.get_meals, name='points'),
    )
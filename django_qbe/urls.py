# -*- coding: utf-8 -*-
try:
    from django.urls import path, re_path
except ImportError:
    # Backward compatibility for Django prior to 1.6
    from django.conf.urls.defaults import url
from django_qbe.exports import formats
from . import views

urlpatterns = [
    path('', views.qbe_form, name="qbe_form"),
    re_path(r'^qbe.js$', views.qbe_js, name="qbe_js"),
    path('bookmark/', views.qbe_bookmark, name="qbe_bookmark"),
    path('proxy/', views.qbe_proxy, name="qbe_proxy"),
    path('auto/', views.qbe_autocomplete, name="qbe_autocomplete"),
    re_path(r'^(?P<query_hash>(.*))/results\.(?P<format>(%s))$' % "|".join(formats.keys()), views.qbe_export, name="qbe_export"),
    re_path(r'^(?P<query_hash>(.*))/results/$', views.qbe_results, name="qbe_results"),
    re_path(r'^(?P<query_hash>(.*))/$', views.qbe_form, name="qbe_form"),
]

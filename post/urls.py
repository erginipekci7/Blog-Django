from django.conf.urls import url
from .views import * #bütün view leri icine aktardık
urlpatterns = [

    url(r'^index/$', post_index),
    url(r'^detail/$', post_detail),
    url(r'^create/$', post_create),
    url(r'^update/$', post_update),
    url(r'^delete/$', post_delete),
]

from django.conf.urls import url
from .views import * #bütün view leri icine aktardık
app_name = 'post'
urlpatterns = [

    url(r'^index/$', post_index, name='index'),
    url(r'^(?P<id>\d+)$', post_detail, name='detail'),
    url(r'^create/$', post_create, name='create'),
    url(r'^update/$', post_update, name='update'),
    url(r'^delete/$', post_delete, name='delete'),
]

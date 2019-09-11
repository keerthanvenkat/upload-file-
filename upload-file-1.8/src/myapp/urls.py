from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    'myapp.views',
    url(r'^list/$', 'list', name='list'),

    url(r'^test/', 'test', name='test'),
    url(r'^address/', 'address', name='address')
    # url(r'^address/','address.html', name='address'),
)
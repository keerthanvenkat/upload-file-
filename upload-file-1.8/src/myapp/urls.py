from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    'myapp.views',
    url(r'^list/$', 'list', name='list'),

    url(r'^test/', 'test_html', name='testhello'),
)
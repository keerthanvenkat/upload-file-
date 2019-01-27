from django.conf.urls import include, url
from django.contrib import admin
from django.url import path,re_path,include
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    # Examples:
    # url(r'^$', 'ShareFieWeb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    path('^admin/', include(admin.site.urls)),
    re_path("",include("sharefie.urls"))
] + [
    re_path('^media/(?P<path>.*$',serve, {'document_root':settings.MEDIA_ROOT}),
    re_path('^static/(?P<path>.*$',serve, {'document_root':settings.STATIC_ROOT})
]

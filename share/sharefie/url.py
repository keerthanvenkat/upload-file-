from django.urls import re_path
from .views import *

urlpattrens = [
    re_path(r'^uploadfiles/$',user_files_share),

]
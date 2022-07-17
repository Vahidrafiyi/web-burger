from django.urls import path, re_path
from .views import *

urlpatterns = [
    # user
    re_path(r'article/(?P<pk>[0-9]*)$', ShowArticle.as_view()),
    re_path(r'group/(?P<pk>[0-9]*)$', ShowArticle.as_view()),
    # admin
    re_path(r'admin/article/$', AdminArticle.as_view()),
    re_path(r'admin/article/(?P<pk>[0-9]+)$', AdminArticle.as_view()),
    re_path(r'admin/group/$', AdminGroup.as_view()),
    re_path(r'admin/group/(?P<pk>[0-9]+)$', AdminGroup.as_view()),
]

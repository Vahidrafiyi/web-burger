from django.urls import path, re_path
from .views import *

urlpatterns = [
    # user
    path('show_footer/', ShowFooter.as_view()),

    # admin
    re_path('admin/$', FooterAdmin.as_view()),
    re_path('admin/(?P<pk>[0-9]*)$', FooterAdmin.as_view()),
    re_path('admin/social/$', SocialMedia.as_view()),
    re_path('admin/socail/(?P<pk>[0-9]*)$', SocialMedia.as_view()),
]

from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('show_slider/', ShowSlider.as_view()),
    re_path(r'admin/$', SliderAdmin.as_view()),
    re_path(r'admin/(?P<pk>[0-9]+/$)', SliderAdmin.as_view()),
]

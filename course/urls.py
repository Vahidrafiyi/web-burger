from django.urls import path, re_path
from .views import *

urlpatterns = [
    # user
    path('show_course/', ShowCourse.as_view()),

    # admin
    re_path('admin/$', CourseAPI.as_view()),
    re_path('admin/(?P<pk>[0-9]*)$', CourseAPI.as_view()),
    re_path('admin/category/$', CourseCategoryAPI.as_view()),
    re_path('admin/category/(?P<pk>[0-9]*)$', CourseCategoryAPI.as_view()),
]

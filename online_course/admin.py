from django.contrib import admin
from online_course.models import OnlineCourse, Chapter, Episode,OnlineCourseCategory

admin.site.register(OnlineCourse)
admin.site.register(Chapter)
admin.site.register(Episode)
admin.site.register(OnlineCourseCategory)
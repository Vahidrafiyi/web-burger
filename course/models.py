import datetime

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django_jalali.db import models as jmodels


class CourseCategory(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Course(models.Model):
    class CourseLevel(models.TextChoices):
        BEGINNER = 'مبتدی'
        INTERMEDIATE = 'متوسط'
        PROFFESSIONAL = 'حرفه ای'

    class CourseStatus(models.TextChoices):
        PRE_REGISTRATION = 'پیش ثبت نام'
        RUNNING = 'در حال برگزاری'
        DONE = 'برگزار شده'

    title = models.CharField(max_length=120)
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, default=1)
    related_category = models.ManyToManyField(CourseCategory, related_name='rel_cat')
    description = models.TextField()
    info = models.TextField(default='', null=True, blank=True)
    prerequisites = models.TextField(default='', null=True, blank=True)
    targets = models.TextField(default='', null=True, blank=True)
    audience = models.TextField(default='', null=True, blank=True)
    image = models.ImageField(upload_to='store_image/courses_image/', null=True, blank=True)

    price = models.IntegerField(default=1)
    discount_percent = models.IntegerField(default=0)
    discounted_price = models.IntegerField(default=1)

    syllabus = models.TextField(default='', null=True, blank=True)
    file = models.FileField(upload_to='files/course_files/', default='', blank=True, null=True)
    level = models.CharField(max_length=100, choices=CourseLevel.choices, default=CourseLevel.BEGINNER)
    status = models.CharField(max_length=100, choices=CourseStatus.choices, default=CourseStatus.RUNNING)
    duration = models.DurationField(default=datetime.timedelta(hours=40))
    start_date = jmodels.jDateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.title




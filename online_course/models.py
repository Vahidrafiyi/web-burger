import datetime

from django.db import models



class OnlineCourseCategory(models.Model):
    category = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Online course categories'

    def __str__(self):
        return self.category


class OnlineCourse(models.Model):
    class CourseLevel(models.TextChoices):
        BEGINNER = 'مبتدی'
        INTERMEDIATE = 'متوسط'
        PROFFESSIONAL = 'حرفه ای'

    class CourseStatus(models.TextChoices):
        PRE_REGISTRATION = 'پیش ثبت نام'
        RUNNING = 'در حال برگزاری'
        DONE = 'برگزار شده'

    title = models.CharField(max_length=100, default='')
    category = models.ForeignKey(OnlineCourseCategory, on_delete=models.CASCADE, default=1)
    related_category = models.ManyToManyField(OnlineCourseCategory, related_name='online_rel_cat')
    price = models.IntegerField(default=1)
    discount_percent = models.IntegerField(default=0)
    discounted_price = models.IntegerField(default=1)
    teacher = models.ForeignKey("users.User", on_delete=models.PROTECT)
    description = models.TextField(default='')
    duration = models.DurationField(default=datetime.timedelta(days=2).total_seconds())
    image = models.ImageField(upload_to='images/', default='')
    number_of_videos = models.IntegerField(default=1)
    level = models.CharField(max_length=100, choices=CourseLevel.choices, default=CourseLevel.BEGINNER)
    status = models.CharField(max_length=100, choices=CourseStatus.choices, default=CourseStatus.RUNNING)
    start_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title





class Chapter(models.Model):
    chapter_order = models.IntegerField(default=1)
    chapter_title = models.CharField(max_length=100, default='')
    chapter_description = models.TextField(default='')
    chapter_duration = models.TimeField(default='')
    number_of_episode = models.IntegerField(default=1)
    related_to_online_course = models.ForeignKey(OnlineCourse, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.chapter_title


class Episode(models.Model):
    episode_order = models.IntegerField(default=1)
    episode_title = models.CharField(max_length=100, default='')
    episode_description = models.TextField(default='')
    episode_duration = models.TimeField(default='')
    related_to_chapter = models.ManyToManyField(Chapter)

    def __str__(self):
        return self.episode_title

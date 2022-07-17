import datetime

from django.db import models
from django_jalali.db import models as jmodels

from online_course.models import OnlineCourse
from ticket.utils import create_new_number
from users.models import User


class Ticket(models.Model):
    TICKET_TO = [
        ('INTERNAL_MANAGER', 'مدیر داخلی'),
        ('GENERAL_MANAGER', 'مدیر اصلی'),
        ('TEACHER', 'مدرس'),
        ('FINANCIAL', 'امور مالی'),
        ('TECHNICAL ISSUES', 'مشکلات فنی')
    ]
    COURSE = [
        ('ONLINE COURSE', 'دوره ی مجازی'),
        ('COURSE', 'دوره ی حضوری'),
    ]
    STATUS = [
        ('OPEN', 'باز'),
        ('CLOSED', 'بسته'),
        ('ANSWERD', 'پاسخ داده شده'),
        ('FINISHED', 'پایان یافته'),
        ('IN PROGRESS', 'درحال بررسی'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    identical = models.CharField(max_length=10, editable=False, unique=True, default=create_new_number)
    department = models.CharField(max_length=100, choices=TICKET_TO, default=TICKET_TO[0])
    what_course = models.CharField(max_length=100, choices=COURSE, default=COURSE[0])
    ticket_title = models.CharField(max_length=100, default='')
    ticket_file = models.FileField(upload_to='files/ticket_files/', default='', null=True, blank=True)
    ticket_status = models.CharField(max_length=100, choices=STATUS, default=STATUS[0])
    created_at = jmodels.jDateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.ticket_title + '/ code: ' + str(self.identical)


class TicketMessage(models.Model):
    message = models.TextField(blank=True)
    ticket_id = models.ForeignKey(Ticket, to_field='identical', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.ticket_id)

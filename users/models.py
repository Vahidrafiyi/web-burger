import datetime
import random
import string
import uuid
from datetime import timedelta
from jalali_date import datetime2jalali
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django_jalali.db import models as jmodels
from online_course.models import OnlineCourse
from .sender import send_otp


# Create your models here.
class User(AbstractUser):
    pass


# 8
class OtpRequestQuerySet(models.QuerySet):
    def is_valid(self, receiver, request, password):
        current_time = timezone.now()
        return self.filter(
            receiver=receiver,
            request_id=request,
            password=password,
            created__lt=current_time,
            created__gt=current_time - timedelta(seconds=120)
        ).exists()


# 3 third this one
class OTPManager(models.Manager):

    # 7
    def get_queryset(self):
        return OtpRequestQuerySet(self.model, self._db)

    # 6
    def is_valid(self, receiver, request, password):
        return self.get_queryset().is_valid(receiver, request, password)

    # 4 fourth this one
    def generate(self, data):
        otp = self.model(channel=data['channel'], receiver=data['receiver'])
        otp.save(using=self._db)
        send_otp(otp)
        return otp


# 2 second this
def generate_otp():
    rand = random.SystemRandom()
    digits = rand.choices(string.digits, k=4)
    return ''.join(digits)


# 1 first this one
class OTPRequest(models.Model):
    class OtpChannel(models.TextChoices):
        PHONE = 'Phone'
        EMAIL = 'E_Mail'

    request_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    channel = models.CharField(max_length=10, choices=OtpChannel.choices, default=OtpChannel.PHONE)
    receiver = models.CharField(max_length=50)
    password = models.CharField(max_length=4, default=generate_otp)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    # 5 fifth
    objects = OTPManager()


# ------------------------------------PROFILE---------------------------------------------#


class Profile(models.Model):
    class UserRole(models.TextChoices):
        ADMIN = 'admin'
        TEACHER = 'teacher'
        STUDENT = 'student'

    class Gender(models.TextChoices):
        MALE = 'male'
        FEMALE = 'female'

    show_user_info = models.BooleanField(default=True)
    profile_image = models.ImageField(upload_to='store_image/profile_image', null=True, blank=True)
    code_melli = models.CharField(max_length=10, default='1234567890')
    gender = models.CharField(max_length=10, choices=Gender.choices, default=Gender.MALE)
    user_role = models.CharField(max_length=10, choices=UserRole.choices, default=UserRole.STUDENT)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    online_course = models.ManyToManyField("online_course.OnlineCourse", blank=True)
    course = models.ManyToManyField("course.Course", blank=True)
    biography = models.TextField(default="جایی برای معرفی خودتان...", null=True, blank=True)
    registration_date = jmodels.jDateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + ' ' + self.user.username

    def datetime_to_jalali(self):
        return datetime2jalali(self.registration_date)


from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import OnlineCourse


@receiver(pre_save, sender=OnlineCourse)
def calculate_online_course_discounted_price(sender, **kwargs):
    online_course = kwargs['instance']
    online_course.online_course_discounted_price = float(online_course.online_course_price) - (
            float(online_course.online_course_price) * float(online_course.online_course_discount_percent) / 100)

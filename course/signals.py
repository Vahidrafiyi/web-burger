from django.db.models.signals import pre_save
from django.dispatch import receiver

from course.models import Course


@receiver(pre_save, sender=Course)
def calculate_course_discounted_price(sender, **kwargs):
    course = kwargs['instance']
    course.course_discounted_price = float(course.course_price) - (
            float(course.course_price) * float(course.course_discount_percent) / 100)

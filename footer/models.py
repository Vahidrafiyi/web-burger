from datetime import datetime

from django.db import models


class Social(models.Model):
    image = models.ImageField(upload_to='store_image/social-media')
    alt = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Social media'
        verbose_name_plural = 'Social media'


class Footer(models.Model):
    address = models.TextField()
    email = models.EmailField()
    phone = models.IntegerField()
    social_media = models.ForeignKey(Social, on_delete=models.CASCADE)

    def __str__(self):
        return self.email

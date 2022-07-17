from datetime import datetime

from django.db import models


# Create your models here.

class MenuCategory(models.Model):
    title = models.CharField(max_length=120)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Menu Categories'

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    title = models.CharField(max_length=120)
    order = models.IntegerField(default=0)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Menu(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

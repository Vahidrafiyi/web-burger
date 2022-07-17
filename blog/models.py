from users.models import User
from django.db import models
from django_jalali.db import models as jmodels


class ArticleGroup(models.Model):
    title = models.CharField(max_length=64)
    image = models.ImageField(upload_to='store_image/articles-group')
    alt = models.CharField(max_length=64, default='alt')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.alt = self.title
        super(ArticleGroup, self).save(*args, **kwargs)


class Article(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    alt = models.TextField(default='')
    image = models.ImageField(upload_to='store_image/blog_image/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(ArticleGroup, on_delete=models.CASCADE)
    created_at = jmodels.jDateTimeField(auto_now_add=True)
    updated_at= jmodels.jDateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.alt = self.title
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        return self.title

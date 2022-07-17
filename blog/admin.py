from django.contrib import admin
from django.contrib.admin import register

from .models import ArticleGroup, Article


@register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')


@register(ArticleGroup)
class ArticleGroupAdmin(admin.ModelAdmin):
    list_display = ('title',)

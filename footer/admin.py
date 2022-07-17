from django.contrib import admin
from django.contrib.admin import register

from .models import Footer, Social

@register(Footer)
class AdminFooter(admin.ModelAdmin):
    fields = ('title', 'category__title', 'start_date')

@register(Social)
class AdminSocial(admin.ModelAdmin):
    fields = ('title', 'category__title', 'start_date')
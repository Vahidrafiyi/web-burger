from django.contrib import admin
from django.contrib.admin import register
from certification.models import Certification


@register(Certification)
class AdminCertification(admin.ModelAdmin):
    fields = ('user', 'code_fani', 'code_academy', 'fani_score', 'date')
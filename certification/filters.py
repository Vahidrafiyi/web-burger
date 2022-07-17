import django_filters
from django_filters import DateFilter,CharFilter

from .models import *

class CertificateFilter(django_filters.FilterSet):

    course_title_fani = CharFilter(field_name="course_title_fani",lookup_expr='icontains')

    class Meta:
        model = Certification
        fields = '__all__'
        exclude = ['code_academy','certificate_image_fani','certificate_image_academy','course','user']
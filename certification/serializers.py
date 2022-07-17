from rest_framework import serializers

from certification.models import *


class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = ['id', 'course_title_fani', 'code_fani', 'code_academy', 'certificate_image_academy',
                  'certificate_image_fani', 'fani_score', 'academy_score', 'online_course', 'course', 'user']
        depth = 1

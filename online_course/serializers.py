from rest_framework import serializers
from online_course.models import OnlineCourse, Chapter, Episode

class OnlineCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineCourse
        fields = '__all__'

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'
        depth = 1


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = '__all__'
        depth = 2

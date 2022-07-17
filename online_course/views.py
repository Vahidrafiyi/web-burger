from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from online_course.models import OnlineCourse, Chapter, Episode
from online_course.serializers import OnlineCourseSerializer, ChapterSerializer, EpisodeSerializer


class OnlineCourseView(APIView):
    def get(self, request):
        query = OnlineCourse.objects.all()
        serializer = OnlineCourseSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = OnlineCourseSerializer(data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OnlineCourseViewSet(viewsets.ModelViewSet):
    queryset = OnlineCourse.objects.all()
    serializer_class = OnlineCourseSerializer


class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer


class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

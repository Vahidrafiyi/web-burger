from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Course, CourseCategory
from .serializers import CourseSerializer, CourseCategorySerializer


# ____________________________USER___________________________
class ShowCourse(APIView):
    def get(self, request):
        query = Course.objects.all()
        serializers = CourseSerializer(query, many=True, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)

class ShowCourseCategory(APIView):
    def get(self, request):
        query = CourseCategory.objects.all()
        serializers = CourseCategorySerializer(query, many=True, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)


# ____________________________ADMIN___________________________
class CourseAPI(APIView):
    def get(self, request):
        query = Course.objects.all()
        serializers = CourseSerializer(query, many=True, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializers = CourseSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        query = Course.objects.get(pk=pk)
        serializer = CourseSerializer(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        query = Course.objects.get(pk=pk)
        query.delete()
        return Response(status=204)

class CourseCategoryAPI(APIView):
    def get(self, request):
        query = CourseCategory.objects.all()
        serializers = CourseCategorySerializer(query, many=True, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializers = CourseCategorySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        query = CourseCategory.objects.get(pk=pk)
        serializer = CourseCategorySerializer(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        query = CourseCategory.objects.get(pk=pk)
        query.delete()
        return Response(status=204)

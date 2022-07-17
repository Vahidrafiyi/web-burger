from django.db.models import Q
from django_filters import NumberFilter
from django_filters import rest_framework as filters
from rest_framework import status, generics
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.permissions import IsSuperAdmin
from certification.serializers import *
from .filters import *

# ____________________________________USER_______________________________
class CertificateView(viewsets.ModelViewSet):
    serializer_class = CertificationSerializer

    def get_queryset(self):
        certificate = Certification.objects.all()
        return certificate


class CertificateApi(APIView):
    def get(self, request, pk):
        query = Certification.objects.get(user_id=pk)
        print(query)
        serializers = CertificationSerializer(query)
        print(serializers.data)
        return Response(serializers.data, status=status.HTTP_200_OK)


class CertificateEditApi(APIView):
    def patch(self, request, pk):
        certificate_obj = Certification.objects.get(user_id=pk)
        data = request.data

        certificate_obj.certificate_image_fani = data.get("certificate_image_fani",
                                                          certificate_obj.certificate_image_fani)
        certificate_obj.certificate_image_academy = data.get("certificate_image_academy",
                                                             certificate_obj.certificate_image_academy)
        certificate_obj.fani_score = data.get("fani_score", certificate_obj.fani_score)
        certificate_obj.academy_score = data.get("fani_score", certificate_obj.academy_score)

        certificate_obj.save()
        serializers = CertificationSerializer(certificate_obj)
        return Response(serializers.data, status=status.HTTP_201_CREATED)


class CertificateSearch(APIView):
    def get(self, request):
        search = request.GET['search']
        query = Certification.objects.filter(course_title_fani__contains=search)
        serializers = CertificationSerializer(query, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class CertificateSearchAll(APIView):
    def get(self, request):
        search = request.GET['search']
        query = Certification.objects.filter(
            Q(course=search) | Q(online_course=search) | Q(course_title_fani=search) | Q(code_fani=search) | Q(
                fani_score=search) | Q(academy_score=search))
        serializers = CertificationSerializer(query, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class CertificateFilterSearch(APIView):
    def get(self, request):
        query = Certification.objects.all()
        myFilter = CertificateFilter(request.GET, queryset=query)
        print(myFilter)
        serializers = CertificationSerializer(myFilter, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


# class UserListView(generics.ListAPIView):
#     queryset = Certificate.objects.all()
#     serializer_class = CertificateSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['course_title_fani', 'user__username']

class CertificateFilter(filters.FilterSet):
    min_fani_score = NumberFilter(field_name='fani_score', lookup_expr='gte')
    max_fani_score = NumberFilter(field_name='fani_score', lookup_expr='lte')

    class Meta:
        model = Certification
        fields = ('online_course', 'course')


class CertificateList(generics.ListCreateAPIView):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer
    name = 'certificate_list'

    # filter_fields = ('course_title_fani')
    filter_class = CertificateFilter

    search_fields = ('course_title_fani', 'fani_score')
    ordering_fields = ('fani_score', 'academy_score')

# ____________________________________ADMIN_______________________________
class AdminCertification(APIView):
    permission_classes = (IsAdminUser, IsSuperAdmin)

    def get(self, request):
        query = Certification.objects.all()
        serializer = CertificationSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CertificationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        query = Certification.objects.get(pk=pk)
        serializer = CertificationSerializer(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors, status=400)

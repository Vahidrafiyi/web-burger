from rest_framework import status
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article, ArticleGroup
from .permissions import IsSuperAdmin
from .serializers import ArticleSerializer, ArticleGroupSerializer


# ______________________________USER_______________________________________
class ShowArticle(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        query = Article.objects.all().order_by('created')
        serializers = ArticleSerializer(query, many=True, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)


class ShowArticlesGroup(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk):
        if len(pk) == 0:
            query = ArticleGroup.objects.all()
        else:
            query = ArticleGroup.objects.filter(pk=pk)
        serializer = ArticleGroupSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=200)


# ______________________________ADMIN_______________________________________
class AdminArticle(APIView):
    permission_classes = (IsAdminUser, IsSuperAdmin)

    def get(self, request):
        query = Article.objects.all().order_by('created')
        serializers = ArticleSerializer(query, many=True, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializers = ArticleSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        query = Article.objects.get(pk=pk)
        serializer = ArticleSerializer(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        query = Article.objects.get(pk=pk)
        query.delete()
        return Response(status=204)


class AdminGroup(APIView):
    permission_classes = (IsAdminUser, IsSuperAdmin)

    def get(self, request):
        query = ArticleGroup.objects.all()
        serializer = ArticleGroupSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ArticleGroupSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        query = ArticleGroup.objects.get(pk=pk)
        serializer = ArticleGroupSerializer(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        query = ArticleGroup.objects.get(pk=pk)
        query.delete()
        return Response(status=204)

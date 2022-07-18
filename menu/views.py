from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.permissions import IsSuperAdmin
from .serializers import *


class MenuCategoryView(viewsets.ModelViewSet):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer


class MenuItemView(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


# _______________________________________ADMIN_______________________________
class MenuCategory(APIView):
    permission_classes = [IsAdminUser, IsSuperAdmin]

    def get(self, request):
        query = MenuCategory.objects.all()
        serializers = MenuCategorySerializer(query, many=True, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializers = MenuCategorySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        query = MenuCategory.objects.get(pk=pk)
        serializer = MenuCategorySerializer(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        query = MenuCategory.objects.get(pk=pk)
        query.delete()
        return Response(status=204)


class MenuItems(APIView):
    def get(self, request):
        query = MenuItem.objects.all()
        serializers = MenuItemSerializer(query, many=True, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializers = MenuItemSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            query = MenuItem.objects.get(pk=pk)
            serializer = MenuItemSerializer(query, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=202)
            return Response(serializer.errors, status=400)
        except:
            data = {'error':'something went wrong!!'}
            return Response(data, status=400)

    def delete(self, request, pk):
        query = MenuItem.objects.get(pk=pk)
        query.delete()
        return Response(status=204)


class MenuList(viewsets.ModelViewSet):
    queryset = Menu.objects.filter(parent__isnull=True)
    serializer_class = MenuSerializer

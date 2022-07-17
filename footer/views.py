from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Footer, Social
from .serializers import FooterSerializer, SocialSerializer


# ________________________USER__________________________________
class ShowFooter(APIView):
    def get(self, request):
        query = Footer.objects.all()
        serializers = FooterSerializer(query, many=True, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)


# ________________________ADMIN__________________________________
class FooterAdmin(APIView):
    def get(self, request):
        query = Footer.objects.all()
        serializers = FooterSerializer(query, many=True, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializers = FooterSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        query = Footer.objects.get(pk=pk)
        serializer = FooterSerializer(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        query = Footer.objects.get(pk=pk)
        query.delete()
        return Response(status=204)


class SocialMedia(APIView):
    def get(self, request):
        query = Social.objects.all()
        serializers = SocialSerializer(query, many=True, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializers = SocialSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        query = Social.objects.get(pk=pk)
        serializer = SocialSerializer(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        query = Social.objects.get(pk=pk)
        query.delete()
        return Response(status=204)

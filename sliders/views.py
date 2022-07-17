from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Slider
from .serializers import SliderSerializer


# ________________________USER_____________________________________________
class ShowSlider(APIView):
    def get(self, request):
        query = Slider.objects.all()
        serializers = SliderSerializer(query, many=True, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)


# __________________________________________ADMIN_____________________________________________
class SliderAdmin(APIView):
    def get(self, request):
        query = Slider.objects.all()
        serializers = SliderSerializer(query, many=True, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializers = SliderSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        query = Slider.objects.get(pk=pk)
        serializer = SliderSerializer(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        query = Slider.objects.get(pk=pk)
        query.delete()
        return Response(status=204)

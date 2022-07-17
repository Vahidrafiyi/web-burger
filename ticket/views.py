from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ticket.models import Ticket, TicketMessage
from ticket.serializers import TicketSerializer, TicketMessageSerializer


# API for users
class TicketUser(generics.ListCreateAPIView):
    serializer_class = TicketSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        tickets = Ticket.objects.filter(user=user.id)
        return tickets


# API for Tickets
class TicketAdmin(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (IsAuthenticated,)


class CustomTicket(APIView):
    def get(self, request, pk):
        query = Ticket.objects.get(identical=pk)
        serializer = TicketSerializer(query)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SendTicket(APIView):
    def post(self, request):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# API for Ticket Messages
class GetAllTicketMessage(APIView):
    def get(self, request):
        query = TicketMessage.objects.all()
        serialzier = TicketMessageSerializer(query, many=True)
        return Response(serialzier.data, status=status.HTTP_200_OK)


class CustomTicketMessage(APIView):
    def get(self, request, pk):
        query = TicketMessage.objects.filter(ticket_id=pk)
        serializer = TicketMessageSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SendTicketMessage(APIView):
    def post(self, request):
        serializer = TicketMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

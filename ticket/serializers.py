import django_filters
from rest_framework import serializers

from ticket.models import Ticket, TicketMessage


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class TicketMessageFilter(django_filters.FilterSet):
    class Meta:
        model = TicketMessage
        fields = ['ticket_id__identical']


class TicketMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketMessage
        fields = ['ticket_id', 'message']

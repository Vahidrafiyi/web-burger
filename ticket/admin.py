from django.contrib import admin
from ticket.models import Ticket, TicketMessage
# Register your models here.
admin.site.register(Ticket)
admin.site.register(TicketMessage)
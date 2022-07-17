from django.urls import path

from ticket.views import CustomTicket, SendTicket, GetAllTicketMessage, CustomTicketMessage, \
    SendTicketMessage, TicketUser, TicketAdmin

urlpatterns = [
    # API for Tickets
    path('user/', TicketUser.as_view()),
    # path('custom_ticket/<int:pk>', CustomTicket.as_view()),
    # path('send_ticket', SendTicket.as_view()),
    # API for Ticket Messages
    path('admin/', TicketAdmin.as_view()),
    path('custom_message/<int:pk>', CustomTicketMessage.as_view()),
    path('send_message', SendTicketMessage.as_view()),
]

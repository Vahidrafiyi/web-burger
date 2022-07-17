from django.db.models.signals import post_save
from django.dispatch import receiver

from ticket.models import Ticket, TicketMessage


@receiver(post_save, sender=Ticket)
def create_update_ticket(sender, instance, **kwargs):
    if instance:
        TicketMessage.objects.create(message='Type SomeThing', ticket_id=instance)

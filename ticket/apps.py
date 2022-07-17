from django.apps import AppConfig


class TickConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ticket'
    def ready(self):
        import ticket.signals

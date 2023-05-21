from django.db.models.signals import post_migrate
from django.dispatch import receiver
from app.models import Settings

@receiver(post_migrate)
def create_website(sender, **kwargs):
    if Settings.objects.count() == 0:
        Settings.objects.create()
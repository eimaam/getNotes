from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.conf import settings
import os

User = get_user_model()
@receiver(post_save, sender=User)
def create_folder(sender, instance, created, **kwargs):
    if created:
        os.makedirs(f"{settings.MEDIA_ROOT}{os.sep}{instance.username}")
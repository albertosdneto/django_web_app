from django.db.models.signals import post_save # Fires a signal when something is created
from django.contrib.auth.models import User
from django.dispatch import receiver # Gets the signal from first line and execute some action
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
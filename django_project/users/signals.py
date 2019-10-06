from django.contrib.auth import get_user_model
from django.db.models.signals import post_save  # Fires a signal when something is created
from django.dispatch import receiver  # Gets the signal from first line and execute some action

from .models import Profile


# https://docs.djangoproject.com/en/2.2/topics/auth/customizing/#referencing-the-user-model
User = get_user_model()  # pylint: disable=invalid-name


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

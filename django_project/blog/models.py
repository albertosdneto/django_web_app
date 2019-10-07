from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse


# https://docs.djangoproject.com/en/2.2/topics/auth/customizing/#referencing-the-user-model
User = get_user_model()  # pylint: disable=invalid-name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    excerpt = models.TextField(
        max_length=150, default='Click at the title for more details.')
    tags = models.CharField(max_length=100, default='tags')
    published = models.BooleanField(default=True)
    date_posted = models.DateTimeField(default=timezone.now)
    # https://docs.djangoproject.com/en/2.2/topics/auth/customizing/#referencing-the-user-model
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

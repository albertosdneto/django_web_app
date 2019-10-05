from django.conf import settings
from django.db import models
from PIL import Image


class Profile(models.Model):
    # https://docs.djangoproject.com/en/2.2/topics/auth/customizing/#referencing-the-user-model
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # Tente mantenha a mesma assinatura do método que você está sobrescrevendo.
    # Altere a assinatura somente se for intencional.
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        super().save(force_insert, force_update,
                     using, update_fields)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

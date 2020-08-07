from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField('Image', upload_to='user_images', null=True, blank=True)
    bio = models.TextField('Bio', null=True, blank=True)

    @property
    def avatar(self):
        if self.image:
            return self.image.url
        return 'https://icon-library.com/images/facebook-user-icon/facebook-user-icon-17.jpg'
    
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField('Image', upload_to='user_images', null=True, blank=True)
    bio = models.TextField('Bio', null=True, blank=True)
    
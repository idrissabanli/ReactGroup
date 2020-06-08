from django.db import models

class Recipe(models.Model):
    
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/recipes/')
    short_description = models.TextField(max_length=1000)
    long_description = models.TextField()
    category = models.IntegerField(choices=((1, 'Dessert'), (2, 'Food')))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

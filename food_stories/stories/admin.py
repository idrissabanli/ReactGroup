from django.contrib import admin
from stories.models import Recipe, Author, Category
# Register your models here.

admin.site.register(Recipe)
admin.site.register([Author, Category])
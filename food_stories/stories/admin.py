from django.contrib import admin
from stories.models import Recipe, Author, Category, Contact
# Register your models here.

admin.site.register(Recipe)
admin.site.register([Author, Category, Contact])
from django.contrib import admin
from books.models import Category, Author, Book


admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Book)

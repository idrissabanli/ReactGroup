from django.contrib import admin
from stories.models import Recipe, Author, Category, Contact
# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'created_at', )
    ordering = ('title',)
    search_fields = ('title', 'category__title', 'author__description',)
    list_filter = ('category__title', 'author__full_name',)
    # readonly_fields = ('title','category',)
    fieldsets = (
        ('Relations', {
            'description': 'This for relations',
            'fields': ('category', 'author')
        }),
        ('Informations', {
            # 'classes': ('collapse',),
            'description': 'This for information',
            'fields': ('title', 'image', 'short_description', 'long_description'),
        }),
    )


admin.site.register(Recipe, RecipeAdmin)
admin.site.register([Author, Category, Contact])
from django.contrib import admin
from stories.models import Recipe, Category, Contact, Story, About, Tag, Subscriber, Comment
from stories.forms import RecipeForm
# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    form = RecipeForm
    list_display = ('title', 'category', 'author', 'created_at', )
    ordering = ('title',)
    search_fields = ('title', 'category__title', 'author__description',)
    list_filter = ('category__title', 'author__username',)
    # readonly_fields = ('title','category',)
    fieldsets = (
        ('Relations', {
            'description': 'This for relations',
            'fields': ('category', 'author', 'tags',)
        }),
        ('Informations', {
            # 'classes': ('collapse',),
            'description': 'This for information',
            'fields': ('title', 'image', 'short_description', 'long_description'),
        }),
    )

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'parent_comment', 'recipe', 'story', 'created_at',)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Story)
admin.site.register(Comment, CommentAdmin)
admin.site.register([Category, Contact, About, Tag, Subscriber])
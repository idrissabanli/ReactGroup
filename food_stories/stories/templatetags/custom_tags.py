from django.template import Library
from stories.models import About, Story, Recipe
from django.contrib.auth import get_user_model


User = get_user_model()

register = Library()

@register.simple_tag
def get_about_info():
    return About.objects.last()

@register.simple_tag
def get_data_informations():
    data = {
        'story_count': Story.objects.count(),
        'recipe_count': Recipe.objects.count(),
        'user_count': User.objects.count(),
    }
    return data
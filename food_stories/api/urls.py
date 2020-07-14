from django.urls import path
from api.views import recipes, recipe_detail

app_name = 'api'

urlpatterns = [
    path('recipes/', recipes, name='recipes'),
    path('recipes/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
]
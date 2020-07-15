from django.urls import path
from api.views import recipes, recipe_detail, registration, CustomAuthToken
from rest_framework.authtoken.views import obtain_auth_token
from api.routers import router 

app_name = 'api'

urlpatterns = [
    path('recipes/', recipes, name='recipes'),
    path('recipes/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    path('register/', registration, name='registration'),
    path('login/', CustomAuthToken.as_view(), name='api_login'),
] + router.urls
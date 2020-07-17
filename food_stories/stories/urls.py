from django.urls import path
from stories.views import test, ContactView, RecipeList, RecipeDetail, AboutView, \
    StoryList, dump, SubscribeView, Home


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('test/', test, name='test'),
    path('recipes/', RecipeList.as_view(), name="recipes"),
    path('stories/', StoryList.as_view(), name="stories"),
    path('recipe-detail/<int:pk>/', RecipeDetail.as_view(), name="recipe-detail"),
    path('contact/', ContactView.as_view(), name='contact'),
    path('dump/', dump, name='dump'),
    path('subscribe/', SubscribeView.as_view(), name='subscribe')
]
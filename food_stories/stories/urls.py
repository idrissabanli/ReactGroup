from django.urls import path
from stories.views import test, ContactView, RecipeList, RecipeDetail, AboutView, \
        StoryList, dump, SubscribeView, Home, UserProfile, CreateStory, CreateRecipe, RecipeUpdateView, \
        RecipeDeleteView


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('test/', test, name='test'),
    path('recipes/', RecipeList.as_view(), name="recipes"),
    path('create-story/', CreateStory.as_view(), name="create_story"),
    path('create-recipe/', CreateRecipe.as_view(), name="create_recipe"),
    path('update-recipe/<int:pk>/', RecipeUpdateView.as_view(), name="update_recipe"),
    path('delete-recipe/<int:pk>/', RecipeDeleteView.as_view(), name="delete_recipe"),
    path('stories/', StoryList.as_view(), name="stories"),
    path('recipe-detail/<int:pk>/', RecipeDetail.as_view(), name="recipe-detail"),
    path('contact/', ContactView.as_view(), name='contact'),
    path('dump/', dump, name='dump'),
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
    path('user-profile/', UserProfile.as_view(), name='user-profile'),
]
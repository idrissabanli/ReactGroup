from django.urls import path
from stories.views import home, test, ContactView, RecipeList, RecipeDetail, AboutView


urlpatterns = [
    path('', home, name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('test/', test, name='test'),
    path('recipes/', RecipeList.as_view(), name="recipes"),
    path('recipe-detail/<int:pk>/', RecipeDetail.as_view(), name="recipe-detail"),
    path('contact/', ContactView.as_view(), name='contact'),
]
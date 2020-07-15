from rest_framework.routers import DefaultRouter
from api.viewsets import StoryViewSet

router = DefaultRouter()

router.register('stories', StoryViewSet)
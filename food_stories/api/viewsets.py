from rest_framework.viewsets import ModelViewSet
from stories.models import Story
from api.serializers import StorySerializer
from rest_framework.permissions import IsAuthenticated

class IsAuthenticatedForCreate(IsAuthenticated):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return super().has_permission(request, view)


class StoryViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedForCreate,)
    serializer_class = StorySerializer
    queryset = Story.objects.all()
from rest_framework.viewsets import ModelViewSet
from stories.models import Story
from api.serializers import StorySerializer, StoryReadSerializer
from rest_framework.permissions import IsAuthenticated

class IsAuthenticatedForCreate(IsAuthenticated):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return super().has_permission(request, view)


class StoryViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedForCreate,)
    # serializer_class = StorySerializer
    serializer_classes = {
        'list': StoryReadSerializer,
        'retrieve': StoryReadSerializer,
        'default': StorySerializer,
        # 'create': StorySerializer,
        # 'update': StorySerializer,
        # 'partial_update': StorySerializer,
        # 'delete': StorySerializer
    }
    queryset = Story.objects.all()

    def get_serializer_class(self):
        print(self.action)
        return self.serializer_classes.get(self.action, self.serializer_classes.get('default'))
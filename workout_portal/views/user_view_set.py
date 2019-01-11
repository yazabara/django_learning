from rest_framework import viewsets

from workout_portal.models import SimpleUser
from workout_portal.serializers.user_serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SimpleUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    pagination_class = None

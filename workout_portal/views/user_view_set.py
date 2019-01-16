from rest_framework import viewsets

from workout_portal.serializers.user_serializer import UserSerializer
from workout_portal.service.user_service import user_service


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = user_service.list()
    serializer_class = UserSerializer
    pagination_class = None

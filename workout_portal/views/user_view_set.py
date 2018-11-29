from rest_framework import viewsets

from serializers.user_serializer import UserSerializer
from service.user_service import user_service


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = user_service.list_users()
    serializer_class = UserSerializer

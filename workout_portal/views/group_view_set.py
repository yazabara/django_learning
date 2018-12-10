from rest_framework import viewsets

from workout_portal.serializers.group_serializer import GroupSerializer
from workout_portal.service.group_service import group_service


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = group_service.list_groups()
    serializer_class = GroupSerializer

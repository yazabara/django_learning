from rest_framework import viewsets

from serializers.group_serializer import GroupSerializer
from service.group_service import group_service


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = group_service.list_groups()
    serializer_class = GroupSerializer

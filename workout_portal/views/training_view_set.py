from rest_framework import viewsets

from workout_portal.serializers.training_serializer import TrainingSerializer
from workout_portal.service.training_service import training_service


class TrainingViewSet(viewsets.ModelViewSet):
    queryset = training_service.list()
    serializer_class = TrainingSerializer

from rest_framework import viewsets

from workout_portal.serializers.training_serializer import TrainingSerializer
from workout_portal.service.training_service import training_service


class TrainingViewSet(viewsets.ModelViewSet):
    queryset = training_service.list()
    serializer_class = TrainingSerializer

    # def retrieve(self, request, pk=None):
    #     return training_service.get_by_id(training_id=pk)

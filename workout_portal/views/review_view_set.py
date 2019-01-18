from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from workout_portal.serializers.review_serializer import ReviewSerializer
from workout_portal.service.review_service import review_service


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = review_service.list_reviews()
    serializer_class = ReviewSerializer

    def list(self, request, **kwargs):
        queryset = review_service.list_reviews()
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, name="Get review for entity")
    def get_by_entity_id_and_type(self, request):
        queryset = review_service.get_by_entity_id_and_type(request.query_params["entity_id"],
                                                            request.query_params["entity_type"])
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data)

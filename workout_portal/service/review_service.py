from workout_portal.models import Review


class ReviewService(object):

    @staticmethod
    def get_by_entity_id_and_type(entity_id, entity_type):
        return Review.objects.order_by("-publication_date").filter(entity_id=entity_id, entity_type=entity_type)

    @staticmethod
    def list_reviews():
        return Review.objects.all()


review_service = ReviewService()

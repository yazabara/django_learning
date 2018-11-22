from workout_portal.models import Training


class TrainingService(object):
    # singleton instance
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(TrainingService)
        return cls._instance

    @staticmethod
    def create_new(user_id, name, date):
        return Training.objects.create(user_id=user_id, name=name, date=date)

    @staticmethod
    def list(limit=5):
        return Training.objects.order_by('date')[0:limit]

    @staticmethod
    def get_by_id(training_id):
        return Training.objects.get(pk=training_id)

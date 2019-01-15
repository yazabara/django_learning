from workout_portal.models import Training


class TrainingService(object):
    @staticmethod
    def create_new(user_id, name, date):
        return Training.objects.create(user_id=user_id, name=name, date=date)

    @staticmethod
    def list():
        trainings = Training.objects.all()
        return trainings

    @staticmethod
    def get_by_id(training_id):
        return Training.objects.get(pk=training_id)


training_service = TrainingService()

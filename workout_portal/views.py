import uuid

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.utils.datetime_safe import datetime

from service.training_service import TrainingService
from workout_portal.models import Training


class Views(object):

    def __init__(self) -> None:
        super().__init__()
        self.training_service = TrainingService()

    def index(self, request):
        last_trainings = self.training_service.list(limit=5)
        return render(request, 'index.html', {'last_trainings': last_trainings})

    def add_training(self, request):
        # TODO remove hardcode
        self.training_service.create_new(1, uuid.uuid4(), datetime.now())
        return HttpResponseRedirect("/workout/training/1")

    def get_training(self, request, training_id):
        try:
            training = self.training_service.get_by_id(training_id=training_id)
        except Training.DoesNotExist:
            raise Http404("Training does not exist")
        return render(request, 'training-detail.html', {'training': training})

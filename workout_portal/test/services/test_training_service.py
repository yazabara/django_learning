from unittest.mock import patch

from django.test import TestCase
from django.utils import timezone

from workout_portal.service.training_service import training_service


class TrainingServiceTest(TestCase):

    def setUp(self):
        self.patcher = patch('workout_portal.models.Training.objects')
        self.mocked_training_model = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_should_call_create_on_model_when_create_new_training(self):
        training_service.create_new(user_id=None, name='name', date=timezone.now())
        self.mocked_training_model.create.assert_called_once()

    def test_should_call_create_on_model_when_create_new_training_with_specified_params(self):
        current_date = timezone.now()
        training_service.create_new(user_id=None, name='name', date=current_date)
        self.mocked_training_model.create.assert_called_with(user_id=None, name='name', date=current_date)

    def test_should_call_list_with_order_by_date(self):
        training_service.list()
        self.mocked_training_model.order_by.assert_called_with('date')

    def test_should_get_with_specified_training_id(self):
        training_id = 1
        training_service.get_by_id(training_id)
        self.mocked_training_model.get.assert_called_with(pk=training_id)

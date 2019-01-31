from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory

from workout_portal.models import Training
from workout_portal.test.data.builders.exercise_image_builder import ExerciseImageBuilder
from workout_portal.test.data.builders.exercise_video_builder import ExerciseVideoBuilder
from workout_portal.test.data.builders.simple_user_builder import SimpleUserBuilder
from workout_portal.test.data.builders.training_builder import TrainingBuilder
from workout_portal.views.training_view_set import TrainingViewSet
from workout_portal.views.view_sets_actions import ViewSetsActions

TRAININGS_URL = '/api/trainings/'


class TrainingViewSetTest(TestCase):
    fixtures = ['test/trainings.json', 'workout_portal/fixtures/test/users.json']

    def setUp(self):
        self.simple_user = SimpleUserBuilder().build()
        self.simple_user.save()
        self.exercise_video = ExerciseVideoBuilder().build()
        self.exercise_video.save()
        self.exercise_image = ExerciseImageBuilder().build()
        self.exercise_image.save()

    def test_should_successful_getting_list_of_trainings(self):
        request = APIRequestFactory().get(TRAININGS_URL)
        training_view_set = TrainingViewSet.as_view(ViewSetsActions.GET_LIST)
        response = training_view_set(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_should_list_should_contains_all_trainings(self):
        request = APIRequestFactory().get(TRAININGS_URL)
        training_view_set = TrainingViewSet.as_view(ViewSetsActions.GET_LIST)
        response = training_view_set(request)
        self.assertEqual(len(Training.objects.all()), response.data['count'])

    def test_should_successful_getting_training_by_id(self):
        request = APIRequestFactory().get(TRAININGS_URL)
        training_view_set = TrainingViewSet.as_view(ViewSetsActions.RETRIEVE)
        response = training_view_set(request, pk=1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_should_unsuccessful_creating_training(self):
        request_params = {'name': 'test training',
                          'date': '2019-01-16T07:55:21.526Z',
                          'user': {
                              "password": "pb",
                              "last_login": "",
                              "is_superuser": 1,
                              "username": "joe",
                              "first_name": "",
                              "last_name": "",
                              "email": "joe@example.com",
                              "is_staff": 1,
                              "is_active": 1,
                              "date_joined": "2019-01-31 18:19:44.799979",
                              "telephone": "213",
                              "profile_img": '',
                              "profile_url": "asd"
                          }}
        request = APIRequestFactory().post(TRAININGS_URL, request_params, format='json')
        training_view_set = TrainingViewSet.as_view(ViewSetsActions.CREATE)
        response = training_view_set(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIsNotNone(Training.objects.filter(name='test training'))

    def test_should_successful_partial_update_Training(self):
        created_training = TrainingBuilder(self.simple_user, self.exercise_image, self.exercise_video,
                                           name='not partial updated Training name yet').build()
        request_params = {'name': 'partial updated Training name'}
        request = APIRequestFactory().patch(TRAININGS_URL, request_params)
        training_view_set = TrainingViewSet.as_view(ViewSetsActions.PARTIAL_UPDATE)
        response = training_view_set(request, pk=created_training.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(Training.objects.filter(name='partial updated Training name'))

    def test_should_successful_deleting_training(self):
        created_training = TrainingBuilder(self.simple_user, self.exercise_image, self.exercise_video,
                                           name='not deleted Training yet').build()
        request = APIRequestFactory().delete(TRAININGS_URL)
        training_view_set = TrainingViewSet.as_view(ViewSetsActions.DELETE)
        response = training_view_set(request, pk=created_training.pk)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(Training.objects.filter(name='not deleted Training yet')), 0)

from datetime import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase

from workout_portal.models import Exercise, Training, SimpleUser, ExerciseVideo, ExerciseImage


class ExerciseTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        simple_user = SimpleUser.objects.create(profile_url='x', username="username", password="password",
                                                telephone=79040029933, profile_img="/images/img.png")
        exercise_video = ExerciseVideo.objects.create(name="exercise_video_name", video="/video.mkv")
        exercise_image = ExerciseImage.objects.create(name="exercise_image_name", image="/image.jpg")
        cls.training = Training.objects.create(name="name2", date=datetime.now(), user=simple_user,
                                               image_gallery=exercise_image, video_gallery=exercise_video)

    def test_exercise_name_can_not_be_more_than_255_characters(self):
        incorrect_length = 256
        exercise = Exercise(
            # incorrect field
            name='x' * incorrect_length,
            # correct fields
            description="description", training=self.training
        )
        self.assertRaises(ValidationError, exercise.full_clean)

    def test_exercise_description_can_not_be_more_than_1000_characters(self):
        incorrect_length = 1001
        exercise = Exercise(
            # incorrect field
            description="d" * incorrect_length,
            # correct fields
            name="name", training=self.training
        )
        self.assertRaises(ValidationError, exercise.full_clean)

    def test_exercise_has_relation_with_training(self):
        Exercise.objects.create(name="exc_name", description="description", training=self.training)
        self.assertEqual(Exercise.objects.filter(training__name="name2").count(), 1)

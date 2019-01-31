from django.core.exceptions import ValidationError
from django.test import TestCase

from workout_portal.models import Exercise
from workout_portal.test.data.builders.exercise_builder import ExerciseBuilder
from workout_portal.test.data.builders.exercise_image_builder import ExerciseImageBuilder
from workout_portal.test.data.builders.exercise_video_builder import ExerciseVideoBuilder
from workout_portal.test.data.builders.simple_user_builder import SimpleUserBuilder
from workout_portal.test.data.builders.training_builder import TrainingBuilder


class ExerciseTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        simple_user = SimpleUserBuilder().build()
        simple_user.save()
        exercise_video = ExerciseVideoBuilder().build()
        exercise_video.save()
        exercise_image = ExerciseImageBuilder().build()
        exercise_image.save()
        cls.training = TrainingBuilder(simple_user, exercise_image, exercise_video).build()

    def test_exercise_name_can_not_be_more_than_255_characters(self):
        incorrect_length = 256
        exercise = ExerciseBuilder(self.training,
                                   # incorrect field
                                   name='x' * incorrect_length).build()
        self.assertRaises(ValidationError, exercise.full_clean)

    def test_exercise_description_can_not_be_more_than_1000_characters(self):
        incorrect_length = 1001
        exercise = ExerciseBuilder(self.training,
                                   # incorrect field
                                   description="d" * incorrect_length, ).build()
        self.assertRaises(ValidationError, exercise.full_clean)

    def test_exercise_has_relation_with_training(self):
        ExerciseBuilder(self.training).build().save()
        self.assertEqual(Exercise.objects.filter(training__pk=self.training.pk).count(), 1)

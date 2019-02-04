from django.core.exceptions import ValidationError
from django.test import TestCase

from workout_portal.models import WorkoutSet
from workout_portal.test.data.builders.exercise_builder import ExerciseBuilder
from workout_portal.test.data.builders.exercise_image_builder import ExerciseImageBuilder
from workout_portal.test.data.builders.exercise_video_builder import ExerciseVideoBuilder
from workout_portal.test.data.builders.simple_user_builder import SimpleUserBuilder
from workout_portal.test.data.builders.training_builder import TrainingBuilder
from workout_portal.test.data.builders.workout_set_builder import WorkoutSetBuilder


class WorkoutSetTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        simple_user = SimpleUserBuilder().build()
        simple_user.save()
        exercise_video = ExerciseVideoBuilder().build()
        exercise_video.save()
        exercise_image = ExerciseImageBuilder().build()
        exercise_image.save()
        training = TrainingBuilder(simple_user, exercise_image, exercise_video).build()
        cls.exercise = ExerciseBuilder(training).build()
        cls.exercise.save()

    def test_workout_set_additional_can_not_be_more_than_1000_characters(self):
        incorrect_length = 1001
        workout_set = WorkoutSetBuilder(self.exercise, additional="a" * incorrect_length).build()
        self.assertRaises(ValidationError, workout_set.full_clean)

    def test_workout_set_has_relation_with_exercise(self):
        WorkoutSetBuilder(self.exercise).build().save()
        self.assertEqual(WorkoutSet.objects.filter(exercise__pk=self.exercise.pk).count(), 1)

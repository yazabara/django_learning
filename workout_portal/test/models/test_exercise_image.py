from django.core.exceptions import ValidationError
from django.test import TestCase

from workout_portal.models import ExerciseImage
from workout_portal.test.data.builders.exercise_image_builder import ExerciseImageBuilder


class ExerciseImageTest(TestCase):

    def test_exercise_image_name_can_not_be_more_than_40_characters(self):
        incorrect_length = 41
        exercise_image = ExerciseImageBuilder(
            # incorrect field
            name='x' * incorrect_length
        ).build()
        self.assertRaises(ValidationError, exercise_image.full_clean)

    def test_exercise_image_verbose_name_should_be_empty(self):
        self.assertEqual(str(ExerciseImage._meta.get_field('image').verbose_name), '')

    def test_exercise_image_upload_to_should_not_be_empty(self):
        self.assertEqual(str(ExerciseImage._meta.get_field('image').upload_to), 'images/')

    def test_exercise_image_may_be_empty(self):
        exercise_image = ExerciseImage()
        self.assertFalse(bool(exercise_image.image))

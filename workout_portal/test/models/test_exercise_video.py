from django.core.exceptions import ValidationError
from django.test import TestCase

from workout_portal.models import ExerciseVideo
from workout_portal.test.data.builders.exercise_video_builder import ExerciseVideoBuilder


class ExerciseImageTest(TestCase):

    def test_exercise_video_name_can_not_be_more_than_40_characters(self):
        incorrect_length = 41
        exercise_video = ExerciseVideoBuilder(
            # incorrect field
            name='x' * incorrect_length).build()
        self.assertRaises(ValidationError, exercise_video.full_clean)

    def test_exercise_video_upload_to_should_not_be_empty(self):
        self.assertEqual(str(ExerciseVideo._meta.get_field('video').upload_to), 'video/')

    def test_exercise_video_may_be_empty(self):
        exercise_video = ExerciseVideo()
        self.assertFalse(bool(exercise_video.video))

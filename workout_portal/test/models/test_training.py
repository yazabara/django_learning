from django.core.exceptions import ValidationError
from django.test import TestCase

from workout_portal.models import Training
from workout_portal.test.data.builders.exercise_image_builder import ExerciseImageBuilder
from workout_portal.test.data.builders.exercise_video_builder import ExerciseVideoBuilder
from workout_portal.test.data.builders.simple_user_builder import SimpleUserBuilder
from workout_portal.test.data.builders.training_builder import TrainingBuilder


class TrainingTest(TestCase):

    def setUp(self):
        self.simple_user = SimpleUserBuilder().build()
        self.simple_user.save()
        self.exercise_video = ExerciseVideoBuilder().build()
        self.exercise_video.save()
        self.exercise_image = ExerciseImageBuilder().build()
        self.exercise_image.save()
        TrainingBuilder(self.simple_user, self.exercise_image, self.exercise_video).build().save()

    def test_training_name_can_not_be_more_than_255_characters(self):
        incorrect_length = 256
        training = TrainingBuilder(self.simple_user, self.exercise_image, self.exercise_video,
                                   # incorrect field
                                   name='x' * incorrect_length).build()
        self.assertRaises(ValidationError, training.full_clean)

    def test_training_has_relation_with_user(self):
        self.assertEqual(Training.objects.filter(user__pk=self.simple_user.pk).count(), 1)

    def test_training_has_relation_with_exercise_image(self):
        self.assertEqual(Training.objects.filter(image_gallery__pk=self.exercise_image.pk).count(), 1)

    def test_training_has_relation_with_exercise_video(self):
        self.assertEqual(Training.objects.filter(video_gallery__pk=self.exercise_video.pk).count(), 1)

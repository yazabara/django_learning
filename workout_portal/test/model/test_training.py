from datetime import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase

from workout_portal.models import Training, SimpleUser, ExerciseVideo, ExerciseImage


class TrainingTest(TestCase):

    def setUp(self):
        simple_user = SimpleUser.objects.create(profile_url='x', username="username", password="password",
                                                telephone=79040029933, profile_img="/images/img.png")
        exercise_video = ExerciseVideo.objects.create(name="exercise_video_name", video="/video.mkv")
        exercise_image = ExerciseImage.objects.create(name="exercise_image_name", image="/image.jpg")
        Training.objects.create(name="name", date=datetime.now(), user=simple_user, image_gallery=exercise_image,
                                video_gallery=exercise_video)

    def test_training_name_can_not_be_more_than_255_characters(self):
        incorrect_length = 256
        training = Training(
            # incorrect field
            name='x' * incorrect_length
        )
        self.assertRaises(ValidationError, training.full_clean)

    def test_training_has_relation_with_user(self):
        self.assertEqual(Training.objects.filter(user__username="username").count(), 1)

    def test_training_has_relation_with_exercise_image(self):
        self.assertEqual(Training.objects.filter(image_gallery__name="exercise_image_name").count(), 1)

    def test_training_has_relation_with_exercise_video(self):
        self.assertEqual(Training.objects.filter(video_gallery__name="exercise_video_name").count(), 1)

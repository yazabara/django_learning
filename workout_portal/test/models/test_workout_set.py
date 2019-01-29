from datetime import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase

from workout_portal.models import Training, SimpleUser, ExerciseVideo, ExerciseImage, WorkoutSet, Exercise


class WorkoutSetTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        simple_user = SimpleUser.objects.create(profile_url='x', username="username", password="password",
                                                telephone=79040029933, profile_img="/images/img.png")
        exercise_video = ExerciseVideo.objects.create(name="exercise_video_name", video="/video.mkv")
        exercise_image = ExerciseImage.objects.create(name="exercise_image_name", image="/image.jpg")
        training = Training.objects.create(name="name2", date=datetime.now(), user=simple_user,
                                           image_gallery=exercise_image, video_gallery=exercise_video)
        cls.exercise = Exercise.objects.create(name="exc_name", description="description", training=training)

    def test_workout_set_additional_can_not_be_more_than_1000_characters(self):
        incorrect_length = 1001
        workout_set = WorkoutSet(
            # incorrect field
            additional="a" * incorrect_length,
            # correct fields
            weight=100, repetitions=5, duration=1, exercise=self.exercise
        )
        self.assertRaises(ValidationError, workout_set.full_clean)

    def test_workout_set_has_relation_with_exercise(self):
        WorkoutSet.objects.create(additional="WorkoutSet additional", weight=100, repetitions=5, duration=1,
                                  exercise=self.exercise)
        self.assertEqual(WorkoutSet.objects.filter(exercise__name="exc_name").count(), 1)

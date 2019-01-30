from django.test import TestCase

from workout_portal.serializers.user_serializer import UserSerializer
from workout_portal.serializers.workout_serializer import WorkoutSetSerializer
from workout_portal.test.data.builders.exercise_builder import ExerciseBuilder
from workout_portal.test.data.builders.exercise_image_builder import ExerciseImageBuilder
from workout_portal.test.data.builders.exercise_video_builder import ExerciseVideoBuilder
from workout_portal.test.data.builders.simple_user_builder import SimpleUserBuilder
from workout_portal.test.data.builders.training_builder import TrainingBuilder
from workout_portal.test.data.builders.workout_set_builder import WorkoutSetBuilder


class WorkoutSetTest(TestCase):

    def setUp(self):
        self.valid_serializer_data = {
            'id': '555',
            'weight': '105',
            'repetitions': '3',
            'duration': '1',
            'additional': 'additional text',
            'user': UserSerializer(
                instance=SimpleUserBuilder(username="username_of_user", profile_img=None).build()).data
        }

        simple_user = SimpleUserBuilder().build()
        simple_user.save()
        exercise_video = ExerciseVideoBuilder().build()
        exercise_video.save()
        exercise_image = ExerciseImageBuilder().build()
        exercise_image.save()
        training = TrainingBuilder(simple_user, exercise_image, exercise_video).build()
        exercise = ExerciseBuilder(training).build()
        exercise.save()

        self.workout_set = WorkoutSetBuilder(exercise).build()
        self.serializer = WorkoutSetSerializer(instance=self.workout_set)
        self.deserializer = WorkoutSetSerializer(data=self.valid_serializer_data)

    def test_contains_expected_fields_when_serialize(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {'id', 'weight', 'repetitions', 'duration', 'additional'})

    def test_equality_id_fields_when_serialize(self):
        data = self.serializer.data
        self.assertEqual(data['id'], self.workout_set.id)

    def test_equality_weight_fields_when_serialize(self):
        data = self.serializer.data
        self.assertEqual(data['weight'], self.workout_set.weight)

    def test_equality_repetitions_fields_when_serialize(self):
        data = self.serializer.data
        self.assertEqual(data['repetitions'], self.workout_set.repetitions)

    def test_equality_duration_fields_when_serialize(self):
        data = self.serializer.data
        self.assertEqual(data['duration'], self.workout_set.duration)

    def test_equality_additional_fields_when_serialize(self):
        data = self.serializer.data
        self.assertEqual(data['additional'], self.workout_set.additional)

    def test_valid_data_when_deserialize(self):
        self.assertTrue(self.deserializer.is_valid())

    def test_equality_weight_fields_when_deserialize(self):
        self.deserializer.is_valid()
        self.assertEqual(self.deserializer.validated_data.get('weight'), float(self.valid_serializer_data['weight']))

    def test_equality_repetitions_fields_when_deserialize(self):
        self.deserializer.is_valid()
        self.assertEqual(self.deserializer.validated_data.get('repetitions'),
                         int(self.valid_serializer_data['repetitions']))

    def test_equality_duration_fields_when_deserialize(self):
        self.deserializer.is_valid()
        self.assertEqual(self.deserializer.validated_data.get('duration'), int(self.valid_serializer_data['duration']))

    def test_equality_additional_fields_when_deserialize(self):
        self.deserializer.is_valid()
        self.assertEqual(self.deserializer.validated_data.get('additional'), self.valid_serializer_data['additional'])

from django.test import TestCase

from workout_portal.serializers.exercise_serializer import ExerciseSerializer
from workout_portal.test.data.builders.exercise_builder import ExerciseBuilder
from workout_portal.test.data.builders.exercise_image_builder import ExerciseImageBuilder
from workout_portal.test.data.builders.exercise_video_builder import ExerciseVideoBuilder
from workout_portal.test.data.builders.simple_user_builder import SimpleUserBuilder
from workout_portal.test.data.builders.training_builder import TrainingBuilder


class ExerciseSerializerTest(TestCase):

    def setUp(self):
        self.valid_serializer_data = {
            'id': '2',
            'name': 'exercise',
            'description': 'exercise description'
        }

        simple_user = SimpleUserBuilder().build()
        simple_user.save()
        exercise_video = ExerciseVideoBuilder().build()
        exercise_video.save()
        exercise_image = ExerciseImageBuilder().build()
        exercise_image.save()
        training = TrainingBuilder(simple_user, exercise_image, exercise_video).build()

        self.exercise = ExerciseBuilder(training).build()
        self.serializer = ExerciseSerializer(instance=self.exercise)
        self.deserializer = ExerciseSerializer(data=self.valid_serializer_data)

    def test_contains_expected_fields_when_serialize(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {'id', 'name', 'description', 'workouts'})

    def test_equality_id_fields_when_serialize(self):
        data = self.serializer.data
        self.assertEqual(data['id'], self.exercise.id)

    def test_equality_name_fields_when_serialize(self):
        data = self.serializer.data
        self.assertEqual(data['name'], self.exercise.name)

    def test_equality_description_fields_when_serialize(self):
        data = self.serializer.data
        self.assertEqual(data['description'], self.exercise.description)

    def test_valid_data_when_deserialize(self):
        self.assertTrue(self.deserializer.is_valid())

    def test_equality_name_fields_when_deserialize(self):
        self.deserializer.is_valid()
        self.assertEqual(self.deserializer.validated_data.get('name'), self.valid_serializer_data['name'])

    def test_equality_description_fields_when_deserialize(self):
        self.deserializer.is_valid()
        self.assertEqual(self.deserializer.validated_data.get('description'), self.valid_serializer_data['description'])

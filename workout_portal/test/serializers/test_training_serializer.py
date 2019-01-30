from django.test import TestCase
from django.utils import timezone

from workout_portal.serializers.training_serializer import TrainingSerializer
from workout_portal.serializers.user_serializer import UserSerializer
from workout_portal.test.data.builders.exercise_image_builder import ExerciseImageBuilder
from workout_portal.test.data.builders.exercise_video_builder import ExerciseVideoBuilder
from workout_portal.test.data.builders.simple_user_builder import SimpleUserBuilder
from workout_portal.test.data.builders.training_builder import TrainingBuilder


class TrainingSerializerTest(TestCase):

    def setUp(self):
        self.valid_serializer_data = {
            'id': '555',
            'name': 'training name',
            'date': timezone.now(),
            'user': UserSerializer(instance=SimpleUserBuilder(username="username_1", profile_img=None).build()).data
        }

        simple_user = SimpleUserBuilder().build()
        simple_user.save()
        exercise_video = ExerciseVideoBuilder().build()
        exercise_video.save()
        exercise_image = ExerciseImageBuilder().build()
        exercise_image.save()
        self.training = TrainingBuilder(simple_user, exercise_image, exercise_video, date=timezone.now()).build()
        self.serializer = TrainingSerializer(instance=self.training)
        self.deserializer = TrainingSerializer(data=self.valid_serializer_data)

    def test_contains_expected_fields_when_serialize(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {'id', 'name', 'date', 'user', 'exercises'})

    def test_equality_id_fields_when_serialize(self):
        data = self.serializer.data
        self.assertEqual(data['id'], self.training.id)

    def test_equality_name_fields_when_serialize(self):
        data = self.serializer.data
        self.assertEqual(data['name'], self.training.name)

    def test_valid_data_when_deserialize(self):
        self.assertTrue(self.deserializer.is_valid())

    def test_equality_name_fields_when_deserialize(self):
        self.deserializer.is_valid()
        self.assertEqual(self.deserializer.validated_data.get('name'), self.valid_serializer_data['name'])

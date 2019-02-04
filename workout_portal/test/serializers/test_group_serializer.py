from django.contrib.auth.models import Group
from django.test import TestCase
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

from workout_portal.serializers.group_serializer import GroupSerializer


class GroupSerializerTest(TestCase):

    def setUp(self):
        self.valid_serializer_data = {
            'url': 'group url',
            'name': 'group name'
        }
        self.group = Group()
        factory = APIRequestFactory()
        request = factory.get('/')
        serializer_context = {
            'request': Request(request),
        }
        self.serializer = GroupSerializer(instance=self.group, context={'request': serializer_context})
        self.deserializer = GroupSerializer(data=self.valid_serializer_data)

    def test_contains_expected_fields_when_serialize(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {'url', 'name'})

    def test_equality_name_fields_when_serialize(self):
        data = self.serializer.data
        self.assertEqual(data['name'], self.group.name)

    def test_valid_data_when_deserialize(self):
        self.assertTrue(self.deserializer.is_valid())

    def test_equality_name_fields_when_deserialize(self):
        self.deserializer.is_valid()
        self.assertEqual(self.deserializer.validated_data.get('name'), self.valid_serializer_data['name'])

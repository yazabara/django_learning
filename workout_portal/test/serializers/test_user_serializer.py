from django.test import TestCase

from workout_portal.serializers.user_serializer import UserSerializer
from workout_portal.test.data.builders.simple_user_builder import SimpleUserBuilder


class UserSerializerTest(TestCase):

    def setUp(self):
        self.simple_user = SimpleUserBuilder().build()
        self.serializer = UserSerializer(instance=self.simple_user)

    def test_contains_expected_fields_when_serialize(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()),
                         {'id', 'profile_img', 'username', 'email', 'groups', 'profile_url', 'telephone'})

    def test_equality_id_fields_when_serialize(self):
        data = self.serializer.data
        self.assertEqual(data['id'], self.simple_user.id)

    def test_equality_profile_img_fields_when_serialize(self):
        data = self.serializer.data
        self.assertEqual(data['profile_img'], self.simple_user.profile_img.url)

    def test_equality_username_fields_when_serialize(self):
        data = self.serializer.data
        self.assertEqual(data['username'], self.simple_user.username)

    def test_equality_email_fields_when_serialize(self):
        data = self.serializer.data
        self.assertEqual(data['email'], self.simple_user.email)

    def test_equality_profile_url_fields_when_serialize(self):
        data = self.serializer.data
        self.assertEqual(data['profile_url'], self.simple_user.profile_url)

    def test_equality_telephone_fields_when_serialize(self):
        data = self.serializer.data
        self.assertEqual(data['telephone'], self.simple_user.telephone)

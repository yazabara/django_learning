import unittest

from django.test import TestCase

from workout_portal.models import SimpleUser
from workout_portal.test.data.builders.simple_user_builder import SimpleUserBuilder


class SimpleUserTest(TestCase):

    def test_telephone_may_be_nullable(self):
        simple_user = SimpleUser()
        self.assertIsNone(simple_user.telephone)

    def test_profile_img_may_be_empty(self):
        simple_user = SimpleUser()
        self.assertFalse(bool(simple_user.profile_img))

    @unittest.expectedFailure
    def test_profile_url_can_not_be_more_than_255_characters(self):
        incorrect_length = 256
        simple_user = SimpleUserBuilder(
            # incorrect field
            profile_url='x' * incorrect_length).build()
        simple_user.full_clean()

    def test_profile_img_upload_to_should_not_be_empty(self):
        self.assertEqual(str(SimpleUser._meta.get_field('profile_img').upload_to), 'profile/')

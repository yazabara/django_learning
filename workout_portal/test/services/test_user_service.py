from unittest import mock

from django.test import TestCase

from workout_portal.service.user_service import user_service


class UserServiceTest(TestCase):

    @mock.patch('workout_portal.models.SimpleUser.objects.all')
    def test_should_call_list_once(self, mocked_simple_user_model):
        user_service.list()
        mocked_simple_user_model.assert_called_once()

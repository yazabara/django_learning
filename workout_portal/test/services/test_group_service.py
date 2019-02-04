from unittest import mock

from django.contrib.auth.models import Group
from django.test import TestCase

from workout_portal.service.group_service import group_service

GROUPS_COUNT = 7


class GroupServiceTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.groups = []
        for x in range(0, GROUPS_COUNT):
            cls.groups.append(Group())

    @mock.patch('django.contrib.auth.models.Group.objects.all')
    def test_should_return_all_groups(self, mocked_group_all):
        mocked_group_all.return_value = self.groups
        groups = group_service.list_groups()
        self.assertEquals(len(groups), GROUPS_COUNT)

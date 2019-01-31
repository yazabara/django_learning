from django.contrib.auth.models import Group
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory

from workout_portal.views.group_view_set import GroupViewSet
from workout_portal.views.view_sets_actions import ViewSetsActions

GROUPS_URL = '/groups/'


class GroupViewSetTest(TestCase):
    fixtures = ['test/groups.json']

    def test_should_successful_getting_list_of_groups(self):
        request = APIRequestFactory().get(GROUPS_URL)
        group_view_set = GroupViewSet.as_view(ViewSetsActions.GET_LIST)
        response = group_view_set(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_should_list_should_contains_all_groups(self):
        request = APIRequestFactory().get(GROUPS_URL)
        group_view_set = GroupViewSet.as_view(ViewSetsActions.GET_LIST)
        response = group_view_set(request)
        self.assertEqual(len(Group.objects.all()), response.data['count'])

    def test_should_successful_getting_group_by_id(self):
        request = APIRequestFactory().get(GROUPS_URL)
        group_view_set = GroupViewSet.as_view(ViewSetsActions.RETRIEVE)
        response = group_view_set(request, pk=1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_should_successful_creating_group(self):
        request_params = {'name': 'test group'}
        request = APIRequestFactory().post(GROUPS_URL, request_params)
        group_view_set = GroupViewSet.as_view(ViewSetsActions.CREATE)
        response = group_view_set(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(Group.objects.filter(name='test group'))

    def test_should_successful_update_group(self):
        created_group = Group.objects.create(name='not updated group name yet')
        request_params = {'name': 'updated group name'}
        request = APIRequestFactory().put(GROUPS_URL, request_params)
        group_view_set = GroupViewSet.as_view(ViewSetsActions.UPDATE)
        response = group_view_set(request, pk=created_group.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(Group.objects.filter(name='updated group name'))

    def test_should_successful_partial_update_group(self):
        created_group = Group.objects.create(name='not partial updated group name yet')
        request_params = {'name': 'partial updated group name'}
        request = APIRequestFactory().patch(GROUPS_URL, request_params)
        group_view_set = GroupViewSet.as_view(ViewSetsActions.PARTIAL_UPDATE)
        response = group_view_set(request, pk=created_group.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(Group.objects.filter(name='partial updated group name'))

    def test_should_successful_deleting_group(self):
        created_group = Group.objects.create(name='not deleted group yet')
        request = APIRequestFactory().delete(GROUPS_URL)
        group_view_set = GroupViewSet.as_view(ViewSetsActions.DELETE)
        response = group_view_set(request, pk=created_group.pk)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(Group.objects.filter(name='not deleted group yet')), 0)

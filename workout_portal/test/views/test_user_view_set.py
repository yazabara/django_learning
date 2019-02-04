from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory

from workout_portal.models import SimpleUser
from workout_portal.views.user_view_set import UserViewSet
from workout_portal.views.view_sets_actions import ViewSetsActions

USERS_URL = '/users/'


class UserViewSetTest(TestCase):
    fixtures = ['test/users.json']

    def test_should_successful_getting_list_of_users(self):
        request = APIRequestFactory().get(USERS_URL)
        user_view_set = UserViewSet.as_view(ViewSetsActions.GET_LIST)
        response = user_view_set(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(SimpleUser.objects.all().count(), len(response.data))

    def test_should_list_should_contains_all_users(self):
        request = APIRequestFactory().get(USERS_URL)
        user_view_set = UserViewSet.as_view(ViewSetsActions.GET_LIST)
        response = user_view_set(request)
        self.assertEqual(SimpleUser.objects.all().count(), len(response.data))

    def test_should_successful_getting_user_by_id(self):
        request = APIRequestFactory().get(USERS_URL)
        user_view_set = UserViewSet.as_view(ViewSetsActions.RETRIEVE)
        response = user_view_set(request, pk=1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_should_successful_creating_user(self):
        request_params = {
            'profile_img': [],
            'username': 'test_user',
            'email': 'email@email.com',
            'groups': [],
            'profile_url': 'url',
            'telephone': '1232'}
        request = APIRequestFactory().post(USERS_URL, request_params)
        user_view_set = UserViewSet.as_view(ViewSetsActions.CREATE)
        response = user_view_set(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(SimpleUser.objects.filter(username='test_user'))

    def test_should_successful_update_user(self):
        created_user = SimpleUser.objects.create(username='not_updated_username_yet', profile_img=[],
                                                 email='email@email.com', profile_url='url', telephone=444)
        payload = {
            'profile_img': [],
            'username': 'updated_username',
            'email': 'email@email.com',
            'groups': [],
            'profile_url': 'url_updated',
            'telephone': '8888'}
        request = APIRequestFactory().put(USERS_URL, payload)
        user_view_set = UserViewSet.as_view(ViewSetsActions.UPDATE)
        response = user_view_set(request, pk=created_user.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(SimpleUser.objects.filter(username='updated_username'))

    def test_should_successful_partial_update_user(self):
        created_user = SimpleUser.objects.create(username='not_partial_updated_username_yet', profile_img=[],
                                                 email='email@email.com', profile_url='url', telephone=34234)
        payload = {'username': 'partial_updated_user_name'}
        request = APIRequestFactory().patch(USERS_URL, payload)
        user_view_set = UserViewSet.as_view(ViewSetsActions.PARTIAL_UPDATE)
        response = user_view_set(request, pk=created_user.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(SimpleUser.objects.filter(username='partial_updated_user_name'))

    def test_should_successful_deleting_user(self):
        created_user = SimpleUser.objects.create(username='not_deleted_user_yet')
        request = APIRequestFactory().delete(USERS_URL)
        user_view_set = UserViewSet.as_view(ViewSetsActions.DELETE)
        response = user_view_set(request, pk=created_user.pk)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(SimpleUser.objects.filter(username='not_deleted_user_yet')), 0)

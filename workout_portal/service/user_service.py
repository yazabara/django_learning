from django.contrib.auth.models import User


class UserService(object):

    @staticmethod
    def list(limit=5):
        return User.objects.all().order_by('-date_joined')[0:limit]


user_service = UserService()

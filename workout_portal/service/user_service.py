from workout_portal.models import SimpleUser


class UserService(object):

    @staticmethod
    def list(limit=5):
        return SimpleUser.objects.all().order_by('-date_joined')[0:limit]


user_service = UserService()

from workout_portal.models import SimpleUser


class UserService(object):

    @staticmethod
    def list():
        return SimpleUser.objects.all().order_by('-date_joined')


user_service = UserService()

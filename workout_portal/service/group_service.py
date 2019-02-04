from django.contrib.auth.models import Group


class GroupService(object):

    @staticmethod
    def list_groups():
        return Group.objects.all()


group_service = GroupService()

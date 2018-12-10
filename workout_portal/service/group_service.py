from django.contrib.auth.models import Group


class GroupService(object):

    @staticmethod
    def list_groups(limit=5):
        return Group.objects.all()[:limit]


group_service = GroupService()

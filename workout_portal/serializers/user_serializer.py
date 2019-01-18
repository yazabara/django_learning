from rest_framework import serializers

from workout_portal.models import SimpleUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SimpleUser
        fields = ('id', 'profile_img', 'username', 'email', 'groups', 'profile_url', 'telephone')

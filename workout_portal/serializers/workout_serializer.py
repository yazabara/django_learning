from rest_framework import serializers
from workout_portal.models import WorkoutSet


class WorkoutSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutSet
        fields = ('weight', 'repetitions', 'duration', 'additional')

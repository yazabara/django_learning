from rest_framework import serializers

from workout_portal.serializers.workout_serializer import WorkoutSetSerializer
from workout_portal.models import Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    workouts = WorkoutSetSerializer(many=True, read_only=True)

    class Meta:
        model = Exercise
        fields = ('name', 'description', 'workouts')

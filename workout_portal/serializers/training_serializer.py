from rest_framework import serializers

from serializers.exercise_serializer import ExerciseSerializer
from serializers.user_serializer import UserSerializer
from workout_portal.models import Training


class TrainingSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    exersizes = ExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = Training
        fields = ('name', 'date', 'user', 'exersizes')

from rest_framework import serializers

from models import Training


class TrainingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Training

    fields = ('name', 'date')

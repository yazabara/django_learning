from django.contrib.auth.models import User
from django.db import models


class Training(models.Model):
    """
    Model described one training for user. (name, date, exercises)
    """
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    # Foreign Key to User table
    user = models.ForeignKey(to=User, null=False, blank=False, on_delete=models.CASCADE)


class Exercise(models.Model):
    """
    Model described one training exercise (name, description, workout sets)
    """
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    # Foreign Key to Training table
    training = models.ForeignKey(to=Training, null=False, blank=False, on_delete=models.CASCADE)


class WorkoutSet(models.Model):
    """
    Model described one workout set (number of repetitions, duration of this set, weight etc)
    """
    weight = models.FloatField()
    repetitions = models.IntegerField()
    duration = models.IntegerField()
    additional = models.CharField(max_length=1000)
    # Foreign Key to Exercise table
    exercise = models.ForeignKey(to=Exercise, null=False, blank=False, on_delete=models.CASCADE)

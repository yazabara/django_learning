from django.contrib.auth.models import AbstractUser
from django.db import models


class ExerciseImage(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to='images/', null=True, verbose_name='')

    def __str__(self):
        return 'Image name {}, image data {}'.format(self.name, str(self.image))


class ExerciseVideo(models.Model):
    name = models.CharField(max_length=40)
    video = models.FileField(upload_to='video/', null=True)

    def __str__(self):
        return 'Video name {}, video data {}'.format(self.name, str(self.video))


class SimpleUser(AbstractUser):
    telephone = models.IntegerField(null=True)
    profile_img = models.ImageField(null=True, upload_to='profile/', storage='')
    profile_url = models.CharField(max_length=255)


class Training(models.Model):
    """
    Model described one training for user. (name, date, exercises)
    """
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    # Foreign Key to User table
    user = models.ForeignKey(to=SimpleUser, null=False, blank=False, on_delete=models.CASCADE)
    image_gallery = models.ForeignKey(to=ExerciseImage, null=True, on_delete=models.CASCADE, related_name='images')
    video_gallery = models.ForeignKey(to=ExerciseVideo, null=True, on_delete=models.CASCADE, related_name='videos')

    def __str__(self):
        return "Training: name {}, date {}, user {}".format(self.name,
                                                            self.date,
                                                            self.user)


class Exercise(models.Model):
    """
    Model described one training exercise (name, description, workout sets)
    """
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    # Foreign Key to Training table
    training = models.ForeignKey(to=Training, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return "Exercise: name {}, description {}, training {}".format(self.name,
                                                                       self.description,
                                                                       self.training)


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

    def __str__(self):
        return "Exercise: weight {}, repetitions {}, duration {}, additional {}, exercise {}".format(self.weight,
                                                                                                     self.repetitions,
                                                                                                     self.duration,
                                                                                                     self.additional,
                                                                                                     self.exercise)

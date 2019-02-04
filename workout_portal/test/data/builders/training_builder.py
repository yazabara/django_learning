from django.utils import timezone

from workout_portal.models import Training


class TrainingBuilder(object):

    def __init__(self, user, image_gallery, video_gallery, name="name", date=timezone.now()):
        self.user = user
        self.image_gallery = image_gallery
        self.video_gallery = video_gallery
        self.name = name
        self.date = date

    def build(self):
        return Training.objects.create(name=self.name, date=self.date, user=self.user, image_gallery=self.image_gallery,
                                       video_gallery=self.video_gallery)

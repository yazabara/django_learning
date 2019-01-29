from workout_portal.models import ExerciseVideo


class ExerciseVideoBuilder(object):

    def __init__(self, name="exercise_video_name", video="/video.mkv"):
        self.name = name
        self.video = video

    def build(self):
        return ExerciseVideo(name=self.name, video=self.video)

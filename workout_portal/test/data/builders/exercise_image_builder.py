from workout_portal.models import ExerciseImage


class ExerciseImageBuilder(object):

    def __init__(self, name="ExerciseImage name", image="/image.jpg"):
        self.name = name
        self.image = image

    def build(self):
        return ExerciseImage(name=self.name, image=self.image)

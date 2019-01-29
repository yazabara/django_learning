from workout_portal.models import Exercise


class ExerciseBuilder(object):

    def __init__(self, training, name="exc_name", description="description"):
        self.training = training
        self.name = name
        self.description = description

    def build(self):
        return Exercise(name=self.name, description=self.description, training=self.training)

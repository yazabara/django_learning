from workout_portal.models import WorkoutSet


class WorkoutSetBuilder(object):

    def __init__(self, exercise, additional="WorkoutSet additional", weight=100, repetitions=5, duration=1):
        self.exercise = exercise
        self.additional = additional
        self.weight = weight
        self.repetitions = repetitions
        self.duration = duration

    def build(self):
        return WorkoutSet.objects.create(additional=self.additional, weight=self.weight, repetitions=self.repetitions,
                                         duration=self.duration, exercise=self.exercise)

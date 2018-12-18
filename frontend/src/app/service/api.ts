import { Training, WorkoutSet, Exercise } from '../types';

export class Service {
    public static getTrainings(): Promise<Training[]> {
        return new Promise<Training[]>(function(resolve, reject) {
            resolve(this.trainings());
        });
    }

    private trainings(): Training[]{
        return Array.from(Array(10).keys()).map(element => {
            const name = `training ${element}`;
            return {
                name,
                date: new Date(),
                exercises: this.excercises(name)
            } as Training;
        });
    }

    private excercises(trainingName: string): Exercise[]{
        return Array.from(Array(10).keys()).map(element => {
            const name = `excercise-${trainingName} ${element}`;
            return {
                name,
                description: `description ${element}`,
                workout_sets: this.sets(name)
            } as Exercise;
        });
    }

    private sets(name: string): WorkoutSet[]{
        return Array.from(Array(20).keys()).map(element => {
            return {
                weight: element,
                repetitions: element + element,
                duration: element * element,
                additional: `${name}:${element}-${element + element}-${element * element}`
            } as WorkoutSet;
        });
    }
}
export interface Training {
    name: string;
    date: Date;
    exercises: Exercise[];
}

export interface Exercise {
    name: string;
    description: string;
    workoutSets: WorkoutSet[];
}

export interface WorkoutSet {
    weight: number;
    repetitions: number;
    duration: number;
    additional: string;
}

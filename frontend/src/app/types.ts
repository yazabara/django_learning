export interface Training {
    id: number;
    name: string;
    date: Date;
    isExpanded: boolean;
    exercises: Exercise[];
}

export interface Exercise {
    name: string;
    description: string;
    workoutSets: WorkoutSet[];
}

export interface WorkoutSet {
    id: number;
    weight: number;
    repetitions: number;
    duration: number;
    additional: string;
}

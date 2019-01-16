export interface Training {
    id: number;
    name: string;
    date: Date;
    isExpanded: boolean;
    exercises: Exercise[];
    user: User;
}

export interface User {
    url: string;
    username: string;
    email: string;
    groups: any[];
}

export interface Exercise {
    name: string;
    description: string;
    workouts: WorkoutSet[];
}

export interface WorkoutSet {
    id: number;
    weight: number;
    repetitions: number;
    duration: number;
    additional: string;
}

export interface TrainingsResponse extends ResponseBase {
    results: Training[];
}

interface ResponseBase {
    count: number;
    next: number;
    previous: number;
}

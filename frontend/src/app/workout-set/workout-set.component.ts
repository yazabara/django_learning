import { Component, OnInit, Input } from '@angular/core';
import { WorkoutSet } from '../types';

@Component({
  selector: 'app-workout-set',
  templateUrl: './workout-set.component.html',
  styleUrls: ['./workout-set.component.scss']
})
export class WorkoutSetComponent implements OnInit {
  @Input() workoutSet: WorkoutSet;
  constructor() { }

  ngOnInit() {
  }

}

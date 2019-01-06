import { Component, OnInit, Input } from '@angular/core';
import { WorkoutSet } from '../../types';

@Component({
  selector: 'app-workout-set-preview',
  templateUrl: './workout-set-preview.component.html',
  styleUrls: ['./workout-set-preview.component.scss']
})
export class WorkoutSetPreviewComponent implements OnInit {
  @Input() workoutSet: WorkoutSet;
  constructor() { }

  ngOnInit() {
  }

}

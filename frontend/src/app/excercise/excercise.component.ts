import { Component, OnInit, Input } from '@angular/core';
import { Exercise } from '../types';

@Component({
  selector: 'app-excercise',
  templateUrl: './excercise.component.html',
  styleUrls: ['./excercise.component.scss']
})
export class ExcerciseComponent implements OnInit {
  @Input() excercise: Exercise;
  constructor() { }

  ngOnInit() {
  }

}

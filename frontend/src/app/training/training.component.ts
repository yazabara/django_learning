import { Component, OnInit, Input } from '@angular/core';
import { Training } from '../types';

@Component({
  selector: 'app-training',
  templateUrl: './training.component.html',
  styleUrls: ['./training.component.scss']
})
export class TrainingComponent implements OnInit {
  @Input() training: Training;
  isExpanded: boolean;

  constructor() { }

  ngOnInit() {
  }

  onExpandClick(): void {
    console.log('onExpandClick');
    this.isExpanded = !this.isExpanded;
  }

}

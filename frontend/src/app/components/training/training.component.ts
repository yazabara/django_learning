import { Component, OnInit, Input } from '@angular/core';
import { Training } from '../../types';
import {EntityType} from "../../model/review/entity.type";

@Component({
  selector: 'app-training',
  templateUrl: './training.component.html',
  styleUrls: ['./training.component.scss']
})
export class TrainingComponent implements OnInit {
  @Input() training: Training;

  public entityTypes = EntityType;

  constructor() { }

  ngOnInit() {
  }

  onExpandClick(): void {
    console.log('onExpandClick');
    this.training.isExpanded = !this.training.isExpanded;
  }

}

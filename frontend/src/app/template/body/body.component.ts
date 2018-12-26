import { Component, OnInit } from '@angular/core';
import { Training } from '../types';
import { Service } from '../service/api';

@Component({
  selector: 'app-body',
  templateUrl: './body.component.html',
  styleUrls: ['./body.component.scss']
})
export class BodyComponent implements OnInit {

  trainings: Training[];

  constructor() { }

  async ngOnInit(): Promise<void> {
    this.trainings = await Service.getTrainings();
  }

}

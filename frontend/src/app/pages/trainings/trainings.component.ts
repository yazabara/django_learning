import { Component, OnInit } from '@angular/core';
import { Training } from '../../types';
import { Service } from '../../service/api';

@Component({
  selector: 'app-trainings',
  templateUrl: './trainings.component.html',
  styleUrls: ['./trainings.component.scss']
})
export class TrainingsComponent implements OnInit {

  trainings: Training[];

  constructor() { }

  async ngOnInit() {
    this.trainings = await Service.getTrainings();
  }

}

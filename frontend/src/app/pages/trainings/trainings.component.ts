import { Component, OnInit } from '@angular/core';
import { Training } from '../../types';
import { TrainingsService } from '../../services/trainings.service';

@Component({
  selector: 'app-trainings',
  templateUrl: './trainings.component.html',
  styleUrls: ['./trainings.component.scss']
})
export class TrainingsComponent implements OnInit {

  trainings: Training[];

  constructor(private trainingsService: TrainingsService) { }

  async ngOnInit() {
    this.trainings = await this.trainingsService.getTrainings();
  }

}

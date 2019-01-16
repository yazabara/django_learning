import { Component, OnInit, OnDestroy } from '@angular/core';
import { Training, TrainingsResponse } from '../../types';
import { TrainingsService } from '../../services/trainings.service';
import { getTrainings } from './pypes';
import { pipe, Subscription } from 'rxjs';

@Component({
  selector: 'app-trainings',
  templateUrl: './trainings.component.html',
  styleUrls: ['./trainings.component.scss']
})
export class TrainingsComponent implements OnInit, OnDestroy {

  trainings: Training[];
  trainingsSubscription: Subscription;

  constructor(private trainingsService: TrainingsService) { }

  ngOnInit() {
    this.loadTrainings();
  }

  ngOnDestroy() {
    if (this.trainingsSubscription) {
      this.trainingsSubscription.unsubscribe();
    }
  }

  loadTrainings() {
    this.trainingsSubscription = this.trainingsService.getTrainings()
      .subscribe(pipe(getTrainings, this.fillProperties.bind(this)));
  }

  fillProperties(response: TrainingsResponse): void {
    this.trainings = response.results;
  }
}

import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { WorkoutSetComponent } from './pages/workout-set/workout-set.component';
import { TrainingsComponent } from './pages/trainings/trainings.component';

const routes: Routes = [
  { path: '', component: TrainingsComponent },
  { path: 'wset', component: WorkoutSetComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

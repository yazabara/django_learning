import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './template/header/header.component';
import { FooterComponent } from './template/footer/footer.component';
import { BodyComponent } from './template/body/body.component';
import { WorkoutSetPreviewComponent } from './components/workout-set-preview/workout-set-preview.component';
import { ExcerciseComponent } from './components/excercise/excercise.component';
import { TrainingComponent } from './components/training/training.component';
import { ReviewComponent } from './components/review/review.component';
import { DateFormat } from './pipes/dateFormatter';
import { TrainingsComponent } from './pages/trainings/trainings.component';
import { WorkoutSetComponent } from './pages/workout-set/workout-set.component';
import { HttpClientModule } from "@angular/common/http";
import { AdminDataService } from "./service/admin-data.service";
import { AdminModule } from "./components/admin-page/admin.module";


@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    FooterComponent,
    BodyComponent,
    WorkoutSetPreviewComponent,
    ExcerciseComponent,
    TrainingComponent,
    ReviewComponent,
    DateFormat,
    TrainingsComponent,
    WorkoutSetComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    AdminModule,
    HttpClientModule
  ],
  providers: [
    AdminDataService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }

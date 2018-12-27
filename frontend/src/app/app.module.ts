import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './template/header/header.component';
import { FooterComponent } from './template/footer/footer.component';
import { BodyComponent } from './template/body/body.component';
import { WorkoutSetComponent } from './pages/training/workout-set/workout-set.component';
import { ExcerciseComponent } from './pages/training/excercise/excercise.component';
import { TrainingComponent } from './pages/training/training.component';
import { DateFormat } from './pipes/dateFormatter';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    FooterComponent,
    BodyComponent,
    WorkoutSetComponent,
    ExcerciseComponent,
    TrainingComponent,
    DateFormat
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

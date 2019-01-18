import { Injectable } from '@angular/core';
import { TrainingsResponse } from '../types';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { GET_TRAININGS } from './consts';
import { Observable } from 'rxjs';
import { handleError } from './helper';
import { catchError } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class TrainingsService {

  constructor(private http: HttpClient) { }

  public getTrainings(): Observable<TrainingsResponse> {
    return this.http.get<TrainingsResponse>(GET_TRAININGS).pipe(
      catchError(handleError)
    );
  }
}

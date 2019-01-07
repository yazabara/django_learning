import { Injectable } from '@angular/core';
import { Service } from './api';
import { Training } from '../types';

@Injectable({
  providedIn: 'root'
})
export class TrainingsService {

  constructor() { }

  public async getTrainings(): Promise<Training[]> {
    return Service.getTrainings();
  }
}

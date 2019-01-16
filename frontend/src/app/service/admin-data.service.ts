import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {shareReplay} from "rxjs/operators";
import {environment} from "../../environments/environment";

@Injectable({
  providedIn: 'root'
})
export class AdminDataService {
  usersApiUrl = environment.usersAPI;

  constructor(private http: HttpClient) {
  }

  getUsersList(): Observable<UserData.SimpleUser[]> {
    return this.http.get<UserData.SimpleUser[]>(this.usersApiUrl).pipe(shareReplay(1));
  }

  getUserById(id: string): Observable<UserData.SimpleUser> {
    return this.http.get<UserData.SimpleUser>(this.usersApiUrl + id).pipe(shareReplay(1))
  }

  saveNewUser(user: UserData.SimpleUser) {
    this.http.post(this.usersApiUrl, user)
  }

  deleteUserById(id: string) {
    this.http.delete(this.usersApiUrl + id)
  }
}

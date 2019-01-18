import {Injectable} from "@angular/core";
import {HttpClient, HttpParams} from "@angular/common/http";
import {Observable} from "rxjs";
import {Review} from "../model/review/review";
import {EntityType} from "../model/review/entity.type";
import {take} from "rxjs/operators";

@Injectable({
  providedIn: 'root'
})
export class ReviewService {

  private reviewApiUrl = "/api/reviews/";

  constructor(private http: HttpClient) {
  }

  public getReviewsByEntityIdAndType(entityId: number, entityType: EntityType): Observable<Review[]> {
    const params = new HttpParams()
      .set('entity_id', entityId.toString())
      .set('entity_type', entityType);
    const url = this.reviewApiUrl + "get_by_entity_id_and_type";
    return this.http.get<Review[]>(url, {params}).pipe(take(1));
  }

  public saveNewReview(review: Review): Observable<number> {
    return this.http.post<number>(this.reviewApiUrl, review).pipe(take(1))
  }

  public deleteReview(id: number): Observable<any> {
    return this.http.delete(this.reviewApiUrl + id.toString()).pipe(take(1));
  }
}

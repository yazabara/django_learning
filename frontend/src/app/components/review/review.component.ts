import {Component, Input, OnInit} from "@angular/core";
import {Review} from "../../model/review/review";
import {EntityType} from "../../model/review/entity.type";
import {ReviewService} from "../../services/review.service";

@Component({
  selector: 'review',
  templateUrl: './review.component.html',
  styleUrls: ['./review.component.scss']
})
export class ReviewComponent implements OnInit {

  @Input()
  public entityId: number;

  @Input()
  public entityType: EntityType;

  reviews: Review[] = [];

  private newReview: Review = null;

  constructor(private reviewService: ReviewService) {
  }

  ngOnInit(): void {
    if (this.entityId && this.entityType) {
      this.reviewService.getReviewsByEntityIdAndType(this.entityId, this.entityType).subscribe((reviews) =>
        this.reviews = reviews
      );
    }
  }

  public deleteReview(review: Review): void {
    this.reviewService.deleteReview(review.id).subscribe((result) => {
        const index = this.reviews.findIndex(item => item.id == review.id);
        if (index > -1) {
          this.reviews.splice(index, 1);
        }
      }
    )
  }

  public createNewReview(): void {
    this.newReview = {
      comment_text: "",
      entity_id: this.entityId,
      entity_type: this.entityType,
      id: null,
      publication_date: null
    } as Review
  }

  public saveReview(): void {
    this.newReview.publication_date = new Date();
    this.reviewService.saveNewReview(this.newReview).subscribe((savedId) => {
        this.newReview.id = savedId;
        this.reviews.push(Object.assign({}, this.newReview));
        this.newReview = null;
      }
    );
  }

  public cancel(): void {
    this.newReview = null;
  }

  public doTextareaValueChange(event): void {
      this.newReview.comment_text = event.target.value;
  }

}

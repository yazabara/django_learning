import {EntityType} from "./entity.type";

export interface Review {
  id: number;
  comment_text: string;
  publication_date: Date;
  entity_id: number;
  entity_type: EntityType;
}

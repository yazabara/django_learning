import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WorkoutSetPreviewComponent } from './workout-set-preview.component';

describe('WorkoutSetPreviewComponent', () => {
  let component: WorkoutSetPreviewComponent;
  let fixture: ComponentFixture<WorkoutSetPreviewComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WorkoutSetPreviewComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WorkoutSetPreviewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

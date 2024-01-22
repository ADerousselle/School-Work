import { ComponentFixture, TestBed } from '@angular/core/testing';

import { QueryserviceComponent } from './queryservice.component';

describe('QueryserviceComponent', () => {
  let component: QueryserviceComponent;
  let fixture: ComponentFixture<QueryserviceComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [QueryserviceComponent]
    });
    fixture = TestBed.createComponent(QueryserviceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

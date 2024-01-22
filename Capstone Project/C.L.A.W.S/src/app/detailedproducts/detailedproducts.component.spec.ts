import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DetailedproductsComponent } from './detailedproducts.component';

describe('DetailedproductsComponent', () => {
  let component: DetailedproductsComponent;
  let fixture: ComponentFixture<DetailedproductsComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [DetailedproductsComponent]
    });
    fixture = TestBed.createComponent(DetailedproductsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

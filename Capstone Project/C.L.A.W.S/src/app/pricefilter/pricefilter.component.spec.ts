import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PricefilterComponent } from './pricefilter.component';

describe('PricefilterComponent', () => {
  let component: PricefilterComponent;
  let fixture: ComponentFixture<PricefilterComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [PricefilterComponent]
    });
    fixture = TestBed.createComponent(PricefilterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

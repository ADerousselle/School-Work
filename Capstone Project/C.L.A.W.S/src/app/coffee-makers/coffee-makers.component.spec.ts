import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CoffeeMakersComponent } from './coffee-makers.component';

describe('CoffeeMakersComponent', () => {
  let component: CoffeeMakersComponent;
  let fixture: ComponentFixture<CoffeeMakersComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CoffeeMakersComponent]
    });
    fixture = TestBed.createComponent(CoffeeMakersComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

import { Component, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-price-filter',
  templateUrl: './price-filter.component.html',
  styleUrls: ['./price-filter.component.css']
})
export class PriceFilterComponent {
  minPrice: number = 0;
  maxPrice: number = 0;

  @Output() filterApplied: EventEmitter<any> = new EventEmitter<any>();

  constructor() {}

  applyFilter() {
    // Emit event with filter data
    this.filterApplied.emit({ minPrice: this.minPrice, maxPrice: this.maxPrice });
  }
}
import { Component } from '@angular/core';
import { SaveProductService } from '../save-product.service';
import * as jsonData from '../assets/db_data.json'
import { HeaderComponent } from '../header/header.component';
@Component({
  selector: 'app-coffee-makers',
  templateUrl: './coffee-makers.component.html',
  styleUrls: ['./coffee-makers.component.css']
})
export class CoffeeMakersComponent {
  constructor(private saveProductService: SaveProductService, ){}
  searchResults = this.saveProductService.getCat()
  data: any = jsonData;
  store: any = this.data.Best_Buy.Name;
  filteredProducts: any[] = [];
  priceRange: number = 300;
  startValue: number = 300;
  endValue: number = 400;
  typeProduct: any = this.saveProductService.getKeyword();
  saveProduct(value: any){
    console.log('saving ');
    console.log(value);
    this.saveProductService.saveProductService(value);
  }
  filterProducts() {
    console.log('data', this.searchResults)
    this.filteredProducts = this.searchResults.filter((searchResults:any) => {
      // Replace 'item.Price' with the correct path to the price property in your data
      const price = searchResults.Price;
      return price >= this.startValue && price <= this.endValue;
    });
    console.log('Filtered Products:', this.filteredProducts);
  }
  updateFilter() {
    this.filterProducts();
  }
 
}





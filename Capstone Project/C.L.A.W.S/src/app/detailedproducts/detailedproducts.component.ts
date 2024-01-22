import { Component } from '@angular/core';
import * as jsonData from '../assets/laptops.json'
import { SaveProductService } from '../save-product.service';
import { HeaderComponent } from '../header/header.component';
@Component({
  selector: 'app-detailedproducts',
  templateUrl: './detailedproducts.component.html',
  styleUrls: ['./detailedproducts.component.css']
})
export class DetailedproductsComponent {
  product: any;
  searchResults = this.saveProductService.getCat();
  similarProducts: any[] = [];

  // Price range properties
 
    constructor(private saveProductService: SaveProductService){}
    ngOnInit() {
        this.product = this.saveProductService.getProduct();
        this.similarProducts = this.getSimilarProducts();
        console.log('similar products:', this.similarProducts)
        console.log('', this.similarProducts)
    }
    printProduct(): any{
      console.log('printing',this.product.product.title)
      return this.product.product.title
    }
    inStock(){
      console.log(this.product.inventory.in_stock)
      if(this.product.inventory.in_stock){return "YES"}
      else{return "NO"}
    }
    getProductLink(){
      console.log(this.product.product.link)
    }
    
    // Existing methods 
    getSimilarProducts() {
      // Filter similar products based on price
      const similarPrice = this.product.offers.primary.price;
      return this.similarProducts = this.searchResults.filter((searchResults: any) => {
          return Math.abs(searchResults.offers.primary.price - similarPrice) <= 50; // Adjust the price range as needed
      });
     
  }
    
}


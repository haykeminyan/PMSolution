import {Component} from '@angular/core';
import {FactureService} from "../../services/facture.service";
import {HttpClient} from "@angular/common/http";
import {FormControl} from "@angular/forms";

export interface Facture {
  // id?: string
  name?: string
  created_date?: string
  updated_date?: string
  reference?: string
  destination?: string
  quantity?: number
  percent?: number
  quantity_after_percent?: number
  net_a_payer?: number
  advance_payment?: string
  total_payment?: number
  total_tax?: number
  total_payment_after_tax?: number
}



@Component({
  selector: 'app-facture-list',
  templateUrl: './facture-list.component.html',
  styleUrls: ['./facture-list.component.css']
})
export class FactureListComponent {
  page = 1;
  pageSize = 20;
  facture!: Object | any
  collectionSize: any
  countries?: Facture[]
  filter = new FormControl('', { nonNullable: true });
  searchText: any;
  constructor(private factureService: FactureService, private httpClient: HttpClient) {

  }

  ngOnInit(): void {
    this.factureService.getAll().subscribe(response => {
      this.facture = response
    })
    this.getAll();
    this.getSlider();
  }

  getAll() {
    return this.httpClient.get('http://localhost:8000/api/facture')
  }

  getSlider() {
    return this.getAll().subscribe(response => {
      this.facture = response
        this.countries = this.facture?.map((item: any, i: number) => ({ id: i + 1, ...item })).slice(
        (this.page - 1) * this.pageSize,
        (this.page - 1) * this.pageSize + this.pageSize,
      );
      this.collectionSize = this.facture.length
      this.facture = this.countries
      }
    )
  }



}

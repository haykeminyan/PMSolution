import {Component, PipeTransform} from '@angular/core';
import {FactureService} from "../../services/facture.service";
import {HttpClient} from "@angular/common/http";
import {FormControl, FormsModule, ReactiveFormsModule} from "@angular/forms";
import {AsyncPipe, DecimalPipe, NgFor} from "@angular/common";
import {NgbPagination, NgbTypeaheadModule} from "@ng-bootstrap/ng-bootstrap";
import {Ng2SearchPipeModule} from "ng2-search-filter";
import {Observable, pipe,map, startWith} from "rxjs";

export interface Facture {
  id?: string
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
  selector: 'facture-list-component',
  standalone: true,
  imports: [DecimalPipe, NgFor, AsyncPipe, ReactiveFormsModule, NgbTypeaheadModule, Ng2SearchPipeModule, NgbPagination, FormsModule],
  templateUrl: './facture-list.component.html',
  providers: [DecimalPipe],
  styleUrls: ['./facture-list.component.css']
})
export class FactureListComponent {
  page = 1;
  pageSize = 20;
  facture!: Object | any
  collectionSize: any
  countries?: Observable<void>
  filter = new FormControl('', { nonNullable: true });
  searchText: any;

  constructor(private factureService: FactureService, private httpClient: HttpClient, pipe: DecimalPipe) {
    this.getAll().subscribe(response => {
      this.facture = response
      console.log(this.facture)

    this.countries = this.filter.valueChanges.pipe(
      startWith(''),
      map((text) => this.search(text, pipe)),
    );
      console.log(this.facture)
    })
  }


  ngOnInit(): void {
    this.getSlider();
  }

  search(text: string, pipe: PipeTransform) {
     this.getAll().subscribe(response => {
       this.facture = response
       console.log(this.facture)


    return this.facture.filter((country: any) => {
      const term = text.toLowerCase();
      console.log(term)
      console.log(country)
      return (
        country.name.toLowerCase().includes(term)||
        pipe.transform(country.id).includes(term)||
        pipe.transform(country.name).includes(term) ||
        pipe.transform(country.created_date).includes(term) ||
        pipe.transform(country.updated_date).includes(term) ||
        pipe.transform(country.reference).includes(term) ||
        pipe.transform(country.destination).includes(term) ||
        pipe.transform(country.quantity).includes(term) ||
        pipe.transform(country.percent).includes(term) ||
        pipe.transform(country.quantity_after_percent).includes(term) ||
        pipe.transform(country.net_a_payer).includes(term) ||
        pipe.transform(country.advance_payment).includes(term) ||
        pipe.transform(country.total_payment).includes(term) ||
        pipe.transform(country.total_tax).includes(term) ||
        pipe.transform(country.total_payment_after_tax).includes(term)
      );
    });
     });
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

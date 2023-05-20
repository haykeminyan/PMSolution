import {Input, Component, Injectable, OnInit, ViewChild, Output, EventEmitter, PipeTransform} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {FormControl, FormsModule, ReactiveFormsModule} from "@angular/forms";
import {AsyncPipe, DatePipe, DecimalPipe, NgFor, NgForOf} from "@angular/common";
import {NgbPagination, NgbPaginationModule, NgbTypeaheadModule} from "@ng-bootstrap/ng-bootstrap";
import {Ng2SearchPipeModule} from "ng2-search-filter";
import {RouterOutlet} from "@angular/router";
import {MatTableDataSource, MatTableModule} from '@angular/material/table';
import {MatIconModule} from "@angular/material/icon";
import {MatButtonModule} from "@angular/material/button";
import {MatSort, MatSortModule} from "@angular/material/sort";
import {MatInputModule} from "@angular/material/input";
import {MatPaginator, MatPaginatorModule} from "@angular/material/paginator";
import {FactureService} from "../../services/facture.service";


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

@Injectable({
  providedIn: 'root'
})
@Component({
  selector: 'facture-list-component',
  standalone: true,
  imports: [DecimalPipe, NgFor, FormsModule, NgbTypeaheadModule, NgbPaginationModule, DatePipe, Ng2SearchPipeModule],
  templateUrl: './facture-list.component.html',
  providers: [DecimalPipe, DatePipe],
  styleUrls: ['./facture-list.component.css']
})
export class FactureListComponent implements OnInit{
  page = 1;
  pageSize = 4;
  factureApi!: []
  nestedFactures!: any
  factures!: any
  collectionSize: any;
  searchText: any;
  constructor( private service: FactureService) {
  }


  ngOnInit() {
    this.service.getAll().subscribe(
      data => {
        this.factureApi = data
        this.getListOfAllFacture()
      }
    )
  }

  getListOfAllFacture(){
    this.factures = []
    this.collectionSize = this.factureApi.length;
    this.nestedFactures = this.factureApi?.map((facture, i) => ({ id: i + 1, facture })).slice(
      (this.page - 1) * this.pageSize,
      (this.page - 1) * this.pageSize + this.pageSize,
    )
    this.nestedFactures.forEach((value: { facture: any; })=>{this.factures.push(value.facture)})

  }


}

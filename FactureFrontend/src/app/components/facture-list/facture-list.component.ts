import {AfterViewInit, Component, OnInit, PipeTransform, ViewChild} from '@angular/core';
import {FactureService} from "../../services/facture.service";
import {HttpClient} from "@angular/common/http";
import {FormControl, FormsModule, ReactiveFormsModule} from "@angular/forms";
import {AsyncPipe, DatePipe, DecimalPipe, NgFor, NgForOf} from "@angular/common";
import {NgbPagination, NgbTypeaheadModule} from "@ng-bootstrap/ng-bootstrap";
import {Ng2SearchPipeModule} from "ng2-search-filter";
import {Observable, pipe,map, startWith} from "rxjs";
import { Injectable } from '@angular/core';
import {AppModule} from "../../app.module";
import {RouterOutlet} from "@angular/router";
import {MatTableDataSource, MatTableModule} from '@angular/material/table';
import {MatIconModule} from "@angular/material/icon";
import {MatButtonModule} from "@angular/material/button";
import {MatSort, MatSortModule} from "@angular/material/sort";
import {MatInputModule} from "@angular/material/input";
import {MatPaginator, MatPaginatorModule} from "@angular/material/paginator";


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
  imports: [NgFor, AsyncPipe, ReactiveFormsModule, NgbTypeaheadModule, Ng2SearchPipeModule, NgbPagination, FormsModule, NgForOf, RouterOutlet, MatTableModule, MatIconModule, MatButtonModule, DatePipe, DecimalPipe, MatSortModule, MatInputModule, MatPaginatorModule],
  templateUrl: './facture-list.component.html',
  providers: [DecimalPipe, DatePipe],
  styleUrls: ['./facture-list.component.css']
})
export class FactureListComponent implements OnInit, AfterViewInit{
  page = 1;
  pageSize = 20;
  facture!: Object | any
  collectionSize: any
  countries: any
  filter = new FormControl('', { nonNullable: true });
  searchTerm = '';
  displayedColumns = ['name', 'created_date', 'updated_date', 'reference',
    'destination', 'quantity', 'percent', 'quantity_after_percent', 'net_a_payer',
    'advance_payment', 'total_payment', 'total_tax',
    'total_payment_after_tax', 'details', 'update', 'delete'];
  public dataSource = new MatTableDataSource<Facture>();

  @ViewChild(MatSort) sort: MatSort | undefined;
  @ViewChild(MatPaginator) paginator: MatPaginator | undefined;
  constructor(private httpClient: HttpClient) {


  }
  public doFilter = (value: string) => {
    this.dataSource.filter = value.trim().toLocaleLowerCase();

  }


  ngOnInit() {
    this.getAll();
  }

  ngAfterViewInit(): void {
    // @ts-ignore
    this.dataSource.paginator = this.paginator;
    // @ts-ignore
    this.dataSource.sort = this.sort

    console.log(this.dataSource.data)
    console.log(this.dataSource.paginator?.pageIndex)
  }

  public getAll() {
    return this.httpClient.get('http://localhost:8000/api/facture').subscribe(res=> {
      this.dataSource.data = res as Facture[]
    })
  }

  public redirectToDetails = (id: string) => {

  }
  public redirectToUpdate = (id: string) => {

  }
  public redirectToDelete = (id: string) => {

  }



}

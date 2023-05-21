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
import {Facture} from "../../facture";
import {MatSelectModule} from "@angular/material/select";


@Injectable({
  providedIn: 'root'
})
@Component({
  selector: 'facture-list-component',
  standalone: true,
  imports: [DecimalPipe, NgFor, FormsModule, NgbTypeaheadModule, NgbPaginationModule, DatePipe, Ng2SearchPipeModule, MatInputModule, MatSelectModule, ReactiveFormsModule],
  templateUrl: './facture-list.component.html',
  providers: [DecimalPipe, DatePipe],
  styleUrls: ['./facture-list.component.css']
})
export class FactureListComponent implements OnInit{
  page = 1;
  pageSize = 4;
  factures: Facture[] = [];
  sortOrderControl = new FormControl('');

  constructor( private service: FactureService) {
  }


  ngOnInit() {
    this.getApi('', '')
    this.sortOrderControl.valueChanges.subscribe((value) => {
      if (value) {
        this.doSorting(value);
      }
      console.log(this.factures)
    });

  }

  doSorting(value: string) {
    let sortColumn: string = '';
    let sortType: string = '';
    if (value.toLowerCase() === 'id-by-desc') {
      sortColumn = '-id';
      sortType = 'desc';
    } else if (value.toLowerCase() === 'id-by-asc') {
      sortColumn = 'id';
      sortType = 'asc';
    }
    else if (value.toLowerCase() === 'name-by-desc') {
      sortColumn = '-name';
      sortType = 'desc';
    }
    else if (value.toLowerCase() === 'name-by-asc') {
      sortColumn = 'name';
      sortType = 'asc';
    }
    // TO DO EXPAND AND ADD ALL FILTERS!

    this.getApi(sortColumn, sortType);
  }
  getApi(sortColumn: string, sortType: string){
    this.service.get(sortColumn, sortType).subscribe(
      response => {
        this.factures = response
      }
    )
  }


}

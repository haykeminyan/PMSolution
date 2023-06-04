import {
  Input,
  Component,
  Injectable,
  OnInit,
  ViewChild,
  Output,
  EventEmitter,
  PipeTransform,
  AfterViewInit
} from '@angular/core';
import {HttpClient, HttpResponse} from "@angular/common/http";
import {FormControl, FormsModule, ReactiveFormsModule} from "@angular/forms";
import {AsyncPipe, DatePipe, DecimalPipe, NgFor, NgForOf} from "@angular/common";
import {NgbPagination, NgbPaginationModule, NgbTypeaheadModule} from "@ng-bootstrap/ng-bootstrap";
import {Ng2SearchPipeModule} from "ng2-search-filter";
import {RouterLink, RouterOutlet} from "@angular/router";
import {MatTableDataSource, MatTableModule} from '@angular/material/table';
import {MatIconModule} from "@angular/material/icon";
import {MatButtonModule} from "@angular/material/button";
import {MatSort, MatSortModule} from "@angular/material/sort";
import {MatInputModule} from "@angular/material/input";
import {MatPaginator, MatPaginatorModule, PageEvent} from "@angular/material/paginator";
import {FactureService} from "../../services/facture.service";
import {Facture} from "../../facture";
import {MatSelectModule} from "@angular/material/select";


@Injectable({
  providedIn: 'root'
})
@Component({
  selector: 'facture-list-component',
  standalone: true,
  imports: [DecimalPipe, NgFor, FormsModule, NgbTypeaheadModule, NgbPaginationModule, DatePipe, Ng2SearchPipeModule, MatInputModule, MatSelectModule, ReactiveFormsModule, MatButtonModule, MatIconModule, MatPaginatorModule, RouterLink],
  templateUrl: './facture-list.component.html',
  providers: [DecimalPipe, DatePipe],
  styleUrls: ['./facture-list.component.css']
})
export class FactureListComponent implements OnInit{
  page = 1;
  sortOrderControl = new FormControl('');
  searchKey = new FormControl('')
  factures: Facture[] = [];
  totalRecords: number = 0
  pageIndex = 0
  pageSize = 5
  constructor( private service: FactureService) {
  }


  ngOnInit() {
    this.getApi('', '', '', this.pageSize, this.pageIndex)
    this.sortOrderControl.valueChanges.subscribe((value) => {
      if (value) {
        let sortResult = this.doSorting(value)
        this.pageIndex = 0
        this.pageSize = 5
        this.getApi(sortResult.sortColumn, sortResult.sortType, '', this.pageIndex, this.pageSize)
      }
      console.log('!!!')
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

    // this.getApi(sortColumn, sortType, searchKey);
    return {sortColumn, sortType}
  }

  searchByName() {
    let sortResult = this.doSorting(this.sortOrderControl.value ?? '');
    this.pageIndex = 0
    this.pageSize = 5
    this.getApi(
      sortResult.sortColumn,
      sortResult.sortType,
      this.searchKey.value ?? '',
      this.pageIndex,
      this.pageSize
    );
  }

  getApi(sortColumn: string, sortType: string, searchKey: string, currentPage:number, pageSize:number){
    this.service.get(sortColumn, sortType, searchKey, (currentPage + 1), pageSize).subscribe(
      response => {
        this.factures = response.body as unknown as Facture[]
        console.log(response)
        console.log(this.factures)
        this.totalRecords = response.headers.get('content-length')
          ? Math.floor(Number(response.headers.get('content-length'))/this.pageSize)
          : 0;
      }
    )
  }
  handlePageEvent(e: PageEvent) {

    this.pageIndex = e.pageIndex ;
    this.pageSize = e.pageSize;
    console.log(this.pageIndex)
    let sortResult = this.doSorting(this.sortOrderControl.value ?? '');
    this.getApi(
      sortResult.sortColumn,
      sortResult.sortType,
      this.searchKey.value ?? '',
      this.pageIndex,
      this.pageSize
    );
  }


  deleteFacture(id: any) {
    this.service.delete(id).subscribe(()=>{
      this.factures = this.factures.filter((value) => value.id !== id);
    })
  }


}

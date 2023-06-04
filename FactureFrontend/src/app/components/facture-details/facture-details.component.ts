import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {Facture} from "../../facture";
import {FactureService} from "../../services/facture.service";
import {FactureListComponent} from "../facture-list/facture-list.component";
import {ActivatedRoute, Router, RouterLink} from "@angular/router";
import {DatePipe, DecimalPipe, NgFor} from "@angular/common";
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {NgbPaginationModule, NgbTypeaheadModule} from "@ng-bootstrap/ng-bootstrap";
import {Ng2SearchPipeModule} from "ng2-search-filter";
import {MatInputModule} from "@angular/material/input";
import {MatSelectModule} from "@angular/material/select";
import {MatButtonModule} from "@angular/material/button";
import {MatIconModule} from "@angular/material/icon";
import {MatPaginatorModule} from "@angular/material/paginator";

@Component({
  selector: 'app-facture-details',
  standalone: true,
  imports: [DecimalPipe, NgFor, FormsModule, NgbTypeaheadModule, NgbPaginationModule, DatePipe, Ng2SearchPipeModule, MatInputModule, MatSelectModule, ReactiveFormsModule, MatButtonModule, MatIconModule, MatPaginatorModule, RouterLink],
  templateUrl: './facture-details.component.html',
  styleUrls: ['./facture-details.component.css']
})
export class FactureDetailsComponent implements OnInit{
  factures: any= []
constructor(
  private router: Router,
  private activeRoute: ActivatedRoute,
  private service: FactureService) {
}
  ngOnInit(): void {
    const id = this.activeRoute.snapshot.queryParams['id']
    this.viewFacture(id)
  }

  viewFacture(id: number){
    this.service.getFacture(id).subscribe(
      response=>{
        this.factures.push(response.body as unknown as Facture[])
      }
    )
  }



}

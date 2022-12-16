import {Component, OnInit} from '@angular/core';
import {FactureService} from "./services/facture.service";
import {FactureModel} from "./models/facture.model";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  facture!: FactureModel[]
  constructor(private factureService: FactureService) { }

  ngOnInit(): void {
    this.factureService.getAll().subscribe(response => {
      this.facture = response
      console.log(this.facture)
    })
  }

}

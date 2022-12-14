import {Component, OnInit} from '@angular/core';
import {FactureService} from "./services/facture.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  constructor(private factureService: FactureService) { }

  ngOnInit(): void {
    this.getAll();
  }

  getAll() {
    this.factureService.getAll().subscribe({
        next: (data) => {
          console.log(data);
        },
        error: (error) => {
          console.log(error);
        }
      }
    )
  }

}

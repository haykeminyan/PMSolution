import { Component, OnInit } from '@angular/core';
import { FactureModel } from 'src/app/models/facture.model';
import { FactureService } from 'src/app/services/facture.service';

@Component({
  selector: 'app-add-tutorial',
  templateUrl: './add-facture.component.html',
  styleUrls: ['./add-facture.component.css']
})
export class AddFactureComponent implements OnInit {

  facture: FactureModel = {

  };
  submitted = false;

  constructor(private factureService: FactureModel) { }

  ngOnInit(): void {
  }



  newTutorial(): void {
    this.submitted = false;
    this.facture = {
        id: '',
        name: 'Test'
    };
  }

}

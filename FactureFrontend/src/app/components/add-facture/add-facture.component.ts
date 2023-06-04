import { Component, OnInit } from '@angular/core';
import { FactureModel } from 'src/app/models/facture.model';
import { FactureService } from 'src/app/services/facture.service';
import {Facture} from "../../facture";
import {AbstractControl, FormBuilder, FormControl, FormGroup, Validators} from "@angular/forms";

@Component({
  selector: 'app-add-tutorial',
  templateUrl: './add-facture.component.html',
  styleUrls: ['./add-facture.component.css']
})
export class AddFactureComponent implements OnInit {
  factures: Facture[] = [];
  form: FormGroup = new FormGroup({
    name: new FormControl('', Validators.required),
    reference: new FormControl(''),
    destination: new FormControl(''),
    quantity: new FormControl(''),
    created_date: new FormControl(''),
    updated_date: new FormControl(''),
    percent: new FormControl(''),
    quantity_after_percent: new FormControl(''),
    net_a_payer: new FormControl(''),
    advance_payment: new FormControl(''),
    total_payment: new FormControl(''),
    total_tax: new FormControl(''),
    total_payment_after_tax: new FormControl(''),
  });
  submitted = false

  constructor( private service: FactureService, private formBuilder: FormBuilder) {
  }


  ngOnInit() {
  }
  get f(): { [key: string]: AbstractControl } {
    return this.form.controls;
  }

  onSubmit(): void {
    this.submitted = true;

    if (this.form.invalid) {
      return;
    }
    console.log(this.form.value)
    this.service.post(this.form.value).subscribe(()=>{this.factures.push(this.form.value)})
    console.log(JSON.stringify(this.form.value, null, 2));
  }

  onReset(): void {
    this.submitted = false;
    this.form.reset();
  }

}

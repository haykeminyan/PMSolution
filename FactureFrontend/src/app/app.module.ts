import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { AddFactureComponent } from './components/add-facture/add-facture.component';
import { FactureDetailsComponent } from './components/facture-details/facture-details.component';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { FactureComponent } from './facture/facture.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { Ng2SearchPipeModule } from 'ng2-search-filter';
import {FactureListComponent} from "./components/facture-list/facture-list.component";
import { SearchFilterPipe } from './search-filter.pipe';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {MatSidenavModule} from "@angular/material/sidenav";
import {MatSelectModule} from "@angular/material/select";

@NgModule({
  declarations: [
    AppComponent,
    AddFactureComponent,
    FactureComponent,
    SearchFilterPipe
  ],
  imports: [
    MatSelectModule,
    FormsModule,
    ReactiveFormsModule,
    BrowserModule,
    FactureListComponent,
    FormsModule,
    HttpClientModule,
    AppRoutingModule,
    NgbModule,
    Ng2SearchPipeModule,
    BrowserAnimationsModule,
    MatSidenavModule
  ],
  providers: [],
  exports: [
    SearchFilterPipe
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }

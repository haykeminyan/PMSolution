import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
// import { FactureListComponent } from './components/facture-list/facture-list.component';
import { FactureDetailsComponent } from './components/facture-details/facture-details.component';
import { AddFactureComponent } from './components/add-facture/add-facture.component';
import {FactureListComponent} from "./components/facture-list/facture-list.component";

const routes: Routes = [
  { path: '', component: FactureListComponent},
  // { path: 'tutorials', component: FactureListComponent },
  // { path: 'tutorials/:id', component: FactureDetailsComponent },
  // { path: 'add', component: AddFactureComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
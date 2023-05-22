import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { FactureModel } from '../models/facture.model';
import { BehaviorSubject } from 'rxjs/internal/BehaviorSubject';
import {Facture} from "../facture";
const baseUrl = 'http://localhost:8000/api/';

@Injectable({
  providedIn: 'root'
})
export class FactureService {
  private url = 'http://localhost:8000/api/facture'
  constructor(private http: HttpClient) { }

  get(sortColumn: string, sortType: string): Observable<any> {
    let url = 'http://localhost:8000/api/facture/filters?ordering='
    if(sortColumn && sortType){
      url = `${url}${sortColumn}`
    }
    return this.http.get<Facture[]>(url);
  }

  create(data: any): Observable<any> {
    return this.http.post(baseUrl, data);
  }

  update(id: any, data: any): Observable<any> {
    return this.http.put(`${baseUrl}/${id}`, data);
  }

  delete(id: any): Observable<any> {
    return this.http.delete(`${baseUrl}/${id}`);
  }

  deleteAll(): Observable<any> {
    return this.http.delete(baseUrl);
  }

  findByTitle(title: any): Observable<FactureModel[]> {
    return this.http.get<FactureModel[]>(`${baseUrl}?title=${title}`);
  }
}

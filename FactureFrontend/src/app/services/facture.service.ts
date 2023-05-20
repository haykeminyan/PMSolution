import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { FactureModel } from '../models/facture.model';
import { BehaviorSubject } from 'rxjs/internal/BehaviorSubject';
const baseUrl = 'http://localhost:8000/api/';

@Injectable({
  providedIn: 'root'
})
export class FactureService {
  private url = 'http://localhost:8000/api/facture'
  constructor(private http: HttpClient) { }

  getAll(): Observable<any> {
    return this.http.get(this.url) as Observable<any>;
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

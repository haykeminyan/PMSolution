import { Injectable } from '@angular/core';
import {HttpClient, HttpResponse} from '@angular/common/http';
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

  get(sortColumn: string, sortType: string, searchKey: string, currentPage: number,pageSize: number): Observable<HttpResponse<HttpResponse<any>>> {
    let url = 'http://localhost:8000/api/facture'
    if (sortColumn && sortType && searchKey){
      url = `${url}/filters?search=${searchKey}&ordering=${sortColumn}?p=${currentPage}&page_size=${pageSize}`
    }
    else if(sortColumn && sortType){
      url = `${url}/filters?ordering=${sortColumn}`
    }
    if (searchKey){
      url = `${url}?p=${currentPage}&page_size=${pageSize}`
      console.log(url)
    }
    console.log(url)

    return this.http.get<HttpResponse<any>>(url, { observe: 'response' });
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

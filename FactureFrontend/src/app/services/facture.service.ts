import { Injectable } from '@angular/core';
import {HttpClient, HttpResponse} from '@angular/common/http';
import { Observable } from 'rxjs';
import { FactureModel } from '../models/facture.model';
import { BehaviorSubject } from 'rxjs/internal/BehaviorSubject';
import {Facture} from "../facture";
const baseUrl = 'http://localhost:8000/api';

@Injectable({
  providedIn: 'root'
})
export class FactureService {
  private url = 'http://localhost:8000/api/facture'
  constructor(private http: HttpClient) { }

  get(sortColumn: string, sortType: string, searchKey: string, currentPage: number,pageSize: number): Observable<HttpResponse<HttpResponse<any>>> {
    let url = `http://localhost:8000/api/facture?p=${currentPage}&page_size=${pageSize}`
    if (sortColumn && sortType && searchKey){
      url = `${url}&search=${searchKey}&ordering=${sortColumn}`
    }
    if(sortColumn && sortType){
      url = `${url}&ordering=${sortColumn}`
    }
    console.log(url)

    return this.http.get<HttpResponse<any>>(url, { observe: 'response' });
  }

  getFacture(id: any){
    const url = `http://localhost:8000/api/facture/${id}`
    console.log(`http://localhost:8000/api/facture/${id}`)
    return this.http.get<HttpResponse<any>>(url, { observe: 'response' })
  }

  post(data: any): Observable<HttpResponse<HttpResponse<any>>> {
    const url = 'http://localhost:8000/api/facture'
    console.log(this.http.post<HttpResponse<any>>(url, data))
    return this.http.post<HttpResponse<any>>(url, data)
  }

  delete(id: any): Observable<any> {
    const url = `http://localhost:8000/api/facture/${id}`
    return this.http.delete(url)
  }

  put(id: any, data: any): Observable<any> {
    const url = `http://localhost:8000/api/facture/${id}`
    return this.http.put(url, data)
  }


}

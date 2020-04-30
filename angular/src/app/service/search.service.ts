import {Injectable} from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class SearchService {
  private searchTerms: string[] = [];

  constructor() {

  }

  putTerm(term: string) {
    this.searchTerms.push(term);
  }

  getTerms() {
    return this.searchTerms;
  }
}

import {Component, OnInit} from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {CookieService} from 'ngx-cookie-service';
import {AngularFirestore, AngularFirestoreCollection, AngularFirestoreDocument} from '@angular/fire/firestore';
import {Observable} from 'rxjs';
import {AngularFireAuth} from "@angular/fire/auth";

export interface Item {
  name: string;
  food?: string;
}

function buildURL(code: string) {
  const url = "https://www.strava.com/oauth/authorize?client_id=7704&state=" + code + "&redirect_uri=" +
    "https://strava.montcopa.io/auth&response_type=code&scope=" +
    "read_all,activity:read_all,profile:read_all"
  return url

}


@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {
  items: Observable<any[]>;
  item: Observable<Item>;
  url = '';
  state = '';
  access_token = '';
  refresh_token = '';
  lastname = '';
  firstname = '';
  private itemsCollection: AngularFirestoreCollection<Item>;
  private itemDoc: AngularFirestoreDocument<Item>;

  constructor(private route: ActivatedRoute, private cookieService: CookieService,
              private afs: AngularFirestore, public auth: AngularFireAuth) {

    this.itemsCollection = afs.collection<Item>('items');

    this.items = this.itemsCollection.valueChanges();

    this.itemDoc = afs.doc<Item>('items/1');
    this.item = this.itemDoc.valueChanges();
    // this.items = afs.collection('items').valueChanges();

    this.cookieService.set('Test', 'Hello World');
    this.state = this.cookieService.get('state');
    this.access_token = this.cookieService.get('access_token');
    this.refresh_token = this.cookieService.get('refresh_token');
    this.lastname = this.cookieService.get('lastname');
    this.firstname = this.cookieService.get('firstname');

    this.url = buildURL(this.state);

    console.log(`state: ${this.state}`)

    this.route.queryParams.subscribe(params => {
      // this.param1 = params['param1'];
      // this.param2 = params['param2'];
      console.log(params)
    });


  }

  ngOnInit(): void {
  }

  addItem(item: Item) {
    this.itemsCollection.add(item);
  }

  update(item: Item) {
    this.itemDoc.update(item);
  }

}

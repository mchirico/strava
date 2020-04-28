import {Component, OnInit} from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {CookieService} from 'ngx-cookie-service';


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
  url = '';
  state = '';
  access_token = '';
  refresh_token = '';
  lastname = '';
  firstname = '';

  constructor(private route: ActivatedRoute, private cookieService: CookieService) {
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

}

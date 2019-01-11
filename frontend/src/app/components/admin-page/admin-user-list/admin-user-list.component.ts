import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-admin-user-list',
  templateUrl: './admin-user-list.component.html',
  styleUrls: ['./admin-user-list.component.css']
})
export class AdminUserListComponent implements OnInit {

  @Input() users: UserData.SimpleUser[];

  constructor() {
  }

  ngOnInit() {
  }

}

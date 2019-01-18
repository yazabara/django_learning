import {Component, OnInit} from '@angular/core';
import {AdminDataService} from "../../service/admin-data.service";

@Component({
  selector: 'app-admin-page',
  templateUrl: './admin-page.component.html',
  styleUrls: ['./admin-page.component.css']
})
export class AdminPageComponent implements OnInit {
  users: UserData.SimpleUser[];
  adminService: AdminDataService;

  constructor(adminService: AdminDataService) {
    this.adminService = adminService
  }

  ngOnInit() {
    this.adminService.getUsersList().subscribe(users => this.users = users);
  }

}

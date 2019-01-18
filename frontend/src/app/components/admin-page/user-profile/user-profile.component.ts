import {Component, OnInit} from '@angular/core';
import {ActivatedRoute, ParamMap} from "@angular/router";
import {AdminDataService} from "../../../service/admin-data.service";

@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.scss']
})
export class UserProfileComponent implements OnInit {
  user: UserData.SimpleUser;

  constructor(private route: ActivatedRoute, private service: AdminDataService) {
  }

  ngOnInit() {
    this.route.paramMap.subscribe((params: ParamMap) => {
      this.service.getUserById(params.get('id')).subscribe(data => {
        if (data) {
          this.user = data
        }
      })
    })
  }

}

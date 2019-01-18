import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { AdminRoutingModule } from './admin-routing.module';
import { UserProfileComponent } from "./user-profile/user-profile.component";
import { AdminUserListComponent } from "./admin-user-list/admin-user-list.component";
import { AdminPageComponent } from "./admin-page.component";

@NgModule({
  declarations: [
    UserProfileComponent,
    AdminUserListComponent,
    AdminPageComponent
  ],
  imports: [
    CommonModule,
    AdminRoutingModule
  ]
})
export class AdminModule { }

import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MaterialModule } from './material.module';
import { PlayerComponent } from './pages/player/player.component';
import { ProfileComponent } from './pages/profile/profile.component';
import { MatSliderModule } from '@angular/material/slider';
import { FormsModule } from '@angular/forms';
import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { OpenigScreenComponent } from './pages/openig-screen/openig-screen.component';
import { WebcamModule } from 'ngx-webcam';
import { NgxFileDropModule } from 'ngx-file-drop';


@NgModule({
  declarations: [
    AppComponent,
    PlayerComponent,
    ProfileComponent,
    OpenigScreenComponent
   ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatSliderModule,
    FormsModule,
    MaterialModule,
    HttpClientModule,
    WebcamModule,
    NgxFileDropModule
  ],
  providers: [],
  bootstrap: [AppComponent],
  schemas:[CUSTOM_ELEMENTS_SCHEMA]
})
export class AppModule { }

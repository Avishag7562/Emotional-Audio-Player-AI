// src/app/material.module.ts
import { NgModule } from '@angular/core';
import {MatListModule} from '@angular/material/list'
import {MatButtonModule} from '@angular/material/button'
import {MatSliderModule} from '@angular/material/slider'
import {MatToolbarModule} from '@angular/material/toolbar'
import {MatCardModule} from '@angular/material/card'
import {MatIconModule} from '@angular/material/icon'

const modules = [
    MatButtonModule,
    MatListModule,
    MatSliderModule,
    MatIconModule,
    MatToolbarModule,
    MatCardModule,
    
];

@NgModule({
    imports: modules,
    exports: modules
})
export class MaterialModule {}
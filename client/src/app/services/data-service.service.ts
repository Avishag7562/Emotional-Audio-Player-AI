import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  private playerData: any;

  constructor() { }

  setPlayerData(data: any) {
    this.playerData = data;
  }

  getPlayerData() {
    return this.playerData;
  }
}

import { Component } from '@angular/core';
import { AudioService } from '../../services/audio.service';
import { StreamState } from '../../interfaces/stream-state';
import { AuthService } from '../../services/auth.service';
import { DataService } from '../../services/data-service.service';

@Component({
  selector: 'app-player',
  templateUrl: './player.component.html',
  styleUrls: ['./player.component.scss']
})
export class PlayerComponent {
  files: Array<any> = [];
  state: StreamState |undefined;
  currentFile: any = {};
  data: any;
  emotion: any;
  songs: any;
  songEmotion: Array<any> = [];


  constructor(private audioService: AudioService, public auth: AuthService, private dataService: DataService) {
    const data = this.dataService.getPlayerData();

    if (data) {
      this.emotion = data.emotion;
      this.songs = data.songs;
      this.songEmotion = data.songEmotionPromise;
      console.log(data);
    } else {
      // Handle case when data is not available
    }
    this.files = this.filterSongs()
    // listen to stream state
    this.audioService.getState()
    .subscribe(state => {
      this.state = state;
    });

  }

  ngOnInit(): void {

  }

  
  playStream(url:any) {
    console.log(url)
    this.audioService.playStream(url)
    .subscribe(events => {
      // listening for fun here
    });
    
    console.log('hhhhh');

  }

  openFile(file:any, index:any) {
    this.currentFile = { index, file };
    this.audioService.stop();
    console.log(file)
    this.playStream(file.url);
  }

  pause() {
    this.audioService.pause();
  }

  play() {
    this.audioService.play();
  }

  stop() {
    this.audioService.stop();
  }

  next() {
    if(this.currentFile.index == undefined)
      return
    const index = this.currentFile.index + 1;
    const file = this.files[index];
    this.openFile(file, index);
  }

  previous() {
    if(this.currentFile.index == undefined)
      return
    const index = this.currentFile.index - 1;
    const file = this.files[index];
    this.openFile(file, index);
  }

  isFirstPlaying() {
    return this.currentFile.index === 0;
  }

  isLastPlaying() {
    return this.currentFile.index === this.files.length - 1;
  }

  onSliderChangeEnd(change:any) {
    
    this.audioService.seekTo(change);
  }

  filterSongs(){
    const songs: any = this.songs.filter((song:any, i:any)=>{
        if(this.songEmotion[i] == 'Happy' && this.emotion.toLowerCase()=='happy')
          return true
        if(this.songEmotion[i] == 'Sad' && this.emotion.toLowerCase()=='sad')
          return true        
        if(this.songEmotion[i] == 'Angry' && this.emotion.toLowerCase()=='angry')
            return true        
        if(this.songEmotion[i] == 'Calm' && this.emotion.toLowerCase()=='neutral')
            return true
        return false
    });
  
  if(songs.length == 0)
    alert('Didnt faund mached songs')
  return songs
  }
}


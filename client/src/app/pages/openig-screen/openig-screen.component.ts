import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { WebcamImage, WebcamInitError } from 'ngx-webcam';
import { Subject } from 'rxjs';
import { FileSystemFileEntry, NgxFileDropEntry } from 'ngx-file-drop';
import { Router } from '@angular/router';
import { DataService } from '../../services/data-service.service';
import { Location } from '@angular/common';

@Component({
  selector: 'app-openig-screen',
  templateUrl: './openig-screen.component.html',
  styleUrls: ['./openig-screen.component.scss'],
})
export class OpenigScreenComponent implements OnInit {
  buttonState = 'initial';
  countdown: number = 12;
  countdownActive = false;
  visible = false;
  webcamActive = false;
  capturedImages: WebcamImage[] = [];
  isImageSest = false;
  isWaiting = false;


  webcamImage: WebcamImage | undefined;
  private trigger: Subject<void> = new Subject<void>();
  triggerObservable = this.trigger.asObservable();

  constructor(private http: HttpClient, private router: Router, private dataService: DataService, private location: Location) {}

  ngOnInit(): void {}

  // toggleButtonAnimation() {
  //   this.visible = !this.visible;
  //   setTimeout(() => {
  //     this.showSuccessAnimation = true;
  //   }, 1000); // Example delay for animation
  // }

  
  toggleButtonAnimation() {
    this.buttonState = this.buttonState === 'initial' ? 'final' : 'initial';
    if (this.buttonState === 'final') {
      this.startCountdown();
    }
  }

  songs: File[] = [];
  songPromise: any = null;

  onFileDrop(files: NgxFileDropEntry[]) {
    for (const droppedFile of files) {
      if (droppedFile.fileEntry.isFile) {
        const fileEntry = droppedFile.fileEntry as FileSystemFileEntry;
        fileEntry.file((file: File) => {
          if (this.isAudioFile(file)) {
            this.songs.push(file);
          }
        });
      }
    }
    this.sendSongs();
  }

  handleFiles(event: Event) {
    const input = event.target as HTMLInputElement;
    if (input.files) {
      for (let i = 0; i < input.files.length; i++) {
        const file = input.files[i];
        if (this.isAudioFile(file)) {
          this.songs.push(file);
        }
      }
      this.sendSongs();
    }
  }

  isAudioFile(file: File): boolean {
    const audioFileTypes = ['audio/mpeg', 'audio/wav', 'audio/ogg'];
    return audioFileTypes.includes(file.type);
  }

startCountdown(): void {
    this.countdownActive = true;
    this.visible = true;
    this.webcamActive = true;

    let initialDelayPassed = false;

    const countdownInterval = setInterval(async () => {
        if (!initialDelayPassed) {
            this.webcamActive = true; // Turn on the webcam
            setTimeout(() => {
                initialDelayPassed = true;
                this.captureImages(); // Start capturing images after 1 second delay
            }, 1000);
            return;
        }
    
        this.countdown--;
    
        if (this.countdown === 0) {
            clearInterval(countdownInterval);
            this.countdownActive = false;
            this.visible = false;
            this.webcamActive = false; // Turn off the webcam
    
            if (!this.isImageSest) {
                console.log(this.isImageSest);
                this.isImageSest = true;
                this.isWaiting = true;
                const image_emotion = await this.sendImages(); // Send captured images to server
                const songs_emotions = await this.songPromise;
                const newSongs =  this.songs.map((s:any)=>{
                  return {
                    url: URL.createObjectURL(s),
                    name: s.name,
                    artist: '' // You'll need to determine how to get artist information
                  };
                })    

                const data = {
                    emotion: image_emotion.emotion,
                    songs: newSongs,
                    songEmotionPromise: songs_emotions
                };
    
                this.dataService.setPlayerData(data);
                this.router.navigate(['/player']);
            }
        }
    }, 1000);
  }

  handleImage(webcamImage: WebcamImage): void {
    this.webcamImage = webcamImage;

    if (this.capturedImages.length < 10) {
      this.capturedImages.push(webcamImage); // Save the captured image
    }
  }

  triggerSnapshot(): void {
    this.trigger.next();
  }

  captureImages(): void {
    let counter = 0; // Counter for captured images

    const imageCaptureInterval = setInterval(() => {
      this.triggerSnapshot(); // Trigger snapshot
      counter++; // Increment the counter

      if (counter === 10) { // Check if 10 images were captured
        clearInterval(imageCaptureInterval); // Stop capturing images

        this.webcamActive = false; // Deactivate the webcam
        //this.sendImages(); // Send captured images to server
      }
    }, 1000);
  }

  async sendImages(): Promise<any> {

    const headers = new HttpHeaders().set('Content-Type', 'application/json');
    try{
    const response = await this.http.post('http://127.0.0.1:5000/classify_images', {'images':this.capturedImages}, {headers}).toPromise();
    return response;  
  }  
    catch (error: any) {
      if (error.status === 404) {
          alert('No face detected')
          location.reload();
      } else {
          console.log('An error occurred:', error);
      }

  }
}

  async sendSongs() {
    const formData: FormData = new FormData();

    for (let i = 0; i < this.songs.length; i++) {
      formData.append('songs', this.songs[i], this.songs[i].name);
    }

    try {
      this.songPromise = this.http.post('http://127.0.0.1:5000/classify_songs', formData).toPromise();
    } catch (error) {
      console.error('Error sending songs:', error);
    }
  }

  handleInitError(error: WebcamInitError): void {
    console.error('Webcam initialization error:', error);
  }
}






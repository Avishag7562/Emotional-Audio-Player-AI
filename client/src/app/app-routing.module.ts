import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PlayerComponent } from './pages/player/player.component';
import { ProfileComponent } from './pages/profile/profile.component';
import { OpenigScreenComponent } from './pages/openig-screen/openig-screen.component';

const routes: Routes = [
    // { path: '', component: PlayerComponent },
    // { path: 'profile', component: ProfileComponent },
    // { path: '**', redirectTo: '' },
    { path: '', component: OpenigScreenComponent },
    { path: 'player', component: PlayerComponent}

];

@NgModule({
    imports: [
      RouterModule.forRoot(routes)
    ],
    exports: [RouterModule],
})
export class AppRoutingModule {}


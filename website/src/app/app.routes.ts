import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './components/pages/home/home.component';
import { AboutComponent } from './components/pages/about/about.component';
import { ContactComponent } from './components/pages/contact/contact.component';
import { NotFoundComponent } from './components/pages/not-found/not-found.component';
import { NotYetComponent } from './components/pages/not-yet/not-yet.component';
import { TeamComponent } from './components/pages/team/team.component';
import { ServicesComponent } from './components/pages/services/services.component';
import { ArtistsComponent } from './components/pages/artists/artists.component';
import { GetintouchComponent } from './components/pages/getintouch/getintouch.component';
import { RequestComponent } from './components/pages/request/request.component';

export const routes: Routes = [
  { path: '', component: HomeComponent },
  // { path: '', component: NotYetComponent },
  { path: 'about', component: AboutComponent },
  { path: 'contact', component: ContactComponent },
  { path: 'not-found', component: NotFoundComponent },
  { path: 'not-yet', component: HomeComponent },
  { path: 'team', component: TeamComponent },
  { path: 'services', component: ServicesComponent },
  { path: 'artists', component: ArtistsComponent },
  { path: 'getintouch', component: GetintouchComponent },
  { path: 'request', component: RequestComponent },
  { path: '**', redirectTo: 'not-found' } 
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

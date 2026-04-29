import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './components/pages/home/home.component';
import { AboutComponent } from './components/pages/about/about.component';
import { ContactComponent } from './components/pages/contact/contact.component';
import { NotFoundComponent } from './components/pages/not-found/not-found.component';
import { TeamComponent } from './components/pages/team/team.component';
import { ServicesComponent } from './components/pages/services/services.component';
import { ArtistsComponent } from './components/pages/artists/artists.component';
import { StageComponent } from './components/pages/stage/stage.component';
import { GalleryComponent } from './components/pages/gallery/gallery.component';
import { PrivacyComponent } from './components/pages/privacy/privacy.component';
import { TermsComponent } from './components/pages/terms/terms.component';
import { LicensingComponent } from './components/pages/licensing/licensing.component';
import { CookiesComponent } from './components/pages/cookies/cookies.component';

export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'about', component: AboutComponent },
  { path: 'contact', component: ContactComponent },
  { path: 'team', component: TeamComponent },
  { path: 'services', component: ServicesComponent },
  { path: 'artists', component: ArtistsComponent },
  { path: 'stage', component: StageComponent },
  { path: 'gallery', component: GalleryComponent },
  { path: 'getintouch', redirectTo: 'contact', pathMatch: 'full' },
  { path: 'privacy', component: PrivacyComponent },
  { path: 'terms', component: TermsComponent },
  { path: 'licensing', component: LicensingComponent },
  { path: 'cookies', component: CookiesComponent },
  { path: 'not-found', component: NotFoundComponent },
  { path: '**', redirectTo: 'not-found' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

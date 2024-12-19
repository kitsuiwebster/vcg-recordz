import { Component } from '@angular/core';
import { RouterModule, Router } from '@angular/router';

@Component({
  selector: 'app-layout',
  standalone: true,
  templateUrl: './layout.component.html',
  styleUrls: ['./layout.component.scss'],
  imports: [RouterModule]
})
export class LayoutComponent {
  isMenuOpen = false;

  constructor(private router: Router) {}

  toggleMenu(): void {
    this.isMenuOpen = !this.isMenuOpen;
  }

  switchLanguage(): void {
    const currentUrl = this.router.url;
    const segments = currentUrl.split('/');
    const currentLanguage = segments[1] === 'fr' ? 'fr' : 'en';
    const newLanguage = currentLanguage === 'en' ? 'fr' : 'en';
    segments[1] = newLanguage;
    this.router.navigate([segments.join('/')]);
  }
}

import { Component, Inject, LOCALE_ID, PLATFORM_ID } from '@angular/core';
import { CommonModule, isPlatformBrowser } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-layout',
  standalone: true,
  templateUrl: './layout.component.html',
  styleUrls: ['./layout.component.scss'],
  imports: [CommonModule, RouterModule]
})
export class LayoutComponent {
  isMenuOpen = false;

  constructor(
    @Inject(LOCALE_ID) private locale: string,
    @Inject(PLATFORM_ID) private platformId: Object
  ) {}

  toggleMenu(): void {
    this.isMenuOpen = !this.isMenuOpen;
  }

  private currentLanguage(): 'fr' | 'en' {
    if (isPlatformBrowser(this.platformId)) {
      const pathSegments = window.location.pathname.split('/');
      return pathSegments[1] === 'en' ? 'en' : 'fr';
    }
    return this.locale.startsWith('en') ? 'en' : 'fr';
  }

  isFrench(): boolean {
    return this.currentLanguage() === 'fr';
  }

  switchLanguage(): void {
    if (!isPlatformBrowser(this.platformId)) return;

    const url = new URL(window.location.href);
    const pathSegments = url.pathname.split('/');
    const current = pathSegments[1] === 'en' ? 'en' : 'fr';
    const next = current === 'fr' ? 'en' : 'fr';

    if (pathSegments[1] === 'fr' || pathSegments[1] === 'en') {
      pathSegments.splice(1, 1);
    }
    if (next === 'en') {
      pathSegments.splice(1, 0, 'en');
    }

    url.pathname = pathSegments.join('/') || '/';
    window.location.href = url.toString();
  }
}

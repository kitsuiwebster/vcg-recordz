import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-layout',
  standalone: true,
  templateUrl: './layout.component.html',
  styleUrls: ['./layout.component.scss'],
  imports: [RouterModule]
})
export class LayoutComponent {
  isMenuOpen = false;

  toggleMenu(): void {
    this.isMenuOpen = !this.isMenuOpen;
  }

  getCurrentLanguageFlag(): string {
    const currentUrl = window.location.href;
    const url = new URL(currentUrl);
    const pathSegments = url.pathname.split('/');
    
    // Determine current language
    const currentLanguage = pathSegments[1] === 'fr' ? 'fr' : 'en';
    
    // Return the flag of the OTHER language (the one to switch to)
    return currentLanguage === 'en' ? '🇫🇷' : '🇬🇧';
  }

  switchLanguage(): void {
    const currentUrl = window.location.href;
    const url = new URL(currentUrl);
    const pathSegments = url.pathname.split('/');

    // Determine current language
    const currentLanguage = pathSegments[1] === 'fr' ? 'fr' : 'en';

    // Determine new language
    const newLanguage = currentLanguage === 'en' ? 'fr' : 'en';

    // Replace the language in the URL
    pathSegments[1] = newLanguage;

    // Update the pathname and reload the page
    url.pathname = pathSegments.join('/');
    window.location.href = url.toString();
  }
}

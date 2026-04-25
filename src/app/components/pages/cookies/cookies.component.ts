import { Component, OnInit } from '@angular/core';
import { SeoService } from '../../../services/seo.service';

@Component({
  selector: 'app-cookies',
  standalone: true,
  imports: [],
  templateUrl: './cookies.component.html',
  styleUrl: './cookies.component.scss'
})
export class CookiesComponent implements OnInit {
  constructor(private seo: SeoService) {}

  ngOnInit(): void {
    this.seo.update({
      title: $localize`:@@seo.cookies.title:Cookie Policy`,
      description: $localize`:@@seo.cookies.description:How VCG Recordz uses cookies · essential only, no tracking, no advertising.`,
      path: '/cookies'
    });
  }
}

import { Component, OnInit } from '@angular/core';
import { SeoService } from '../../../services/seo.service';

@Component({
  selector: 'app-privacy',
  standalone: true,
  imports: [],
  templateUrl: './privacy.component.html',
  styleUrl: './privacy.component.scss'
})
export class PrivacyComponent implements OnInit {
  constructor(private seo: SeoService) {}

  ngOnInit(): void {
    this.seo.update({
      title: $localize`:@@seo.privacy.title:Privacy Policy`,
      description: $localize`:@@seo.privacy.description:How VCG Recordz collects, uses and protects your personal data under GDPR.`,
      path: '/privacy'
    });
  }
}

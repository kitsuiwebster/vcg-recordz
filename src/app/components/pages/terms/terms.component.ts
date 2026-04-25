import { Component, OnInit } from '@angular/core';
import { SeoService } from '../../../services/seo.service';

@Component({
  selector: 'app-terms',
  standalone: true,
  imports: [],
  templateUrl: './terms.component.html',
  styleUrl: './terms.component.scss'
})
export class TermsComponent implements OnInit {
  constructor(private seo: SeoService) {}

  ngOnInit(): void {
    this.seo.update({
      title: $localize`:@@seo.terms.title:Terms & Conditions`,
      description: $localize`:@@seo.terms.description:Terms of use of the VCG Recordz website, intellectual property, liability and governing law.`,
      path: '/terms'
    });
  }
}

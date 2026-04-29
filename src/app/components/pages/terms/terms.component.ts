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
      title: 'Conditions d\'utilisation',
      description: 'Conditions d\'utilisation du site VCG Recordz · propriété intellectuelle, responsabilité et droit applicable.',
      path: '/terms'
    });
  }
}

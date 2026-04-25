import { Component, OnInit } from '@angular/core';
import { RouterModule } from '@angular/router';
import { SeoService } from '../../../services/seo.service';

@Component({
  selector: 'app-licensing',
  standalone: true,
  imports: [RouterModule],
  templateUrl: './licensing.component.html',
  styleUrl: './licensing.component.scss'
})
export class LicensingComponent implements OnInit {
  constructor(private seo: SeoService) {}

  ngOnInit(): void {
    this.seo.update({
      title: $localize`:@@seo.licensing.title:Licensing`,
      description: $localize`:@@seo.licensing.description:Licensing, sync, beats and clearance policies for the VCG Recordz catalogue.`,
      path: '/licensing'
    });
  }
}

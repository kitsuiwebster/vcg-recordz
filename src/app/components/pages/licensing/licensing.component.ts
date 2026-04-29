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
      title: 'Licensing',
      description: 'Licensing, sync, beats et conditions de licence du catalogue VCG Recordz.',
      path: '/licensing'
    });
  }
}

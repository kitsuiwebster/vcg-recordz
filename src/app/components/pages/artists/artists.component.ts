import { Component, OnInit } from '@angular/core';
import { ArtistCardComponent } from '../../shared/artist-card/artist-card.component';
import { SeoService } from '../../../services/seo.service';

@Component({
  selector: 'app-artists',
  standalone: true,
  imports: [ArtistCardComponent],
  templateUrl: './artists.component.html',
  styleUrl: './artists.component.scss'
})
export class ArtistsComponent implements OnInit {
  constructor(private seo: SeoService) {}

  ngOnInit(): void {
    this.seo.update({
      title: $localize`:@@seo.artists.title:Our Artists`,
      description: $localize`:@@seo.artists.description:Meet the artists distributed by VCG Recordz · Kitsui & Køni, MADPOOF · and our collaborators Cl6ud6, Loupa, Gaxve, CXMET.`,
      path: '/artists'
    });
  }
}

import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { SeoService } from '../../../services/seo.service';
import { EventGalleryComponent } from '../../shared/event-gallery/event-gallery.component';

interface PhotoCredit {
  handle: string;
  role?: string;
}

interface EventEntry {
  date: string;
  title: string;
  location: string;
  lineup: string;
  photos: string[];
  credits: PhotoCredit[];
}

@Component({
  selector: 'app-stage',
  standalone: true,
  imports: [CommonModule, RouterModule, EventGalleryComponent],
  templateUrl: './stage.component.html',
  styleUrl: './stage.component.scss'
})
export class StageComponent implements OnInit {
  events: EventEntry[] = [
    {
      date: 'Août 2025',
      title: 'Portaz Festival',
      location: 'Delley-Portalban · Suisse',
      lineup: 'Loupa · Kitsui · Køni · Biaco · Baptiste (DJ)',
      photos: Array.from({ length: 14 }, (_, i) => `/images/stage/events/portaz_${String(i + 1).padStart(2, '0')}.webp`),
      credits: [
        { handle: 'e_theillard' },
        { handle: 'romeo_ballara', role: 'vidéo' },
      ],
    },
    {
      date: 'Juil. 2025',
      title: 'Trevad Festival',
      location: "Ergué-Gabéric · Bretagne · Salle L'Athenaz",
      lineup: 'Loupa · Kitsui · Køni · Djoolias (DJ)',
      photos: Array.from({ length: 13 }, (_, i) => `/images/stage/events/trevad_${String(i + 1).padStart(2, '0')}.webp`),
      credits: [
        { handle: 'johann_marrec' },
        { handle: 'tom._mvl' },
        { handle: 'fanny_mbn' },
      ],
    },
    {
      date: 'Juin 2025',
      title: 'Fête de la musique de Chambéry',
      location: 'Chambéry · France',
      lineup: 'Loupa · Kitsui · Køni · Gryffon · Gary (DJ)',
      photos: Array.from({ length: 17 }, (_, i) => `/images/stage/events/chambery_${String(i + 1).padStart(2, '0')}.webp`),
      credits: [
        { handle: 'dylan.yagami' },
        { handle: 'romeo_ballara', role: 'vidéo' },
      ],
    },
    {
      date: 'Sept. 2025',
      title: 'Fête de la musique de Morges',
      location: 'Morges · Suisse',
      lineup: 'Loupa · Kitsui · Køni · Baptiste (DJ)',
      photos: Array.from({ length: 19 }, (_, i) => `/images/stage/events/morges_${String(i + 1).padStart(2, '0')}.webp`),
      credits: [{ handle: 'dylan.yagami' }],
    },
  ];

  constructor(private seo: SeoService) {}

  ngOnInit(): void {
    this.seo.update({
      title: $localize`:@@seo.stage.title:VCG on Stage`,
      description: $localize`:@@seo.stage.description:VCG Recordz on stage · live performances, DJ sets and booking for our artists and crew across France and Europe.`,
      path: '/stage'
    });
  }

  igUrl(handle: string): string {
    return `https://www.instagram.com/${handle}/`;
  }
}

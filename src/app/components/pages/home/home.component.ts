import { Component, OnInit } from '@angular/core';
import { RouterModule } from '@angular/router';
import { SeoService } from '../../../services/seo.service';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [RouterModule],
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent implements OnInit {
  constructor(private seo: SeoService) {}

  ngOnInit(): void {
    this.seo.update({
      title: 'Label Musical Indépendant Européen',
      description: 'VCG Recordz est un label musical indépendant basé à Valleiry · rap, trap, breakcore, drum & bass. Distribution, beatmaking, mixage, booking live.',
      path: '/',
      type: 'music.group'
    });

    this.seo.setJsonLd({
      '@context': 'https://schema.org',
      '@type': 'MusicGroup',
      name: 'VCG Recordz',
      url: 'https://vcgrecordz.eu',
      logo: 'https://vcgrecordz.eu/logo.png',
      image: 'https://vcgrecordz.eu/banner.jpg',
      foundingDate: "2024",
      foundingLocation: {
        '@type': 'Place',
        name: 'Valleiry, Haute-Savoie'
      },
      genre: ['Hip Hop', 'Rap', 'Trap', 'Drum and Bass', 'Breakcore', 'Phonk'],
      member: [
        { '@type': 'Person', name: 'Kitsui' },
        { '@type': 'Person', name: 'Biggy' },
        { '@type': 'Person', name: 'Køni' }
      ],
      sameAs: [
        'https://www.instagram.com/vcg.recordz',
        'https://www.youtube.com/@vcgrecordz'
      ]
    });
  }
}

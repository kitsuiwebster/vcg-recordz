import { Component, OnInit } from '@angular/core';
import { RouterModule } from '@angular/router';
import { SeoService } from '../../../services/seo.service';

@Component({
  selector: 'app-about',
  standalone: true,
  imports: [RouterModule],
  templateUrl: './about.component.html',
  styleUrl: './about.component.scss'
})
export class AboutComponent implements OnInit {
  constructor(private seo: SeoService) {}

  ngOnInit(): void {
    this.seo.update({
      title: $localize`:@@seo.about.title:Notre histoire`,
      description: $localize`:@@seo.about.description:De la chambre d'ado au label structuré · l'histoire de VCG Recordz depuis 2024.`,
      path: '/about'
    });
  }
}

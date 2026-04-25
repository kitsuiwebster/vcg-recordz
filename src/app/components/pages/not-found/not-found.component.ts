import { Component, OnInit } from '@angular/core';
import { RouterModule } from '@angular/router';
import { SeoService } from '../../../services/seo.service';

@Component({
  selector: 'app-not-found',
  standalone: true,
  imports: [RouterModule],
  templateUrl: './not-found.component.html',
  styleUrl: './not-found.component.scss'
})
export class NotFoundComponent implements OnInit {
  constructor(private seo: SeoService) {}

  ngOnInit(): void {
    this.seo.update({
      title: $localize`:@@seo.notfound.title:Page Not Found`,
      description: $localize`:@@seo.notfound.description:This page does not exist. Return to the VCG Recordz homepage.`,
      path: '/not-found'
    });
  }
}

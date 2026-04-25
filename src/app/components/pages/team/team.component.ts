import { Component, OnInit } from '@angular/core';
import { RouterModule } from '@angular/router';
import { SeoService } from '../../../services/seo.service';

@Component({
  selector: 'app-team',
  standalone: true,
  imports: [RouterModule],
  templateUrl: './team.component.html',
  styleUrl: './team.component.scss'
})
export class TeamComponent implements OnInit {
  constructor(private seo: SeoService) {}

  ngOnInit(): void {
    this.seo.update({
      title: $localize`:@@seo.team.title:Our Team`,
      description: $localize`:@@seo.team.description:The VCG Recordz team · Kitsui, Biggy, Køni · and the VCG Production beatmakers: Oddgyes, Shidozz, DMB, NVSDV, No$$if.`,
      path: '/team'
    });
  }
}

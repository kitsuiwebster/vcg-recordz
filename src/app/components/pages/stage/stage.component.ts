import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { SeoService } from '../../../services/seo.service';
import { EventGalleryComponent } from '../../shared/event-gallery/event-gallery.component';
import { EventEntry, GalleryService } from '../../../services/gallery.service';

@Component({
  selector: 'app-stage',
  standalone: true,
  imports: [CommonModule, RouterModule, EventGalleryComponent],
  templateUrl: './stage.component.html',
  styleUrl: './stage.component.scss'
})
export class StageComponent implements OnInit {
  events: EventEntry[];

  constructor(private seo: SeoService, private gallery: GalleryService) {
    this.events = this.gallery.events.filter((e) => !e.extra);
  }

  ngOnInit(): void {
    this.seo.update({
      title: 'VCG on Stage',
      description: 'VCG Recordz sur scène · live, DJ sets et booking pour nos artistes et notre crew en France et en Europe.',
      path: '/stage'
    });
  }

  igUrl(handle: string): string {
    return `https://www.instagram.com/${handle}/`;
  }
}

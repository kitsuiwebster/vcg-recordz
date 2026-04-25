import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-artist-card',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './artist-card.component.html',
  styleUrl: './artist-card.component.scss'
})
export class ArtistCardComponent {
  @Input() imageSrc!: string;
  @Input() imageAlt = '';
  @Input() reversed = false;
}

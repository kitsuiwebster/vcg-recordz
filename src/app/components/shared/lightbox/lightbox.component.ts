import {
  Component,
  EventEmitter,
  HostListener,
  Inject,
  Input,
  OnChanges,
  OnDestroy,
  Output,
  PLATFORM_ID,
  SimpleChanges,
} from '@angular/core';
import { CommonModule, isPlatformBrowser } from '@angular/common';
import { GalleryPhoto, GalleryService } from '../../../services/gallery.service';

@Component({
  selector: 'app-lightbox',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './lightbox.component.html',
  styleUrl: './lightbox.component.scss',
})
export class LightboxComponent implements OnChanges, OnDestroy {
  @Input({ required: true }) photos: GalleryPhoto[] = [];
  @Input() open = false;
  @Output() openChange = new EventEmitter<boolean>();
  @Input() index = 0;
  @Output() indexChange = new EventEmitter<number>();

  private touchStartX = 0;
  private touchStartY = 0;
  downloading = false;

  constructor(
    private gallery: GalleryService,
    @Inject(PLATFORM_ID) private platformId: Object,
  ) {}

  ngOnChanges(changes: SimpleChanges): void {
    if (!isPlatformBrowser(this.platformId)) return;
    if (changes['open']) {
      document.body.style.overflow = this.open ? 'hidden' : '';
    }
    if (this.open && (changes['index'] || changes['open'])) {
      this.preloadAdjacent();
    }
  }

  ngOnDestroy(): void {
    if (isPlatformBrowser(this.platformId)) {
      document.body.style.overflow = '';
    }
  }

  get current(): GalleryPhoto | undefined {
    return this.photos[this.index];
  }

  close(): void {
    this.open = false;
    this.openChange.emit(false);
  }

  prev(): void {
    if (this.photos.length === 0) return;
    const next = (this.index - 1 + this.photos.length) % this.photos.length;
    this.index = next;
    this.indexChange.emit(next);
    this.preloadAdjacent();
  }

  next(): void {
    if (this.photos.length === 0) return;
    const next = (this.index + 1) % this.photos.length;
    this.index = next;
    this.indexChange.emit(next);
    this.preloadAdjacent();
  }

  onBackdropClick(event: MouseEvent): void {
    if (event.target === event.currentTarget) {
      this.close();
    }
  }

  onTouchStart(event: TouchEvent): void {
    const t = event.touches[0];
    this.touchStartX = t.clientX;
    this.touchStartY = t.clientY;
  }

  onTouchEnd(event: TouchEvent): void {
    const t = event.changedTouches[0];
    const dx = t.clientX - this.touchStartX;
    const dy = t.clientY - this.touchStartY;
    if (Math.abs(dx) < 50 || Math.abs(dx) < Math.abs(dy)) return;
    if (dx > 0) this.prev();
    else this.next();
  }

  @HostListener('document:keydown', ['$event'])
  onKeydown(event: KeyboardEvent): void {
    if (!this.open) return;
    if (event.key === 'ArrowLeft') {
      event.preventDefault();
      this.prev();
    } else if (event.key === 'ArrowRight') {
      event.preventDefault();
      this.next();
    } else if (event.key === 'Escape') {
      event.preventDefault();
      this.close();
    }
  }

  async download(photo: GalleryPhoto): Promise<void> {
    if (!isPlatformBrowser(this.platformId) || this.downloading) return;
    this.downloading = true;
    try {
      await this.gallery.downloadPhotoAsJpg(photo);
    } finally {
      this.downloading = false;
    }
  }

  private preloadAdjacent(): void {
    if (!isPlatformBrowser(this.platformId)) return;
    const targets = [this.index - 1, this.index + 1]
      .map((i) => (i + this.photos.length) % this.photos.length)
      .map((i) => this.photos[i]?.src)
      .filter((src): src is string => Boolean(src));
    for (const src of targets) {
      const img = new Image();
      img.src = src;
    }
  }
}

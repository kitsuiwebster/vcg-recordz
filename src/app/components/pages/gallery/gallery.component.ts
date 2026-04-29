import {
  AfterViewInit,
  Component,
  ElementRef,
  HostListener,
  Inject,
  OnDestroy,
  OnInit,
  PLATFORM_ID,
  ViewChild,
} from '@angular/core';
import { CommonModule, isPlatformBrowser } from '@angular/common';
import { GalleryPhoto, GalleryService } from '../../../services/gallery.service';
import { LightboxComponent } from '../../shared/lightbox/lightbox.component';
import { SeoService } from '../../../services/seo.service';

interface LayoutItem {
  photo: GalleryPhoto;
  globalIndex: number;
  width: number;
  height: number;
}

interface LayoutRow {
  items: LayoutItem[];
  height: number;
}

const HORIZONTAL_GAP = 6;
const VERTICAL_GAP = 6;

@Component({
  selector: 'app-gallery',
  standalone: true,
  imports: [CommonModule, LightboxComponent],
  templateUrl: './gallery.component.html',
  styleUrl: './gallery.component.scss',
})
export class GalleryComponent implements OnInit, AfterViewInit, OnDestroy {
  @ViewChild('grid', { static: false }) gridRef?: ElementRef<HTMLElement>;

  photos: GalleryPhoto[] = [];
  rows: LayoutRow[] = [];
  selectedIndex = 0;
  lightboxOpen = false;
  ready = false;

  private aspectRatios = new Map<string, number>();
  private resizeTimeout: ReturnType<typeof setTimeout> | null = null;

  constructor(
    private gallery: GalleryService,
    private seo: SeoService,
    @Inject(PLATFORM_ID) private platformId: Object,
  ) {}

  ngOnInit(): void {
    this.photos = this.gallery.getAllPhotos({ shuffle: true });
    this.seo.update({
      title: 'Galerie',
      description: 'Galerie photo de VCG Recordz · une sélection de moments capturés autour du collectif.',
      path: '/gallery',
    });
  }

  async ngAfterViewInit(): Promise<void> {
    if (!isPlatformBrowser(this.platformId)) return;
    await this.loadAspectRatios();
    this.layout();
    this.ready = true;
  }

  ngOnDestroy(): void {
    if (this.resizeTimeout) clearTimeout(this.resizeTimeout);
  }

  @HostListener('window:resize')
  onResize(): void {
    if (!isPlatformBrowser(this.platformId)) return;
    if (this.resizeTimeout) clearTimeout(this.resizeTimeout);
    this.resizeTimeout = setTimeout(() => this.layout(), 100);
  }

  open(globalIndex: number): void {
    this.selectedIndex = globalIndex;
    this.lightboxOpen = true;
  }

  async download(event: MouseEvent, photo: GalleryPhoto): Promise<void> {
    event.stopPropagation();
    await this.gallery.downloadPhotoAsJpg(photo);
  }

  private async loadAspectRatios(): Promise<void> {
    const tasks = this.photos.map(async (p) => {
      try {
        const img = new Image();
        img.src = p.src;
        await img.decode();
        const ar = img.naturalHeight > 0 ? img.naturalWidth / img.naturalHeight : 1;
        this.aspectRatios.set(p.src, ar);
      } catch {
        this.aspectRatios.set(p.src, 4 / 3);
      }
    });
    await Promise.all(tasks);
  }

  private layout(): void {
    const container = this.gridRef?.nativeElement;
    if (!container) return;

    const containerWidth = container.clientWidth;
    if (containerWidth <= 0) return;

    const targetHeight = this.getTargetRowHeight();
    const rows: LayoutRow[] = [];
    let currentItems: { photo: GalleryPhoto; globalIndex: number; ar: number }[] = [];
    let arSum = 0;

    for (let i = 0; i < this.photos.length; i++) {
      const photo = this.photos[i];
      const ar = this.aspectRatios.get(photo.src) ?? 4 / 3;
      currentItems.push({ photo, globalIndex: i, ar });
      arSum += ar;

      const naturalRowWidth = arSum * targetHeight + HORIZONTAL_GAP * (currentItems.length - 1);
      if (naturalRowWidth >= containerWidth) {
        rows.push(this.finalizeJustifiedRow(currentItems, arSum, containerWidth));
        currentItems = [];
        arSum = 0;
      }
    }

    if (currentItems.length > 0) {
      rows.push(this.finalizeLastRow(currentItems, targetHeight, containerWidth));
    }

    this.rows = rows;
  }

  private finalizeJustifiedRow(
    items: { photo: GalleryPhoto; globalIndex: number; ar: number }[],
    arSum: number,
    containerWidth: number,
  ): LayoutRow {
    const totalGap = HORIZONTAL_GAP * (items.length - 1);
    const availableWidth = containerWidth - totalGap;
    const rowHeight = availableWidth / arSum;
    return {
      height: rowHeight,
      items: items.map((it) => ({
        photo: it.photo,
        globalIndex: it.globalIndex,
        width: it.ar * rowHeight,
        height: rowHeight,
      })),
    };
  }

  private finalizeLastRow(
    items: { photo: GalleryPhoto; globalIndex: number; ar: number }[],
    targetHeight: number,
    containerWidth: number,
  ): LayoutRow {
    const totalGap = HORIZONTAL_GAP * (items.length - 1);
    const naturalWidth = items.reduce((sum, it) => sum + it.ar * targetHeight, 0) + totalGap;
    if (naturalWidth >= containerWidth * 0.7) {
      const arSum = items.reduce((sum, it) => sum + it.ar, 0);
      const availableWidth = containerWidth - totalGap;
      const rowHeight = availableWidth / arSum;
      return {
        height: rowHeight,
        items: items.map((it) => ({
          photo: it.photo,
          globalIndex: it.globalIndex,
          width: it.ar * rowHeight,
          height: rowHeight,
        })),
      };
    }
    return {
      height: targetHeight,
      items: items.map((it) => ({
        photo: it.photo,
        globalIndex: it.globalIndex,
        width: it.ar * targetHeight,
        height: targetHeight,
      })),
    };
  }

  private getTargetRowHeight(): number {
    if (!isPlatformBrowser(this.platformId)) return 280;
    const w = window.innerWidth;
    if (w < 640) return 180;
    if (w < 1024) return 240;
    return 320;
  }
}

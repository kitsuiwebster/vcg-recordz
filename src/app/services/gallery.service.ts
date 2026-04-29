import { Inject, Injectable, PLATFORM_ID } from '@angular/core';
import { isPlatformBrowser } from '@angular/common';

export interface PhotoCredit {
  handle: string;
  role?: string;
}

export interface EventEntry {
  slug: string;
  year: number;
  date?: string;
  title: string;
  location?: string;
  lineup?: string;
  photos: string[];
  credits: PhotoCredit[];
  extra?: boolean;
}

export interface GalleryPhoto {
  src: string;
  eventSlug: string;
  eventTitle: string;
  eventYear: number;
  index: number;
  photographers: string[];
}

@Injectable({ providedIn: 'root' })
export class GalleryService {
  readonly events: EventEntry[] = [
    {
      slug: 'portaz',
      year: 2025,
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
      slug: 'trevad',
      year: 2025,
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
      slug: 'chambery',
      year: 2025,
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
      slug: 'morges',
      year: 2025,
      date: 'Sept. 2025',
      title: 'Fête de la musique de Morges',
      location: 'Morges · Suisse',
      lineup: 'Loupa · Kitsui · Køni · Baptiste (DJ)',
      photos: Array.from({ length: 19 }, (_, i) => `/images/stage/events/morges_${String(i + 1).padStart(2, '0')}.webp`),
      credits: [{ handle: 'dylan.yagami' }],
    },
    {
      slug: 'chatnoir',
      year: 2025,
      title: 'Chat Noir',
      photos: ['/images/stage/events/chatnoir_01.jpg'],
      credits: [{ handle: 'ader_alaa' }],
      extra: true,
    },
    {
      slug: 'vcg-crew',
      year: 2025,
      title: 'VCG Crew',
      photos: ['/images/stage/crew2.jpg'],
      credits: [{ handle: 'dylan.yagami' }],
      extra: true,
    },
  ];

  constructor(@Inject(PLATFORM_ID) private platformId: Object) {}

  getAllPhotos(options: { shuffle?: boolean } = {}): GalleryPhoto[] {
    const all: GalleryPhoto[] = [];
    for (const event of this.events) {
      const photographers = this.toPhotographers(event.credits);
      for (const src of event.photos) {
        all.push({
          src,
          eventSlug: event.slug,
          eventTitle: event.title,
          eventYear: event.year,
          index: this.extractIndex(src),
          photographers,
        });
      }
    }
    if (options.shuffle) this.shuffleInPlace(all);
    return all;
  }

  getEventBySlug(slug: string): EventEntry | undefined {
    return this.events.find((e) => e.slug === slug);
  }

  buildDownloadFilename(photo: GalleryPhoto): string {
    const indexPadded = String(photo.index).padStart(2, '0');
    const handles = photo.photographers
      .map((h) => h.replace(/\./g, ''))
      .join('-');
    return `vcg-recordz_${photo.eventSlug}_${indexPadded}_${handles}.jpg`;
  }

  async downloadPhotoAsJpg(photo: GalleryPhoto): Promise<void> {
    if (!isPlatformBrowser(this.platformId)) return;
    const res = await fetch(photo.src);
    const sourceBlob = await res.blob();
    const jpgBlob = await this.convertToJpg(sourceBlob);
    const url = URL.createObjectURL(jpgBlob);
    const a = document.createElement('a');
    a.href = url;
    a.download = this.buildDownloadFilename(photo);
    document.body.appendChild(a);
    a.click();
    a.remove();
    URL.revokeObjectURL(url);
  }

  private async convertToJpg(blob: Blob): Promise<Blob> {
    const bitmap = await this.loadBitmap(blob);
    const canvas = document.createElement('canvas');
    canvas.width = bitmap.width;
    canvas.height = bitmap.height;
    const ctx = canvas.getContext('2d');
    if (!ctx) return blob;
    ctx.fillStyle = '#000000';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(bitmap as CanvasImageSource, 0, 0);
    return new Promise<Blob>((resolve, reject) => {
      canvas.toBlob(
        (b) => (b ? resolve(b) : reject(new Error('toBlob failed'))),
        'image/jpeg',
        0.92,
      );
    });
  }

  private async loadBitmap(blob: Blob): Promise<ImageBitmap | HTMLImageElement> {
    if (typeof createImageBitmap === 'function') {
      try {
        return await createImageBitmap(blob);
      } catch {
        // fall through to HTMLImageElement path
      }
    }
    const url = URL.createObjectURL(blob);
    try {
      const img = new Image();
      img.src = url;
      await img.decode();
      return img;
    } finally {
      URL.revokeObjectURL(url);
    }
  }

  private shuffleInPlace<T>(arr: T[]): void {
    for (let i = arr.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
  }

  private toPhotographers(credits: PhotoCredit[]): string[] {
    return credits
      .filter((c) => c.role !== 'vidéo' && c.role !== 'video')
      .map((c) => c.handle);
  }

  private extractIndex(src: string): number {
    const filename = src.split('/').pop() ?? '';
    const match = filename.match(/(\d+)\.[a-zA-Z0-9]+$/);
    return match ? parseInt(match[1], 10) : 1;
  }
}

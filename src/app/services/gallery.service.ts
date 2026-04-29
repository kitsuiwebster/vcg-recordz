import { Inject, Injectable, PLATFORM_ID } from '@angular/core';
import { isPlatformBrowser } from '@angular/common';
import photoData from '../data/photos.json';

export type PhotoType = 'live' | 'studio' | 'crew' | string;
export type PhotoOrientation = 'portrait' | 'landscape';

export interface Photo {
  id: string;
  event: string;
  year: number;
  type: PhotoType;
  photographer: string;
  orientation: PhotoOrientation;
  path: string;
}

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
  photographer: string;
}

const PHOTOS: Photo[] = photoData.photos as Photo[];

@Injectable({ providedIn: 'root' })
export class GalleryService {
  readonly photos: Photo[] = PHOTOS;

  private readonly eventsMeta: Omit<EventEntry, 'photos'>[] = [
    {
      slug: 'portaz',
      year: 2025,
      date: 'Août 2025',
      title: 'Portaz Festival',
      location: 'Delley-Portalban · Suisse',
      lineup: 'Loupa · Kitsui · Køni · Biaco · Baptiste (DJ)',
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
      credits: [{ handle: 'dylan.yagami' }],
    },
    {
      slug: 'chatnoir',
      year: 2025,
      title: 'Chat Noir',
      credits: [{ handle: 'ader_alaa' }],
      extra: true,
    },
    {
      slug: 'vcg-crew',
      year: 2025,
      title: 'VCG Crew',
      credits: [{ handle: 'dylan.yagami' }],
      extra: true,
    },
  ];

  constructor(@Inject(PLATFORM_ID) private platformId: Object) {}

  get events(): EventEntry[] {
    return this.eventsMeta.map((meta) => ({
      ...meta,
      photos: this.photos.filter((p) => p.event === meta.title).map((p) => p.path),
    }));
  }

  getEventBySlug(slug: string): EventEntry | undefined {
    return this.events.find((e) => e.slug === slug);
  }

  getPhotoById(id: string): Photo | undefined {
    return this.photos.find((p) => p.id === id);
  }

  getPhotosByType(type: PhotoType): Photo[] {
    return this.photos.filter((p) => p.type === type);
  }

  getPhotosByEvent(eventTitle: string): Photo[] {
    return this.photos.filter((p) => p.event === eventTitle);
  }

  getAllPhotos(options: { shuffle?: boolean } = {}): GalleryPhoto[] {
    const all: GalleryPhoto[] = this.photos.map((p) => ({
      src: p.path,
      eventSlug: this.slugForEventTitle(p.event),
      eventTitle: p.event,
      eventYear: p.year,
      index: this.extractIndexFromPath(p.path),
      photographer: p.photographer,
    }));
    if (options.shuffle) this.shuffleInPlace(all);
    return all;
  }

  buildDownloadFilename(photo: GalleryPhoto): string {
    const indexPadded = String(photo.index).padStart(2, '0');
    const handle = photo.photographer.replace(/\./g, '');
    return `vcg-recordz_${photo.eventSlug}_${indexPadded}_${handle}.jpg`;
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
        // fall through
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

  private slugForEventTitle(title: string): string {
    return this.eventsMeta.find((e) => e.title === title)?.slug ?? 'photo';
  }

  private extractIndexFromPath(path: string): number {
    const filename = path.split('/').pop() ?? '';
    const match = filename.match(/(\d+)\.[a-zA-Z0-9]+$/);
    return match ? parseInt(match[1], 10) : 1;
  }
}

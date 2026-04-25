import { Component, Input, OnDestroy, OnInit, Inject, PLATFORM_ID } from '@angular/core';
import { CommonModule, isPlatformBrowser } from '@angular/common';

interface Slot {
  a: string;
  b: string;
  showA: boolean;
  paused: boolean;
  timeout?: ReturnType<typeof setTimeout>;
}

@Component({
  selector: 'app-event-gallery',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './event-gallery.component.html',
  styleUrl: './event-gallery.component.scss'
})
export class EventGalleryComponent implements OnInit, OnDestroy {
  @Input({ required: true }) photos: string[] = [];
  @Input() alt = '';
  @Input() slotCount = 4;
  @Input() minMs = 4000;
  @Input() maxMs = 6000;

  slots: Slot[] = [];

  constructor(@Inject(PLATFORM_ID) private platformId: Object) {}

  ngOnInit(): void {
    if (this.photos.length === 0) return;

    const initial = this.pickInitial(this.slotCount);
    this.slots = initial.map((src) => ({
      a: src,
      b: src,
      showA: true,
      paused: false
    }));

    if (isPlatformBrowser(this.platformId)) {
      this.slots.forEach((_, i) => this.scheduleSlot(i, 1000 + i * 600));
    }
  }

  ngOnDestroy(): void {
    this.slots.forEach((s) => s.timeout && clearTimeout(s.timeout));
  }

  pause(i: number): void {
    const slot = this.slots[i];
    if (!slot) return;
    slot.paused = true;
    if (slot.timeout) clearTimeout(slot.timeout);
  }

  resume(i: number): void {
    const slot = this.slots[i];
    if (!slot) return;
    slot.paused = false;
    this.scheduleSlot(i, this.randomDelay());
  }

  private pickInitial(n: number): string[] {
    const pool = [...this.photos];
    const out: string[] = [];
    while (out.length < n) {
      if (pool.length === 0) {
        out.push(this.photos[out.length % this.photos.length]);
      } else {
        const idx = Math.floor(Math.random() * pool.length);
        out.push(pool.splice(idx, 1)[0]);
      }
    }
    return out;
  }

  private scheduleSlot(i: number, delay: number): void {
    const slot = this.slots[i];
    if (!slot || slot.paused) return;
    slot.timeout = setTimeout(() => this.cycleSlot(i), delay);
  }

  private cycleSlot(i: number): void {
    const slot = this.slots[i];
    if (!slot || slot.paused) return;

    const visible = this.slots.map((s) => (s.showA ? s.a : s.b));
    const candidates = this.photos.filter((p) => !visible.includes(p));
    const pool = candidates.length > 0 ? candidates : this.photos;
    const next = pool[Math.floor(Math.random() * pool.length)];

    if (slot.showA) {
      slot.b = next;
      slot.showA = false;
    } else {
      slot.a = next;
      slot.showA = true;
    }

    this.scheduleSlot(i, this.randomDelay());
  }

  private randomDelay(): number {
    return this.minMs + Math.floor(Math.random() * (this.maxMs - this.minMs));
  }
}

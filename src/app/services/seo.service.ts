import { Injectable, Inject, LOCALE_ID } from '@angular/core';
import { Meta, Title } from '@angular/platform-browser';
import { DOCUMENT } from '@angular/common';

export interface SeoConfig {
  title: string;
  description: string;
  path?: string;
  image?: string;
  type?: 'website' | 'article' | 'music.group';
}

const SITE_URL = 'https://vcgrecordz.eu';
const DEFAULT_IMAGE = `${SITE_URL}/banner.jpg`;
const BRAND = 'VCG Recordz';

@Injectable({ providedIn: 'root' })
export class SeoService {
  constructor(
    private titleService: Title,
    private meta: Meta,
    @Inject(DOCUMENT) private doc: Document,
    @Inject(LOCALE_ID) private locale: string
  ) {}

  update(config: SeoConfig): void {
    const fullTitle = `${config.title} | ${BRAND}`;
    const image = config.image ?? DEFAULT_IMAGE;
    const isEn = this.locale.startsWith('en');
    const localePrefix = isEn ? '/en' : '';
    const url = `${SITE_URL}${localePrefix}${config.path ?? ''}`;
    const type = config.type ?? 'website';
    const lang = isEn ? 'en_US' : 'fr_FR';

    this.titleService.setTitle(fullTitle);

    this.setTag('name', 'description', config.description);
    this.setTag('name', 'robots', 'index, follow');
    this.setTag('name', 'author', BRAND);

    this.setTag('property', 'og:title', fullTitle);
    this.setTag('property', 'og:description', config.description);
    this.setTag('property', 'og:image', image);
    this.setTag('property', 'og:url', url);
    this.setTag('property', 'og:type', type);
    this.setTag('property', 'og:site_name', BRAND);
    this.setTag('property', 'og:locale', lang);

    this.setTag('name', 'twitter:card', 'summary_large_image');
    this.setTag('name', 'twitter:title', fullTitle);
    this.setTag('name', 'twitter:description', config.description);
    this.setTag('name', 'twitter:image', image);

    this.setCanonical(url);
    this.setHtmlLang(isEn ? 'en' : 'fr');
    this.setHreflang(config.path ?? '');
  }

  private setHreflang(path: string): void {
    this.doc.querySelectorAll("link[rel='alternate'][hreflang]").forEach((el) => el.remove());
    const variants: { lang: string; href: string }[] = [
      { lang: 'fr', href: `${SITE_URL}${path}` },
      { lang: 'en', href: `${SITE_URL}/en${path}` },
      { lang: 'x-default', href: `${SITE_URL}${path}` }
    ];
    for (const v of variants) {
      const link = this.doc.createElement('link');
      link.setAttribute('rel', 'alternate');
      link.setAttribute('hreflang', v.lang);
      link.setAttribute('href', v.href);
      this.doc.head.appendChild(link);
    }
  }

  setJsonLd(data: object, id = 'seo-jsonld'): void {
    const existing = this.doc.getElementById(id);
    if (existing) existing.remove();
    const script = this.doc.createElement('script');
    script.type = 'application/ld+json';
    script.id = id;
    script.text = JSON.stringify(data);
    this.doc.head.appendChild(script);
  }

  private setTag(attr: 'name' | 'property', key: string, content: string): void {
    const selector = `${attr}="${key}"`;
    if (this.meta.getTag(selector)) {
      this.meta.updateTag({ [attr]: key, content });
    } else {
      this.meta.addTag({ [attr]: key, content });
    }
  }

  private setCanonical(url: string): void {
    let link = this.doc.querySelector("link[rel='canonical']") as HTMLLinkElement | null;
    if (!link) {
      link = this.doc.createElement('link');
      link.setAttribute('rel', 'canonical');
      this.doc.head.appendChild(link);
    }
    link.setAttribute('href', url);
  }

  private setHtmlLang(lang: string): void {
    this.doc.documentElement.setAttribute('lang', lang);
  }
}

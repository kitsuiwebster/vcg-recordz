# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the VCG-Recordz website, an Angular 18 application for a music/record label. The application features:
- Server-Side Rendering (SSR) with Angular Universal
- Internationalization (i18n) support for English and French
- Standalone components (no NgModules)
- Tailwind CSS for styling

## Essential Commands

```bash
# Development
npm start                    # Start development server (ng serve)
yarn start                   # Alternative using yarn

# Building
npm run build               # Production build
npm run watch              # Development build with watch mode

# Testing
npm test                   # Run unit tests with Karma

# SSR
npm run serve:ssr:vcg-website  # Serve the SSR build
```

## Architecture Overview

### Component Structure
All components follow the standalone pattern and are organized under `src/app/components/`:
- `layout/` - Main layout wrapper with navigation and language switching
- `pages/` - Individual page components (home, about, artists, services, etc.)

Each component has consistent file structure: `.ts`, `.html`, `.scss`, `.spec.ts`

### Routing
Routes are defined in `src/app/app.routes.ts`. The application uses path-based routing with the Layout component as the wrapper containing the router outlet.

### Internationalization
- Source language: English (`src/locale/messages.xlf`)
- Translation: French (`src/locale/messages.fr.xlf`)
- Language switching is handled in the Layout component via URL manipulation
- URLs follow pattern: `/` for English, `/fr/` for French

### Styling
- Component styles use SCSS
- Global utility classes use Tailwind CSS
- Custom Tailwind config extends with:
  - `sm900` breakpoint at 900px
  - `xxs` font size at 0.625rem

### Key Dependencies
- Angular 18.2.0 with SSR
- SweetAlert2 for modals/alerts
- Tailwind CSS for utility styling
- Express for SSR server

## Important Configuration Notes

1. **TypeScript Configuration**: 
   - `noImplicitOverride` is set to `false` to handle RxJS compatibility
   - Strict mode is enabled

2. **Development Server**:
   - Localization is disabled in dev mode (only one locale at a time)
   - Default port for `ng serve` is 4200

3. **Assets**: All static assets are in the `public/` directory, organized by type (images/artists, images/beatmakers, etc.)

4. **No Linting**: The project doesn't have ESLint or TSLint configured. Code quality relies on TypeScript strict mode.
#!/usr/bin/env bash
# Build + flatten dual-locale Angular output for static hosting (Hostinger, Netlify, etc.)
# After this script: dist/deploy/ contains FR at root, EN under /en/, ready to upload.

set -e

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
BUILD_DIR="$ROOT_DIR/dist/vcg-website/browser"
DEPLOY_DIR="$ROOT_DIR/dist/deploy"

if [ ! -d "$BUILD_DIR/fr" ] || [ ! -d "$BUILD_DIR/en" ]; then
  echo "Error: Run 'yarn build' first." >&2
  exit 1
fi

rm -rf "$DEPLOY_DIR"
mkdir -p "$DEPLOY_DIR"

echo "→ Copying FR build to root..."
cp -r "$BUILD_DIR/fr/." "$DEPLOY_DIR/"

echo "→ Copying EN build to /en/..."
mkdir -p "$DEPLOY_DIR/en"
cp -r "$BUILD_DIR/en/." "$DEPLOY_DIR/en/"

echo "→ Copying root assets (.htaccess, robots.txt, sitemap.xml)..."
for f in .htaccess robots.txt sitemap.xml favicon.ico; do
  if [ -f "$BUILD_DIR/$f" ] && [ ! -f "$DEPLOY_DIR/$f" ]; then
    cp "$BUILD_DIR/$f" "$DEPLOY_DIR/$f"
  fi
done

echo ""
echo "✅ Deploy ready: $DEPLOY_DIR"
echo "   Upload its content to public_html/ on Hostinger."
echo ""
ls -la "$DEPLOY_DIR" | head -30

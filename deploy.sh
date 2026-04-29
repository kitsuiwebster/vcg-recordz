#!/usr/bin/env bash
# Build Angular output for static hosting (Hostinger, Netlify, etc.)
# After this script: dist/deploy/ contains the FR site, ready to upload.

set -e

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
BUILD_DIR="$ROOT_DIR/dist/vcg-website/browser"
DEPLOY_DIR="$ROOT_DIR/dist/deploy"

if [ ! -d "$BUILD_DIR" ]; then
  echo "Error: Run 'yarn build' first." >&2
  exit 1
fi

rm -rf "$DEPLOY_DIR"
mkdir -p "$DEPLOY_DIR"

echo "→ Copying build to deploy folder..."
cp -r "$BUILD_DIR/." "$DEPLOY_DIR/"

echo "→ Fixing <base href> in all index.html files..."
find "$DEPLOY_DIR" -name "index.html" \
  -exec sed -i 's|<base href="[^"]*"[[:space:]]*/*>|<base href="/">|g' {} \;

echo ""
echo "✅ Deploy ready: $DEPLOY_DIR"
echo "   Upload its content to public_html/ on Hostinger."
echo ""
ls -la "$DEPLOY_DIR" | head -30

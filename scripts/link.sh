#!/usr/bin/env bash
# Symlink every skill in skills/<category>/<name> into each agent skills dir.
# Safe to re-run: existing symlinks are refreshed, real directories are left alone.
set -euo pipefail
repo="$(cd "$(dirname "$0")/.." && pwd)"
targets=("${@:-$HOME/.claude/skills}")

for target in "${targets[@]}"; do
  mkdir -p "$target"
  for skill in "$repo"/skills/*/*/; do
    name="$(basename "$skill")"
    dest="$target/$name"
    if [ -e "$dest" ] && [ ! -L "$dest" ]; then
      echo "skip  $dest (real directory, move or delete it first)"
      continue
    fi
    ln -sfn "${skill%/}" "$dest"
    echo "link  $dest -> ${skill%/}"
  done
  # Drop links to skills that no longer exist in the repo.
  for link in "$target"/*; do
    if [ -L "$link" ] && [[ "$(readlink "$link")" == "$repo"/* ]] && [ ! -e "$link" ]; then
      rm "$link"; echo "prune $link"
    fi
  done
done

#!/usr/bin/env python3
"""Fetch a YouTube video's metadata and transcript as compact plain text.

Usage: fetch_youtube.py <url> [--lang xx]

Prints a header (title, channel, date, duration, language, chapters,
description) followed by the transcript grouped into ~30s timestamped lines.
Prefers human captions in the video's own language, then auto captions in
that language, then English. Requires yt-dlp on PATH.
"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def pick_track(meta, forced):
    subs = meta.get("subtitles") or {}
    auto = meta.get("automatic_captions") or {}
    lang = (forced or meta.get("language") or "en").split("-")[0]
    candidates = [
        (subs, lambda k: k.split("-")[0] == lang),
        (auto, lambda k: k == f"{lang}-orig"),
        (auto, lambda k: k == lang),
        (subs, lambda k: k.startswith("en")),
        (auto, lambda k: k in ("en-orig", "en")),
    ]
    for pool, match in candidates:
        for key in pool:
            if key != "live_chat" and match(key):
                return key, pool is auto
    return None, False


def vtt_to_text(vtt, bucket=30):
    """Collapse VTT cues into one line per `bucket` seconds, dropping the
    rolling duplicates that auto-captions produce."""
    lines, seen = [], set()
    current_start, current = None, []
    cue_start = 0
    for raw in vtt.splitlines():
        m = re.match(r"(\d+):(\d+):(\d+)\.\d+ -->", raw)
        if m:
            h, mi, s = map(int, m.groups())
            cue_start = h * 3600 + mi * 60 + s
            continue
        text = re.sub(r"<[^>]+>", "", raw).strip()
        if not text or text.startswith(("WEBVTT", "Kind:", "Language:", "NOTE")) or text in seen:
            continue
        seen.add(text)
        if current_start is None:
            current_start = cue_start
        current.append(text)
        if cue_start - current_start >= bucket:
            lines.append((current_start, " ".join(current)))
            current_start, current = None, []
    if current:
        lines.append((current_start or 0, " ".join(current)))
    return "\n".join(f"[{fmt(t)}] {txt}" for t, txt in lines)


def fmt(sec):
    sec = int(sec or 0)
    h, rem = divmod(sec, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    url = args[0]
    forced = args[args.index("--lang") + 1] if "--lang" in args else None
    if not shutil.which("yt-dlp"):
        sys.exit("yt-dlp not found. Install with: brew install yt-dlp")

    res = run(["yt-dlp", "-J", "--skip-download", "--no-playlist", url])
    if res.returncode != 0:
        sys.exit(f"yt-dlp failed:\n{res.stderr.strip()[-800:]}")
    meta = json.loads(res.stdout)

    date = meta.get("upload_date") or ""
    print(f"title: {meta.get('title')}")
    print(f"channel: {meta.get('channel') or meta.get('uploader')}")
    print(f"published: {date[:4]}-{date[4:6]}-{date[6:]}" if date else "published: unknown")
    print(f"duration: {fmt(meta.get('duration'))}")
    print(f"url: {meta.get('webpage_url') or url}")
    print(f"language: {meta.get('language') or 'unknown'}")
    chapters = meta.get("chapters") or []
    if chapters:
        print("chapters:")
        for c in chapters:
            print(f"  {fmt(c.get('start_time'))} {c.get('title')}")
    desc = (meta.get("description") or "").strip()
    if desc:
        print("description:\n" + "\n".join("  " + l for l in desc[:2000].splitlines()))

    track, is_auto = pick_track(meta, forced)
    if not track:
        print("\ntranscript: NONE AVAILABLE")
        sys.exit(2)
    with tempfile.TemporaryDirectory() as tmp:
        res = run([
            "yt-dlp", "--skip-download", "--no-playlist",
            "--write-auto-subs" if is_auto else "--write-subs",
            "--sub-langs", track, "--sub-format", "vtt",
            "-o", str(Path(tmp) / "t"), url,
        ])
        files = list(Path(tmp).glob("*.vtt"))
        if not files:
            print(f"\ntranscript: download failed ({res.stderr.strip()[-400:]})")
            sys.exit(2)
        text = vtt_to_text(files[0].read_text(encoding="utf-8", errors="replace"))
    kind = "auto-generated" if is_auto else "human"
    print(f"\ntranscript ({kind}, {track}):\n{text}")


if __name__ == "__main__":
    main()

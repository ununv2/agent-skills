#!/usr/bin/env python3
"""Fetch a web page and print its readable text in full, keeping headings,
lists and code blocks. Standard library only.

Usage: fetch_article.py <url>

Exits with code 2 when the page yields too little text (JS-rendered,
paywalled, or blocked); fall back to another fetch method in that case.
"""
import re
import sys
import urllib.request
from html.parser import HTMLParser

SKIP = {"script", "style", "noscript", "svg", "nav", "footer", "header", "aside", "form", "iframe"}
BLOCK = {"p", "div", "section", "article", "li", "tr", "br", "blockquote", "figcaption", "dd", "dt"}


class Extractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.skip, self.pre = [], 0, 0
        self.title, self.in_title = "", False

    def handle_starttag(self, tag, attrs):
        if tag in SKIP:
            self.skip += 1
        elif tag == "title":
            self.in_title = True
        elif self.skip:
            return
        elif tag in ("h1", "h2", "h3", "h4"):
            self.out.append("\n\n" + "#" * int(tag[1]) + " ")
        elif tag == "pre":
            self.pre += 1
            self.out.append("\n```\n")
        elif tag == "li":
            self.out.append("\n- ")
        elif tag in BLOCK:
            self.out.append("\n")

    def handle_endtag(self, tag):
        if tag in SKIP:
            self.skip = max(0, self.skip - 1)
        elif tag == "title":
            self.in_title = False
        elif tag == "pre" and not self.skip:
            self.pre = max(0, self.pre - 1)
            self.out.append("\n```\n")
        elif tag in ("h1", "h2", "h3", "h4", "p") and not self.skip:
            self.out.append("\n")

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        elif not self.skip:
            self.out.append(data if self.pre else re.sub(r"\s+", " ", data))


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    url = sys.argv[1]
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh) learning-notes"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            html = r.read().decode(r.headers.get_content_charset() or "utf-8", errors="replace")
    except Exception as e:
        sys.exit(f"fetch failed: {e}")
    p = Extractor()
    p.feed(html)
    lines, in_code = [], False
    for l in "".join(p.out).splitlines():
        if l.strip() == "```":
            in_code = not in_code
        lines.append(l.rstrip() if in_code else l.strip())
    text, blank = [], False
    for l in lines:
        if l.strip():
            text.append(l)
            blank = False
        elif not blank:
            text.append("")
            blank = True
    body = "\n".join(text).strip()
    print(f"title: {p.title.strip()}\nurl: {url}\n\n{body}")
    if len(body.split()) < 150:
        print("\n[warning: very little text extracted; page may need JavaScript or be paywalled]")
        sys.exit(2)


if __name__ == "__main__":
    main()

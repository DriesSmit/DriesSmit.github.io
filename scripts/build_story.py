"""Render the online edition from the canonical Markdown manuscript.

Usage: python3 scripts/build_story.py /path/to/children-of-our-passing.md
Rebuild PDF/EPUB with the book repository's own build scripts.
"""
import argparse
import html
import re
from pathlib import Path

TITLE = 'Children of Our Passing'
DESCRIPTION = ('A fictional short story I wrote about a family living through the rise '
               'of recursively self-improving AI, as the systems that make their lives '
               'better gradually take control of their future.')
OUTPUT = Path(__file__).resolve().parents[1] / 'children-of-our-passing/index.html'


def inline(text):
    text = html.escape(text)
    text = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'<a href="\2">\1</a>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    return re.sub(r'\*([^*]+)\*', r'<em>\1</em>', text)


def render(markdown):
    if markdown.splitlines()[0] != f'# {TITLE}':
        raise ValueError('Unexpected manuscript title')
    clean = re.sub(r'<!--.*?-->', '', markdown, flags=re.S)
    parts = re.split(r'^## (.+)$', clean, flags=re.M)
    quotes = [line[1:].strip() for line in parts[0].splitlines() if line.startswith('>')]
    epigraph = [' '.join(block.splitlines()) for block in '\n'.join(quotes).split('\n\n') if block.strip()]
    if len(epigraph) != 2:
        raise ValueError('Expected epigraph and attribution')
    chapters, links = [], []
    for index in range(1, len(parts), 2):
        heading, body = parts[index], parts[index + 1]
        anchor = 'chapter-' + heading.split()[0]
        links.append(f'<li><a href="#{anchor}">{html.escape(heading)}</a></li>')
        paragraphs = []
        for block in re.split(r'\n\s*\n', body.strip()):
            text = ' '.join(block.splitlines())
            if text == '• • •':
                paragraphs.append('<hr class="scene-break" aria-label="Scene break">')
            else:
                paragraphs.append(f'<p>{inline(text)}</p>')
        chapters.append(f'<section class="chapter" id="{anchor}" aria-labelledby="heading-{anchor}">\n'
                        f'<h2 id="heading-{anchor}">{html.escape(heading)}</h2>\n' + '\n'.join(paragraphs) + '\n</section>')
    if len(chapters) != 10:
        raise ValueError('Expected ten chapters; review the navigation before publishing')
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{TITLE} — Dries Smit</title>
  <meta name="description" content="{html.escape(DESCRIPTION, quote=True)}">
  <meta property="og:title" content="{TITLE}">
  <meta property="og:description" content="{html.escape(DESCRIPTION, quote=True)}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://driessmit.github.io/children-of-our-passing/">
  <meta property="og:image" content="https://driessmit.github.io/children-of-our-passing/cover.jpg">
  <link rel="canonical" href="https://driessmit.github.io/children-of-our-passing/">
  <link rel="stylesheet" href="reading.css">
</head>
<body id="top">
<div class="shell">
  <nav class="site-nav" aria-label="Back to website"><a href="../#projects">← Dries Smit · Projects</a></nav>
  <main>
    <header class="hero">
      <div>
        <p class="eyebrow">A fictional short story</p>
        <h1>{TITLE}</h1>
        <p class="author">Dries Smit</p>
        <p class="description">{DESCRIPTION}</p>
        <div class="actions">
          <a class="start" href="#chapter-2027">Begin reading</a>
          <a href="children-of-our-passing.pdf" download>Download PDF</a>
          <a href="children-of-our-passing.epub" download>Download EPUB</a>
        </div>
      </div>
      <img class="cover" src="cover.jpg" width="600" height="900" alt="Cover of Children of Our Passing by Dries Smit">
    </header>
    <div class="reading">
      <details id="contents">
        <summary>Contents · 10 chapters</summary>
        <nav aria-label="Chapters"><ol class="contents">{''.join(links)}</ol></nav>
      </details>
      <blockquote class="epigraph">
        <p>{inline(epigraph[0])}</p>
        <footer>{inline(epigraph[1])}</footer>
      </blockquote>
      <article aria-label="{TITLE}">
{chr(10).join(chapters)}
      </article>
    </div>
  </main>
  <footer class="end">
    <p>{TITLE} · Dries Smit</p>
    <div class="actions"><a href="#top">Back to top</a><a href="children-of-our-passing.pdf" download>Download PDF</a><a href="children-of-our-passing.epub" download>Download EPUB</a><a href="../#projects">More projects</a></div>
  </footer>
</div>
</body>
</html>
'''


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manuscript', type=Path)
    args = parser.parse_args()
    OUTPUT.write_text(render(args.manuscript.read_text(encoding='utf-8')), encoding='utf-8')
    print(f'Built {OUTPUT}')

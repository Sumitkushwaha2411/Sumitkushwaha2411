"""
terminal_svg.py
Wraps a block of monospace text into an SVG that looks like a macOS-style
terminal window (red/yellow/green dots + title bar), matching the look
in the screenshot. Used by both the portrait generator and the wordmark
generator so every card in the README looks consistent.
"""

def render_terminal_svg(
    lines,
    title="avi@github: ~$ ./portrait.sh",
    font_size=9,
    line_height=11,
    char_width=5.6,
    padding=20,
    bg="#0d1117",
    chrome_bg="#161b22",
    text_color="#e6edf3",
    accent="#58a6ff",
    font_family="'JetBrains Mono','Fira Code',monospace",
):
    """
    lines: list[str] -- each line of ASCII/text to render, top to bottom
    Returns: full SVG markup as a string
    """
    max_len = max((len(l) for l in lines), default=0)
    content_w = max_len * char_width
    content_h = len(lines) * line_height

    width = int(content_w + padding * 2)
    height = int(content_h + padding * 2 + 40)  # +40 for title bar

    def esc(s):
        return (
            s.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
        )

    text_rows = []
    y = 40 + padding
    for line in lines:
        text_rows.append(
            f'<text x="{padding}" y="{y}" font-family="{font_family}" '
            f'font-size="{font_size}" fill="{text_color}" xml:space="preserve">{esc(line)}</text>'
        )
        y += line_height

    svg = f'''<svg viewBox="0 0 {width} {height}" width="{width}" height="{height}"
     xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="0" width="{width}" height="{height}" rx="10" fill="{bg}"/>
  <rect x="0" y="0" width="{width}" height="32" rx="10" fill="{chrome_bg}"/>
  <rect x="0" y="20" width="{width}" height="12" fill="{chrome_bg}"/>
  <circle cx="18" cy="16" r="6" fill="#ff5f56"/>
  <circle cx="38" cy="16" r="6" fill="#ffbd2e"/>
  <circle cx="58" cy="16" r="6" fill="#27c93f"/>
  <text x="{width/2}" y="20" text-anchor="middle" font-family="{font_family}"
        font-size="11" fill="#8b949e">{esc(title)}</text>
  {''.join(text_rows)}
</svg>'''
    return svg


if __name__ == "__main__":
    demo = ["avi@github:~$ whoami", "Sumit Kushwaha"]
    print(render_terminal_svg(demo)[:200], "...")

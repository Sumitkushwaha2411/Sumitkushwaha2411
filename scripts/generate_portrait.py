"""
generate_portrait.py

Usage:
    python generate_portrait.py path/to/your_photo.jpg assets/portrait.svg

Converts a photo into ASCII art and wraps it in a terminal-window SVG,
matching the "whoami / ./portrait.sh" card style.
"""
import sys
from PIL import Image
from terminal_svg import render_terminal_svg

# Darkest -> lightest. Tweak this string to change the "ink" density/style.
RAMP = "@%#*+=-:. "


def image_to_ascii(path, cols=90, font_aspect=0.55):
    """
    cols: how many characters wide the ASCII art should be.
    font_aspect: monospace chars are taller than wide, so we shrink the
    number of rows proportionally to avoid a squished portrait.
    """
    img = Image.open(path).convert("L")  # grayscale
    w, h = img.size
    rows = int(cols * (h / w) * font_aspect)
    img = img.resize((cols, rows))

    pixels = img.getdata()
    ramp_len = len(RAMP) - 1
    chars = []
    for i, p in enumerate(pixels):
        # map 0-255 brightness to a character in the ramp
        idx = int((p / 255) * ramp_len)
        chars.append(RAMP[idx])
        if (i + 1) % cols == 0:
            chars.append("\n")
    ascii_art = "".join(chars)
    return ascii_art.split("\n")


def main():
    if len(sys.argv) < 3:
        print("Usage: python generate_portrait.py <photo_path> <output_svg_path>")
        sys.exit(1)

    photo_path, out_path = sys.argv[1], sys.argv[2]
    lines = image_to_ascii(photo_path, cols=90)
    lines.append("")
    lines.append("avi@github:~$ whoami  Sumit Kushwaha")

    svg = render_terminal_svg(
        lines,
        title="sumit@github: ~$ ./portrait.sh",
        font_size=6,
        line_height=7,
        char_width=3.6,
    )

    with open(out_path, "w") as f:
        f.write(svg)
    print(f"Saved {out_path}")


if __name__ == "__main__":
    main()

"""
generate_wordmark.py

Usage:
    python generate_wordmark.py "SUMIT" assets/wordmark.svg
    python generate_wordmark.py "SK" assets/wordmark.svg --font=isometric1

Renders a big block-letter ASCII wordmark (via pyfiglet) inside a
terminal-window SVG, matching the "./wordmark.sh --3d" card style.
Good font choices for a "3D/blocky" look: isometric1, isometric2,
isometric3, isometric4, block, colossal, doom, larry3d, alligator.
"""
import sys
import pyfiglet
from terminal_svg import render_terminal_svg


def main():
    if len(sys.argv) < 3:
        print('Usage: python generate_wordmark.py "TEXT" <output_svg_path> [--font=isometric1]')
        sys.exit(1)

    text, out_path = sys.argv[1], sys.argv[2]
    font = "block"
    for arg in sys.argv[3:]:
        if arg.startswith("--font="):
            font = arg.split("=", 1)[1]

    art = pyfiglet.figlet_format(text, font=font)
    lines = art.rstrip("\n").split("\n")

    svg = render_terminal_svg(
        lines,
        title="sumit@github: ~$ ./wordmark.sh --3d",
        font_size=10,
        line_height=12,
        char_width=6.2,
    )

    with open(out_path, "w") as f:
        f.write(svg)
    print(f"Saved {out_path} using font '{font}'")


if __name__ == "__main__":
    main()

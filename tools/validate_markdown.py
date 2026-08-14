from __future__ import annotations

import sys
from pathlib import Path

from normalize_markdown import (
    EXCLUDED_DIRECTORIES,
    is_excluded,
    normalize_markdown,
)


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    invalid_files: list[Path] = []

    for path in ROOT.rglob("*.md"):
        relative_path = path.relative_to(ROOT)

        if is_excluded(relative_path):
            continue

        try:
            original = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            print(f"[ERROR] {relative_path}")
            print("        El archivo no está codificado en UTF-8.")
            invalid_files.append(relative_path)
            continue

        normalized = normalize_markdown(original)

        if normalized != original:
            print(f"[ERROR] {relative_path}")
            print(
                "        El archivo contiene Markdown que requiere "
                "normalización."
            )
            invalid_files.append(relative_path)

    if invalid_files:
        print(
            f"\nVALIDACIÓN FALLIDA: "
            f"{len(invalid_files)} archivo(s) requieren normalización."
        )
        print(
            "Ejecuta localmente:\n"
            "  python tools/normalize_markdown.py"
        )
        return 1

    print("VALIDACIÓN CORRECTA: Markdown normalizado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

EXCLUDED_DIRECTORIES = {
    ".git",
    ".obsidian",
    ".quartz-cache",
    "node_modules",
    "public",
}


def is_excluded(path: Path) -> bool:
    return any(part in EXCLUDED_DIRECTORIES for part in path.parts)


def normalize_markdown(content: str) -> str:
    original = content

    # Front matter y separadores escapados.
    content = re.sub(r"(?m)^\\---\s*$", "---", content)

    # Encabezados Markdown.
    content = re.sub(r"(?m)^(\s*)\\(#{1,6})(\s+)", r"\1\2\3", content)

    # Viñetas escapadas.
    content = re.sub(r"(?m)^\s*\\\s*$", "", content)

    # Listas numeradas escapadas: 1\. texto
    content = re.sub(r"(?m)^(\s*\d+)\\\.\s+", r"\1. ", content)

    # Citas escapadas.
    content = re.sub(r"(?m)^(\s*)\\>\s?", r"\1> ", content)

    # Casillas de verificación escapadas.
    content = re.sub(
        r"(?m)^(\s*)-\s+\\\[([ xX])\\\]\s+",
        r"\1- [\2] ",
        content,
    )

    # Espacios codificados como entidad HTML.
    content = content.replace("&#x20;", " ")

    # Elimina espacios al final de las líneas.
    content = re.sub(r"[ \t]+(?=\n)", "", content)

    # Conserva una sola línea final.
    if content:
        content = content.rstrip() + "\n"

    return content if content != original else original


def main() -> None:
    modified_files: list[Path] = []

    for path in ROOT.rglob("*.md"):
        relative_path = path.relative_to(ROOT)

        if is_excluded(relative_path):
            continue

        original = path.read_text(encoding="utf-8")
        normalized = normalize_markdown(original)

        if normalized != original:
            path.write_text(normalized, encoding="utf-8", newline="\n")
            modified_files.append(relative_path)

    if not modified_files:
        print("No se encontraron archivos Markdown que requieran normalización.")
        return

    print("Archivos modificados:")
    for path in modified_files:
        print(f"  - {path}")

    print(f"\nTotal: {len(modified_files)} archivo(s).")


if __name__ == "__main__":
    main()
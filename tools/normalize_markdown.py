from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

EXCLUDED_DIRECTORIES = {
    ".git",
    ".obsidian",
    ".quartz-cache",
    ".vs",
    "node_modules",
    "public",
    "__pycache__",
}


def is_excluded(path: Path) -> bool:
    return any(part in EXCLUDED_DIRECTORIES for part in path.parts)


def normalize_markdown(content: str) -> str:
    original = content

    # Front Matter y separadores escapados.
    content = re.sub(
        r"(?m)^\\---\s*$",
        "---",
        content,
    )

    # Encabezados Markdown escapados.
    # Ejemplo:
    # \# Titulo
    # \## Seccion
    content = re.sub(
        r"(?m)^(\s*)\\(#{1,6})(\s+)",
        r"\1\2\3",
        content,
    )

    # Viñetas escapadas.
    # Ejemplo:
    # \- elemento
    content = re.sub(
        r"(?m)^(\s*)\\-\s+",
        r"\1- ",
        content,
    )

    # Énfasis fuerte escapado.
    # Ejemplo:
    # \*\*texto\*\*
    content = content.replace(
        r"\*\*",
        "**",
    )

    # Cursivas escapadas.
    # Ejemplo:
    # \*texto\*
    content = re.sub(
        r"\\\*([^*\n]+)\\\*",
        r"*\1*",
        content,
    )

    # Listas numeradas escapadas.
    # Ejemplo:
    # 1\. elemento
    content = re.sub(
        r"(?m)^(\s*\d+)\\\.\s+",
        r"\1. ",
        content,
    )

    # Citas escapadas.
    # Ejemplo:
    # \> texto
    content = re.sub(
        r"(?m)^(\s*)\\>\s?",
        r"\1> ",
        content,
    )

    # Casillas de verificación escapadas.
    # Ejemplo:
    # - \[x\] tarea
    content = re.sub(
        r"(?m)^(\s*)-\s+\\\[([ xX])\\\]\s+",
        r"\1- [\2] ",
        content,
    )

    # Backticks escapados.
    # Ejemplo:
    # \`codigo\`
    content = content.replace(
        r"\`",
        "`",
    )

    # Entidad HTML usada accidentalmente como espacio.
    content = content.replace(
        "&#x20;",
        " ",
    )

    # Elimina espacios al final de las líneas.
    content = re.sub(
        r"[ \t]+(?=\n)",
        "",
        content,
    )

    # Elimina exceso de líneas en blanco.
    # Máximo dos saltos consecutivos entre bloques.
    content = re.sub(
        r"\n{4,}",
        "\n\n\n",
        content,
    )

    # Conserva exactamente una línea final.
    if content:
        content = content.rstrip() + "\n"

    return content if content != original else original


def main() -> None:
    modified_files: list[Path] = []

    for path in ROOT.rglob("*.md"):
        relative_path = path.relative_to(ROOT)

        if is_excluded(relative_path):
            continue

        try:
            original = path.read_text(
                encoding="utf-8"
            )
        except UnicodeDecodeError:
            print(
                f"[ERROR] No se pudo leer como UTF-8: "
                f"{relative_path}"
            )
            continue

        normalized = normalize_markdown(original)

        if normalized != original:
            path.write_text(
                normalized,
                encoding="utf-8",
                newline="\n",
            )
            modified_files.append(relative_path)

    if not modified_files:
        print(
            "No se encontraron archivos Markdown "
            "que requieran normalización."
        )
        return

    print("Archivos modificados:")

    for path in modified_files:
        print(f"  - {path}")

    print(
        f"\nTotal: {len(modified_files)} archivo(s)."
    )


if __name__ == "__main__":
    main()
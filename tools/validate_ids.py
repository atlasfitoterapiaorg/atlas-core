from __future__ import annotations

from collections import defaultdict
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]

EXCLUDED_DIRECTORIES = {
    ".git",
    ".github",
    ".obsidian",
    ".quartz-cache",
    ".vs",
    "__pycache__",
    "node_modules",
    "public",
}

EXCLUDED_FILES = {
    "README.md",
    "CHANGELOG.md",
}


def is_excluded(path: Path) -> bool:
    return any(
        part in EXCLUDED_DIRECTORIES
        for part in path.parts
    )


def extract_id(path: Path) -> str | None:
    content = path.read_text(encoding="utf-8")
    lines = content.splitlines()

    if not lines or lines[0].strip() != "---":
        return None

    try:
        closing_index = lines[1:].index("---") + 1
    except ValueError:
        return None

    frontmatter_text = "\n".join(
        lines[1:closing_index]
    )

    metadata = yaml.safe_load(frontmatter_text)

    if not isinstance(metadata, dict):
        return None

    document_id = metadata.get("id")

    if not isinstance(document_id, str):
        return None

    document_id = document_id.strip()

    return document_id or None


def collect_markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if not is_excluded(
            path.relative_to(ROOT)
        )
        and path.name not in EXCLUDED_FILES
    )


def main() -> int:
    files = collect_markdown_files()

    ids: dict[str, list[Path]] = defaultdict(list)

    for path in files:
        document_id = extract_id(path)

        if document_id is None:
            continue

        ids[document_id].append(path)

    duplicates = {
        document_id: paths
        for document_id, paths in ids.items()
        if len(paths) > 1
    }

    if duplicates:
        print(
            "\nVALIDACIÓN DE IDENTIFICADORES FALLIDA\n"
        )

        for document_id, paths in sorted(
            duplicates.items()
        ):
            print(
                f"[ERROR] Identificador duplicado: "
                f"{document_id}"
            )

            for path in paths:
                print(
                    f"        - "
                    f"{path.relative_to(ROOT)}"
                )

        print(
            f"\n{len(duplicates)} identificador(es) "
            "duplicado(s) detectado(s)."
        )

        return 1

    print(
        "VALIDACIÓN CORRECTA: "
        f"{len(ids)} identificador(es) únicos "
        f"en {len(files)} archivo(s) analizados."
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
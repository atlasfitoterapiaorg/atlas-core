from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote


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

MARKDOWN_LINK_PATTERN = re.compile(
    r"!?\[[^\]]*\]\(([^)]+)\)"
)


def is_excluded(path: Path) -> bool:
    return any(
        part in EXCLUDED_DIRECTORIES
        for part in path.parts
    )


def strip_anchor(target: str) -> str:
    return target.split("#", 1)[0]


def is_external(target: str) -> bool:
    lowered = target.lower()

    return lowered.startswith(
        (
            "http://",
            "https://",
            "mailto:",
            "tel:",
        )
    )


def resolve_target(
    source_file: Path,
    target: str,
) -> Path:
    target = unquote(target)

    if target.startswith("/"):
        return ROOT / target.lstrip("/")

    return source_file.parent / target


def validate_file(path: Path) -> list[str]:
    errors: list[str] = []

    content = path.read_text(
        encoding="utf-8"
    )

    for match in MARKDOWN_LINK_PATTERN.finditer(content):
        raw_target = match.group(1).strip()

        if not raw_target:
            continue

        # Permite títulos opcionales:
        # (archivo.md "Descripción")
        target = raw_target.split(" ", 1)[0]

        if is_external(target):
            continue

        target_without_anchor = strip_anchor(target)

        # Enlace únicamente a un anchor del mismo documento.
        if not target_without_anchor:
            continue

        resolved = resolve_target(
            path,
            target_without_anchor,
        ).resolve()

        if resolved.exists():
            continue

        errors.append(
            f"Enlace roto: {target}"
        )

    return errors


def collect_markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if not is_excluded(
            path.relative_to(ROOT)
        )
    )


def main() -> int:
    files = collect_markdown_files()

    total_errors = 0

    for path in files:
        errors = validate_file(path)

        if not errors:
            continue

        relative_path = path.relative_to(ROOT)

        for error in errors:
            print(
                f"[ERROR] {relative_path}"
            )
            print(
                f"        {error}"
            )

        total_errors += len(errors)

    if total_errors:
        print(
            f"\nVALIDACIÓN DE ENLACES FALLIDA: "
            f"{total_errors} error(es)."
        )
        return 1

    print(
        "VALIDACIÓN CORRECTA: "
        "no se encontraron enlaces internos rotos."
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
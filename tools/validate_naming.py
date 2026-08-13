from __future__ import annotations

import re
import sys
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
    "assets",
    "node_modules",
    "public",
    "tools",
}

EXCLUDED_FILES = {
    "README.md",
    "CHANGELOG.md",
}

SPECIAL_FILES = {
    "ROADMAP.md",
}

DOCUMENT_TYPES = {
    "GOV",
    "ADM",
    "ADR",
    "EEA",
    "TPL",
}

FILE_PATTERN = re.compile(
    r"^(GOV|ADM|ADR|EEA|TPL)-"
    r"\d{3}-"
    r"[A-Za-z0-9]+"
    r"(?:-[A-Za-z0-9]+)*"
    r"\.md$"
)

ID_PATTERN = re.compile(
    r"^(GOV|ADM|ADR|EEA|TPL)-\d{3}$"
)

FORBIDDEN_FILENAME_CHARS = re.compile(
    r'[<>:"/\\|?*\sáéíóúÁÉÍÓÚñÑ]'
)


class ValidationError:
    def __init__(self, path: Path, message: str) -> None:
        self.path = path
        self.message = message

    def __str__(self) -> str:
        return f"{self.path}: {self.message}"


def is_excluded(path: Path) -> bool:
    return any(
        part in EXCLUDED_DIRECTORIES
        for part in path.parts
    )


def extract_frontmatter(path: Path) -> dict | None:
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

    return metadata


def validate_filename(
    path: Path,
    metadata: dict | None,
) -> list[ValidationError]:
    errors: list[ValidationError] = []

    filename = path.name

    if filename in SPECIAL_FILES:
        return errors

    if FORBIDDEN_FILENAME_CHARS.search(filename):
        errors.append(
            ValidationError(
                path,
                "El nombre contiene espacios, acentos "
                "o caracteres no permitidos.",
            )
        )

    if not FILE_PATTERN.fullmatch(filename):
        errors.append(
            ValidationError(
                path,
                "El nombre no cumple el formato "
                "IDENTIFICADOR-Nombre-Descriptivo.md.",
            )
        )

    if metadata is None:
        return errors

    document_id = metadata.get("id")
    document_type = metadata.get("type")

    if document_type not in DOCUMENT_TYPES:
        return errors

    if not isinstance(document_id, str):
        errors.append(
            ValidationError(
                path,
                "El campo 'id' no es válido.",
            )
        )
        return errors

    if not ID_PATTERN.fullmatch(document_id):
        errors.append(
            ValidationError(
                path,
                f"Identificador inválido '{document_id}'.",
            )
        )
        return errors

    if not filename.startswith(f"{document_id}-"):
        errors.append(
            ValidationError(
                path,
                "El nombre del archivo no comienza "
                "con el identificador definido "
                "en el Front Matter.",
            )
        )

    if not document_id.startswith(
        f"{document_type}-"
    ):
        errors.append(
            ValidationError(
                path,
                f"El identificador '{document_id}' "
                f"no corresponde al tipo "
                f"'{document_type}'.",
            )
        )

    return errors


def collect_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.md")
        if not is_excluded(
            path.relative_to(root)
        )
        and path.name not in EXCLUDED_FILES
    )


def main() -> int:
    files = collect_files(ROOT)

    if not files:
        print(
            "No se encontraron archivos Markdown "
            "para validar."
        )
        return 0

    all_errors: list[ValidationError] = []

    for path in files:
        metadata = extract_frontmatter(path)

        all_errors.extend(
            validate_filename(
                path,
                metadata,
            )
        )

    if all_errors:
        print("\nVALIDACIÓN DE NOMENCLATURA FALLIDA\n")

        for error in all_errors:
            relative_path = error.path.relative_to(ROOT)

            print(
                f"[ERROR] {relative_path}"
            )
            print(
                f"        {error.message}"
            )

        print(
            f"\n{len(all_errors)} error(es) "
            f"en {len(files)} archivo(s) analizados."
        )

        return 1

    print(
        "VALIDACIÓN CORRECTA: "
        f"{len(files)} archivo(s) cumplen "
        "las reglas de nomenclatura."
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
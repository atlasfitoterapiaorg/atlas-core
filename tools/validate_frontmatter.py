from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

try:
    import yaml
except ImportError:
    print(
        "ERROR: PyYAML no está instalado.\n"
        "Instálalo con:\n"
        "  python -m pip install pyyaml"
    )
    sys.exit(2)


REQUIRED_FIELDS = [
    "id",
    "title",
    "version",
    "status",
    "type",
    "created",
    "updated",
    "author",
    "tags",
]

SEMVER_PATTERN = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$"
)

VALID_STATUSES = {
    "Draft",
    "Review",
    "Approved",
    "Deprecated",
    "Archived",
}

EXCLUDED_DIRECTORIES = {
    ".git",
    ".obsidian",
    ".quartz-cache",
    ".vs",
    "node_modules",
    "public",
}

EXCLUDED_FILES = {
    "README.md",
    "CHANGELOG.md",
}


class ValidationError:
    def __init__(self, path: Path, message: str) -> None:
        self.path = path
        self.message = message

    def __str__(self) -> str:
        return f"{self.path}: {self.message}"


def is_excluded(path: Path) -> bool:
    return any(part in EXCLUDED_DIRECTORIES for part in path.parts)


def extract_frontmatter(content: str) -> tuple[str | None, str | None]:
    lines = content.splitlines()

    if not lines or lines[0].strip() != "---":
        return None, "No comienza con Front Matter YAML."

    try:
        closing_index = lines[1:].index("---") + 1
    except ValueError:
        return None, "El bloque Front Matter no tiene cierre '---'."

    frontmatter = "\n".join(lines[1:closing_index])

    return frontmatter, None


def validate_file(path: Path) -> list[ValidationError]:
    errors: list[ValidationError] = []

    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return [
            ValidationError(
                path,
                "El archivo no está codificado en UTF-8."
            )
        ]

    frontmatter_text, extraction_error = extract_frontmatter(content)

    if extraction_error:
        errors.append(ValidationError(path, extraction_error))
        return errors

    assert frontmatter_text is not None

    try:
        metadata = yaml.safe_load(frontmatter_text)
    except yaml.YAMLError as exc:
        errors.append(
            ValidationError(
                path,
                f"YAML inválido: {exc}"
            )
        )
        return errors

    if not isinstance(metadata, dict):
        errors.append(
            ValidationError(
                path,
                "El Front Matter debe contener un objeto YAML."
            )
        )
        return errors

    actual_fields = list(metadata.keys())

    # Campos obligatorios
    missing = [
        field
        for field in REQUIRED_FIELDS
        if field not in metadata
    ]

    for field in missing:
        errors.append(
            ValidationError(
                path,
                f"Falta el campo obligatorio '{field}'."
            )
        )

    # Campos adicionales
    unexpected = [
        field
        for field in actual_fields
        if field not in REQUIRED_FIELDS
    ]

    for field in unexpected:
        errors.append(
            ValidationError(
                path,
                f"Campo no autorizado '{field}'."
            )
        )

    # Orden de campos
    if not missing and not unexpected:
        if actual_fields != REQUIRED_FIELDS:
            errors.append(
                ValidationError(
                    path,
                    "Los campos del Front Matter no están "
                    "en el orden definido por EEA-001."
                )
            )

    # ID
    document_id = metadata.get("id")

    if not isinstance(document_id, str) or not document_id.strip():
        errors.append(
            ValidationError(
                path,
                "'id' debe ser una cadena no vacía."
            )
        )

    # Title
    title = metadata.get("title")

    if not isinstance(title, str) or not title.strip():
        errors.append(
            ValidationError(
                path,
                "'title' debe ser una cadena no vacía."
            )
        )

    # Version
    version = metadata.get("version")

    if not isinstance(version, str):
        version = str(version) if version is not None else ""

    if not SEMVER_PATTERN.fullmatch(version):
        errors.append(
            ValidationError(
                path,
                f"Versión inválida '{version}'. "
                "Debe utilizar MAJOR.MINOR.PATCH."
            )
        )

    # Status
    status = metadata.get("status")

    if status not in VALID_STATUSES:
        errors.append(
            ValidationError(
                path,
                f"Estado inválido '{status}'. "
                f"Permitidos: {', '.join(sorted(VALID_STATUSES))}."
            )
        )

    # Type
    document_type = metadata.get("type")

    if (
        not isinstance(document_type, str)
        or not document_type.strip()
    ):
        errors.append(
            ValidationError(
                path,
                "'type' debe ser una cadena no vacía."
            )
        )

    # Fechas
    for field in ("created", "updated"):
        value = metadata.get(field)

        if not isinstance(value, (date, str)):
            errors.append(
                ValidationError(
                    path,
                    f"'{field}' debe contener una fecha válida."
                )
            )
            continue

        if isinstance(value, str):
            try:
                date.fromisoformat(value)
            except ValueError:
                errors.append(
                    ValidationError(
                        path,
                        f"'{field}' debe utilizar formato YYYY-MM-DD."
                    )
                )

    # Author
    author = metadata.get("author")

    if not isinstance(author, str) or not author.strip():
        errors.append(
            ValidationError(
                path,
                "'author' debe ser una cadena no vacía."
            )
        )

    # Tags
    tags = metadata.get("tags")

    if not isinstance(tags, list) or not tags:
        errors.append(
            ValidationError(
                path,
                "'tags' debe contener al menos una etiqueta."
            )
        )
    elif not all(
        isinstance(tag, str) and tag.strip()
        for tag in tags
    ):
        errors.append(
            ValidationError(
                path,
                "Todos los elementos de 'tags' deben ser cadenas."
            )
        )

    return errors


def collect_markdown_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.md")
        if not is_excluded(path.relative_to(root))
        and path.name not in EXCLUDED_FILES
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Valida Front Matter YAML conforme a EEA-001."
        )
    )

    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Archivo o directorio a validar.",
    )

    args = parser.parse_args()

    target = Path(args.path).resolve()

    if not target.exists():
        print(f"ERROR: No existe: {target}")
        return 2

    if target.is_file():
        files = [target]
    else:
        files = collect_markdown_files(target)

    if not files:
        print("No se encontraron archivos Markdown.")
        return 0

    all_errors: list[ValidationError] = []

    for path in files:
        all_errors.extend(validate_file(path))

    if all_errors:
        print("\nVALIDACIÓN FALLIDA\n")

        for error in all_errors:
            try:
                display_path = error.path.relative_to(target)
            except ValueError:
                display_path = error.path

            print(f"[ERROR] {display_path}")
            print(f"        {error.message}")

        print(
            f"\n{len(all_errors)} error(es) "
            f"en {len(files)} archivo(s) analizados."
        )

        return 1

    print(
        f"VALIDACIÓN CORRECTA: "
        f"{len(files)} archivo(s) Markdown."
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
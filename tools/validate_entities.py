from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Callable

import yaml


# ============================================================
# Configuración general
# ============================================================

VALID_GOVERNANCE_STATUSES = {
    "proposed",
    "review",
    "approved",
}

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


class ValidationError:
    def __init__(self, path: Path, message: str) -> None:
        self.path = path
        self.message = message

    def __str__(self) -> str:
        return f"{self.path}: {self.message}"


# ============================================================
# Utilidades
# ============================================================

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


def require_non_empty_string(
    path: Path,
    metadata: dict,
    field: str,
    errors: list[ValidationError],
) -> None:
    value = metadata.get(field)

    if not isinstance(value, str) or not value.strip():
        errors.append(
            ValidationError(
                path,
                f"'{field}' debe ser una cadena no vacía.",
            )
        )


def validate_governance_status(
    path: Path,
    metadata: dict,
    errors: list[ValidationError],
) -> None:
    governance_status = metadata.get(
        "governance_status"
    )

    if (
        governance_status
        not in VALID_GOVERNANCE_STATUSES
    ):
        errors.append(
            ValidationError(
                path,
                (
                    "Estado de gobernanza inválido "
                    f"'{governance_status}'. "
                    "Permitidos: "
                    + ", ".join(
                        sorted(
                            VALID_GOVERNANCE_STATUSES
                        )
                    )
                    + "."
                ),
            )
        )


def validate_relationship_structure(
    path: Path,
    metadata: dict,
    errors: list[ValidationError],
) -> None:
    relationships = metadata.get(
        "relationships",
        [],
    )

    if not isinstance(relationships, list):
        errors.append(
            ValidationError(
                path,
                "'relationships' debe ser una lista.",
            )
        )
        return

    for index, relationship in enumerate(
        relationships,
        start=1,
    ):
        if not isinstance(relationship, dict):
            errors.append(
                ValidationError(
                    path,
                    (
                        f"Relación {index} debe ser "
                        "un objeto."
                    ),
                )
            )
            continue

        relation_type = relationship.get("type")
        target = relationship.get("target")

        if (
            not isinstance(relation_type, str)
            or not relation_type.strip()
        ):
            errors.append(
                ValidationError(
                    path,
                    (
                        f"Relación {index}: "
                        "falta 'type'."
                    ),
                )
            )

        if (
            not isinstance(target, str)
            or not target.strip()
        ):
            errors.append(
                ValidationError(
                    path,
                    (
                        f"Relación {index}: "
                        "falta 'target'."
                    ),
                )
            )


def validate_transversal_lists(
    path: Path,
    metadata: dict,
    errors: list[ValidationError],
) -> None:
    for field in (
        "external_ids",
        "provenance",
    ):
        value = metadata.get(field, [])

        if not isinstance(value, list):
            errors.append(
                ValidationError(
                    path,
                    f"'{field}' debe ser una lista.",
                )
            )


# ============================================================
# Taxón
# ============================================================

TAXON_LEVELS = {
    "family": "FAM",
    "genus": "GEN",
    "species": "SP",
    "subspecies": "SSP",
    "variety": "VAR",
    "form": "FOR",
}

TAXON_ID_PATTERN = re.compile(
    r"^TAX-(FAM|GEN|SP|SSP|VAR|FOR)-\d{6}$"
)


def validate_taxon(
    path: Path,
    metadata: dict,
) -> list[ValidationError]:
    errors: list[ValidationError] = []

    taxon_id = metadata.get("id")

    if (
        not isinstance(taxon_id, str)
        or not TAXON_ID_PATTERN.fullmatch(
            taxon_id
        )
    ):
        errors.append(
            ValidationError(
                path,
                (
                    "ID taxonómico inválido. "
                    "Formato esperado: "
                    "TAX-<RANGO>-000000."
                ),
            )
        )

    require_non_empty_string(
        path,
        metadata,
        "title",
        errors,
    )

    require_non_empty_string(
        path,
        metadata,
        "scientific_name",
        errors,
    )

    level = metadata.get("taxonomic_level")

    if level not in TAXON_LEVELS:
        errors.append(
            ValidationError(
                path,
                (
                    "Nivel taxonómico inválido "
                    f"'{level}'."
                ),
            )
        )
    elif isinstance(taxon_id, str):
        expected_prefix = (
            f"TAX-{TAXON_LEVELS[level]}-"
        )

        if not taxon_id.startswith(
            expected_prefix
        ):
            errors.append(
                ValidationError(
                    path,
                    (
                        f"El ID '{taxon_id}' "
                        "no corresponde al nivel "
                        f"'{level}'. Debe comenzar "
                        f"con '{expected_prefix}'."
                    ),
                )
            )

    validate_governance_status(
        path,
        metadata,
        errors,
    )

    validate_relationship_structure(
        path,
        metadata,
        errors,
    )

    relationships = metadata.get(
        "relationships",
        [],
    )

    if isinstance(relationships, list):
        for index, relationship in enumerate(
            relationships,
            start=1,
        ):
            if not isinstance(
                relationship,
                dict,
            ):
                continue

            target = relationship.get("target")

            if (
                isinstance(target, str)
                and target.strip()
                and not target.startswith("TAX-")
            ):
                errors.append(
                    ValidationError(
                        path,
                        (
                            f"Relación {index}: "
                            "el target de una relación "
                            "taxonómica debe utilizar "
                            "un ID TAX-*."
                        ),
                    )
                )

    validate_transversal_lists(
        path,
        metadata,
        errors,
    )

    return errors


# ============================================================
# Registro de tipos soportados
# ============================================================

EntityValidator = Callable[
    [Path, dict],
    list[ValidationError],
]

ENTITY_VALIDATORS: dict[
    str,
    EntityValidator,
] = {
    "taxon": validate_taxon,
}


# ============================================================
# Validación genérica
# ============================================================

def validate_entity(
    path: Path,
) -> list[ValidationError]:
    try:
        metadata = extract_frontmatter(path)
    except UnicodeDecodeError:
        return [
            ValidationError(
                path,
                "El archivo no está codificado en UTF-8.",
            )
        ]
    except yaml.YAMLError as exc:
        return [
            ValidationError(
                path,
                f"Front Matter YAML inválido: {exc}",
            )
        ]

    if metadata is None:
        return []

    entity_type = metadata.get("type")

    if entity_type not in ENTITY_VALIDATORS:
        return []

    validator = ENTITY_VALIDATORS[entity_type]

    return validator(
        path,
        metadata,
    )


def collect_entity_files(
    root: Path,
) -> list[Path]:
    files: list[Path] = []

    for path in root.rglob("*.md"):
        relative_path = path.relative_to(root)

        if is_excluded(relative_path):
            continue

        try:
            metadata = extract_frontmatter(path)
        except (
            UnicodeDecodeError,
            yaml.YAMLError,
        ):
            files.append(path)
            continue

        if not isinstance(metadata, dict):
            continue

        entity_type = metadata.get("type")

        if entity_type in ENTITY_VALIDATORS:
            files.append(path)

    return sorted(files)


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Valida entidades de conocimiento "
            "del Atlas de Fitoterapia."
        )
    )

    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help=(
            "Archivo o directorio que contiene "
            "entidades de conocimiento."
        ),
    )

    args = parser.parse_args()

    target = Path(args.path).resolve()

    if not target.exists():
        print(f"ERROR: No existe: {target}")
        return 2

    if target.is_file():
        files = [target]
    else:
        files = collect_entity_files(
            target
        )

    if not files:
        print(
            "No se encontraron entidades "
            "de conocimiento soportadas."
        )
        return 0

    all_errors: list[ValidationError] = []

    for path in files:
        all_errors.extend(
            validate_entity(path)
        )

    if all_errors:
        print(
            "\nVALIDACIÓN DE ENTIDADES FALLIDA\n"
        )

        for error in all_errors:
            try:
                display_path = (
                    error.path.relative_to(
                        target
                    )
                )
            except ValueError:
                display_path = error.path

            print(
                f"[ERROR] {display_path}"
            )
            print(
                f"        {error.message}"
            )

        print(
            f"\n{len(all_errors)} error(es) "
            f"en {len(files)} entidad(es) "
            "analizada(s)."
        )

        return 1

    supported_types = ", ".join(
        sorted(ENTITY_VALIDATORS)
    )

    print(
        "VALIDACIÓN CORRECTA: "
        f"{len(files)} entidad(es). "
        f"Tipos soportados: "
        f"{supported_types}."
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
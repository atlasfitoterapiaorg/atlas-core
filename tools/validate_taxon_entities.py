from __future__ import annotations

import argparse
import re
from pathlib import Path

import yaml


VALID_LEVELS = {
    "family": "FAM",
    "genus": "GEN",
    "species": "SP",
    "subspecies": "SSP",
    "variety": "VAR",
    "form": "FOR",
}

VALID_GOVERNANCE_STATUSES = {
    "proposed",
    "review",
    "approved",
}

ID_PATTERN = re.compile(
    r"^TAX-(FAM|GEN|SP|SSP|VAR|FOR)-\d{6}$"
)


class ValidationError:
    def __init__(self, path: Path, message: str) -> None:
        self.path = path
        self.message = message

    def __str__(self) -> str:
        return f"{self.path}: {self.message}"


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


def validate_taxon(path: Path) -> list[ValidationError]:
    errors: list[ValidationError] = []

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
        return [
            ValidationError(
                path,
                "No contiene Front Matter YAML válido.",
            )
        ]

    entity_type = metadata.get("type")

    if entity_type != "taxon":
        errors.append(
            ValidationError(
                path,
                "El campo 'type' debe ser 'taxon'.",
            )
        )

    taxon_id = metadata.get("id")

    if (
        not isinstance(taxon_id, str)
        or not ID_PATTERN.fullmatch(taxon_id)
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

    level = metadata.get("taxonomic_level")

    if level not in VALID_LEVELS:
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
            f"TAX-{VALID_LEVELS[level]}-"
        )

        if not taxon_id.startswith(expected_prefix):
            errors.append(
                ValidationError(
                    path,
                    (
                        f"El ID '{taxon_id}' no corresponde "
                        f"al nivel '{level}'. "
                        f"Debe comenzar con "
                        f"'{expected_prefix}'."
                    ),
                )
            )

    scientific_name = metadata.get(
        "scientific_name"
    )

    if (
        not isinstance(scientific_name, str)
        or not scientific_name.strip()
    ):
        errors.append(
            ValidationError(
                path,
                (
                    "'scientific_name' debe ser "
                    "una cadena no vacía."
                ),
            )
        )

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
                    f"'{governance_status}'."
                ),
            )
        )

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
    else:
        for index, relationship in enumerate(
            relationships,
            start=1,
        ):
            if not isinstance(relationship, dict):
                errors.append(
                    ValidationError(
                        path,
                        (
                            "Relación "
                            f"{index} debe ser un objeto."
                        ),
                    )
                )
                continue

            relation_type = relationship.get(
                "type"
            )
            target = relationship.get("target")

            if (
                not isinstance(relation_type, str)
                or not relation_type.strip()
            ):
                errors.append(
                    ValidationError(
                        path,
                        (
                            "Relación "
                            f"{index}: falta 'type'."
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
                            "Relación "
                            f"{index}: falta 'target'."
                        ),
                    )
                )
            elif not target.startswith("TAX-"):
                errors.append(
                    ValidationError(
                        path,
                        (
                            "Relación "
                            f"{index}: target taxonómico "
                            "debe utilizar un ID TAX-*."
                        ),
                    )
                )

    external_ids = metadata.get(
        "external_ids",
        [],
    )

    if not isinstance(external_ids, list):
        errors.append(
            ValidationError(
                path,
                "'external_ids' debe ser una lista.",
            )
        )

    provenance = metadata.get(
        "provenance",
        [],
    )

    if not isinstance(provenance, list):
        errors.append(
            ValidationError(
                path,
                "'provenance' debe ser una lista.",
            )
        )

    return errors


def collect_taxon_files(root: Path) -> list[Path]:
    files: list[Path] = []

    for path in root.rglob("*.md"):
        try:
            metadata = extract_frontmatter(path)
        except (
            UnicodeDecodeError,
            yaml.YAMLError,
        ):
            continue

        if (
            isinstance(metadata, dict)
            and metadata.get("type") == "taxon"
        ):
            files.append(path)

    return sorted(files)


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Valida entidades Taxón del "
            "Atlas de Fitoterapia."
        )
    )

    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help=(
            "Archivo o directorio que contiene "
            "entidades taxonómicas."
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
        files = collect_taxon_files(target)

    if not files:
        print(
            "No se encontraron entidades Taxón."
        )
        return 0

    all_errors: list[ValidationError] = []

    for path in files:
        all_errors.extend(
            validate_taxon(path)
        )

    if all_errors:
        print(
            "\nVALIDACIÓN DE TAXONES FALLIDA\n"
        )

        for error in all_errors:
            print(f"[ERROR] {error.path}")
            print(f"        {error.message}")

        print(
            f"\n{len(all_errors)} error(es) "
            f"en {len(files)} taxón(es)."
        )

        return 1

    print(
        "VALIDACIÓN CORRECTA: "
        f"{len(files)} entidad(es) Taxón."
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

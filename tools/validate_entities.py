from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parent
SCHEMA_FILE = ROOT / "schemas" / "entities.yaml"

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
    def __init__(
        self,
        path: Path,
        message: str,
    ) -> None:
        self.path = path
        self.message = message

    def __str__(self) -> str:
        return f"{self.path}: {self.message}"


def is_excluded(path: Path) -> bool:
    return any(
        part in EXCLUDED_DIRECTORIES
        for part in path.parts
    )


def load_entity_schemas() -> dict[str, dict[str, Any]]:
    if not SCHEMA_FILE.exists():
        raise FileNotFoundError(
            f"No existe el catálogo de entidades: "
            f"{SCHEMA_FILE}"
        )

    content = SCHEMA_FILE.read_text(
        encoding="utf-8"
    )

    data = yaml.safe_load(content)

    if not isinstance(data, dict):
        raise ValueError(
            "El catálogo de entidades no contiene "
            "un objeto YAML válido."
        )

    entities = data.get("entities")

    if not isinstance(entities, dict):
        raise ValueError(
            "El catálogo debe contener la clave "
            "'entities'."
        )

    return entities


def extract_frontmatter(
    path: Path,
) -> dict | None:
    content = path.read_text(
        encoding="utf-8"
    )

    lines = content.splitlines()

    if not lines or lines[0].strip() != "---":
        return None

    try:
        closing_index = (
            lines[1:].index("---") + 1
        )
    except ValueError:
        return None

    frontmatter_text = "\n".join(
        lines[1:closing_index]
    )

    metadata = yaml.safe_load(
        frontmatter_text
    )

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

    if (
        not isinstance(value, str)
        or not value.strip()
    ):
        errors.append(
            ValidationError(
                path,
                f"'{field}' debe ser "
                "una cadena no vacía.",
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
        allowed = ", ".join(
            sorted(
                VALID_GOVERNANCE_STATUSES
            )
        )

        errors.append(
            ValidationError(
                path,
                (
                    "Estado de gobernanza inválido "
                    f"'{governance_status}'. "
                    f"Permitidos: {allowed}."
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

    if not isinstance(
        relationships,
        list,
    ):
        errors.append(
            ValidationError(
                path,
                "'relationships' debe ser "
                "una lista.",
            )
        )
        return

    for index, relationship in enumerate(
        relationships,
        start=1,
    ):
        if not isinstance(
            relationship,
            dict,
        ):
            errors.append(
                ValidationError(
                    path,
                    (
                        f"Relación {index} "
                        "debe ser un objeto."
                    ),
                )
            )
            continue

        relation_type = relationship.get(
            "type"
        )

        target = relationship.get(
            "target"
        )

        if (
            not isinstance(
                relation_type,
                str,
            )
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
            not isinstance(
                target,
                str,
            )
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
        value = metadata.get(
            field,
            [],
        )

        if not isinstance(
            value,
            list,
        ):
            errors.append(
                ValidationError(
                    path,
                    (
                        f"'{field}' debe ser "
                        "una lista."
                    ),
                )
            )


def validate_required_fields(
    path: Path,
    metadata: dict,
    schema: dict[str, Any],
    errors: list[ValidationError],
) -> None:
    required_fields = schema.get(
        "required_fields",
        [],
    )

    if not isinstance(
        required_fields,
        list,
    ):
        errors.append(
            ValidationError(
                path,
                (
                    "La definición de "
                    "'required_fields' "
                    "del esquema es inválida."
                ),
            )
        )
        return

    for field in required_fields:
        if field not in metadata:
            errors.append(
                ValidationError(
                    path,
                    (
                        f"Falta campo obligatorio "
                        f"'{field}'."
                    ),
                )
            )


def validate_id(
    path: Path,
    metadata: dict,
    schema: dict[str, Any],
    errors: list[ValidationError],
) -> None:
    entity_id = metadata.get("id")

    pattern = schema.get(
        "id_pattern"
    )

    if not isinstance(
        pattern,
        str,
    ):
        errors.append(
            ValidationError(
                path,
                (
                    "El esquema no define "
                    "'id_pattern' correctamente."
                ),
            )
        )
        return

    if not isinstance(
        entity_id,
        str,
    ):
        errors.append(
            ValidationError(
                path,
                "'id' debe ser una cadena.",
            )
        )
        return

    if not re.fullmatch(
        pattern,
        entity_id,
    ):
        errors.append(
            ValidationError(
                path,
                (
                    f"ID inválido '{entity_id}'. "
                    f"Debe cumplir: {pattern}"
                ),
            )
        )


def validate_taxon_specific_rules(
    path: Path,
    metadata: dict,
    schema: dict[str, Any],
    errors: list[ValidationError],
) -> None:
    level = metadata.get(
        "taxonomic_level"
    )

    ranks = schema.get(
        "taxonomic_ranks",
        {},
    )

    if not isinstance(
        ranks,
        dict,
    ):
        errors.append(
            ValidationError(
                path,
                (
                    "La definición de "
                    "'taxonomic_ranks' "
                    "es inválida."
                ),
            )
        )
        return

    if level not in ranks:
        errors.append(
            ValidationError(
                path,
                (
                    "Nivel taxonómico inválido "
                    f"'{level}'."
                ),
            )
        )
        return

    entity_id = metadata.get("id")

    if isinstance(
        entity_id,
        str,
    ):
        expected_prefix = (
            f"TAX-{ranks[level]}-"
        )

        if not entity_id.startswith(
            expected_prefix
        ):
            errors.append(
                ValidationError(
                    path,
                    (
                        f"El ID '{entity_id}' "
                        "no corresponde al nivel "
                        f"'{level}'. Debe comenzar "
                        f"con '{expected_prefix}'."
                    ),
                )
            )

    require_non_empty_string(
        path,
        metadata,
        "scientific_name",
        errors,
    )

    relationships = metadata.get(
        "relationships",
        [],
    )

    if isinstance(
        relationships,
        list,
    ):
        for index, relationship in enumerate(
            relationships,
            start=1,
        ):
            if not isinstance(
                relationship,
                dict,
            ):
                continue

            target = relationship.get(
                "target"
            )

            if (
                isinstance(
                    target,
                    str,
                )
                and target.strip()
                and not target.startswith(
                    "TAX-"
                )
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


def validate_entity_metadata(
    path: Path,
    metadata: dict,
    entity_schemas: dict[
        str,
        dict[str, Any],
    ],
) -> list[ValidationError]:
    errors: list[ValidationError] = []

    entity_type = metadata.get(
        "type"
    )

    if not isinstance(
        entity_type,
        str,
    ):
        return errors

    schema = entity_schemas.get(
        entity_type
    )

    if schema is None:
        return errors

    validate_required_fields(
        path,
        metadata,
        schema,
        errors,
    )

    validate_id(
        path,
        metadata,
        schema,
        errors,
    )

    require_non_empty_string(
        path,
        metadata,
        "title",
        errors,
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

    validate_transversal_lists(
        path,
        metadata,
        errors,
    )

    if entity_type == "taxon":
        validate_taxon_specific_rules(
            path,
            metadata,
            schema,
            errors,
        )

    return errors


def validate_entity(
    path: Path,
    entity_schemas: dict[
        str,
        dict[str, Any],
    ],
) -> list[ValidationError]:
    try:
        metadata = extract_frontmatter(
            path
        )
    except UnicodeDecodeError:
        return [
            ValidationError(
                path,
                (
                    "El archivo no está "
                    "codificado en UTF-8."
                ),
            )
        ]
    except yaml.YAMLError as exc:
        return [
            ValidationError(
                path,
                (
                    "Front Matter YAML "
                    f"inválido: {exc}"
                ),
            )
        ]

    if metadata is None:
        return []

    return validate_entity_metadata(
        path,
        metadata,
        entity_schemas,
    )


def collect_entity_files(
    root: Path,
    entity_schemas: dict[
        str,
        dict[str, Any],
    ],
) -> list[Path]:
    files: list[Path] = []

    for path in root.rglob("*.md"):
        relative_path = path.relative_to(
            root
        )

        if is_excluded(
            relative_path
        ):
            continue

        try:
            metadata = extract_frontmatter(
                path
            )
        except (
            UnicodeDecodeError,
            yaml.YAMLError,
        ):
            files.append(path)
            continue

        if not isinstance(
            metadata,
            dict,
        ):
            continue

        entity_type = metadata.get(
            "type"
        )

        if entity_type in entity_schemas:
            files.append(path)

    return sorted(files)


def validate_duplicate_ids(
    files: list[Path],
) -> list[ValidationError]:
    errors: list[ValidationError] = []

    seen: dict[str, Path] = {}

    for path in files:
        try:
            metadata = extract_frontmatter(
                path
            )
        except (
            UnicodeDecodeError,
            yaml.YAMLError,
        ):
            continue

        if not isinstance(
            metadata,
            dict,
        ):
            continue

        entity_id = metadata.get(
            "id"
        )

        if not isinstance(
            entity_id,
            str,
        ):
            continue

        previous_path = seen.get(
            entity_id
        )

        if previous_path is not None:
            errors.append(
                ValidationError(
                    path,
                    (
                        f"ID duplicado "
                        f"'{entity_id}'. "
                        "Ya utilizado en "
                        f"{previous_path}."
                    ),
                )
            )
        else:
            seen[entity_id] = path

    return errors


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

    target = Path(
        args.path
    ).resolve()

    if not target.exists():
        print(
            f"ERROR: No existe: {target}"
        )
        return 2

    try:
        entity_schemas = (
            load_entity_schemas()
        )
    except (
        FileNotFoundError,
        ValueError,
        yaml.YAMLError,
    ) as exc:
        print(
            f"ERROR DE CONFIGURACIÓN: {exc}"
        )
        return 2

    if target.is_file():
        files = [target]
    else:
        files = collect_entity_files(
            target,
            entity_schemas,
        )

    if not files:
        print(
            "No se encontraron entidades "
            "de conocimiento soportadas."
        )
        return 0

    all_errors: list[
        ValidationError
    ] = []

    for path in files:
        all_errors.extend(
            validate_entity(
                path,
                entity_schemas,
            )
        )

    all_errors.extend(
        validate_duplicate_ids(
            files
        )
    )

    if all_errors:
        print(
            "\nVALIDACIÓN DE ENTIDADES "
            "FALLIDA\n"
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
        sorted(
            entity_schemas.keys()
        )
    )

    print(
        "VALIDACIÓN CORRECTA: "
        f"{len(files)} entidad(es)."
    )

    print(
        "Tipos soportados: "
        f"{supported_types}."
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
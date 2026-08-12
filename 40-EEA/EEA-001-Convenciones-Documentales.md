---
id: EEA-001
title: Convenciones Documentales
version: 1.1.0
status: Approved
type: EEA
created: 2026-07-25
updated: 2026-07-28
author: Proyecto Atlas de Fitoterapia
tags:
  - documentation
  - standards
  - markdown
  - yaml
---

# Convenciones Documentales

## 1. Propósito

Este estándar define la estructura documental mínima que deberán cumplir todos los documentos oficiales del Atlas de Fitoterapia.

Su finalidad es asegurar uniformidad en la organización de la información, facilitar la navegación entre documentos, simplificar su mantenimiento y permitir la automatización de procesos de validación, generación y publicación.

---

## 2. Alcance

Este estándar aplica a todos los documentos incorporados al repositorio oficial del Atlas, independientemente de su categoría documental.

Las reglas aquí definidas constituyen los requisitos mínimos de estructura, organización y presentación para cualquier documento aprobado.

---

## 3. Objetivos

Este estándar tiene como objetivos:

- Definir una estructura documental uniforme.
- Estandarizar los metadatos de todos los documentos.
- Facilitar la validación automática de la documentación.
- Garantizar la compatibilidad entre herramientas de edición y publicación.
- Favorecer la mantenibilidad y evolución del Atlas.

---

## 4. Estructura documental

Todo documento oficial deberá seguir la siguiente estructura general:

1. Front Matter YAML.
2. Título principal (H1).
3. Contenido organizado mediante encabezados jerárquicos.
4. Referencias.
5. Anexos (cuando existan).
6. Historial de versiones (cuando aplique).

Cada categoría documental podrá incorporar secciones adicionales siempre que respete esta estructura base.

No deberán incorporarse secciones informativas redundantes cuando la información ya exista en el Front Matter.

---

## 5. Metadatos obligatorios

Todo documento oficial del Atlas deberá comenzar con un bloque **YAML Front Matter** válido.

El orden de los campos será obligatorio para facilitar la validación automática.

```yaml
id:
title:
version:
status:
type:
created:
updated:
author:
tags:
```

### Definición de campos

| Campo | Obligatorio | Descripción |
|--------|:-----------:|-------------|
| id | Sí | Identificador único del documento. |
| title | Sí | Nombre oficial del documento. |
| version | Sí | Versión conforme a Semantic Versioning. |
| status | Sí | Estado del documento. |
| type | Sí | Categoría documental. |
| created | Sí | Fecha de creación. |
| updated | Sí | Fecha de la última actualización aprobada. |
| author | Sí | Responsable del documento. |
| tags | Sí | Etiquetas de clasificación. |

No deberán incorporarse campos adicionales salvo que un estándar posterior lo autorice expresamente.

---

## 6. Organización del contenido

Los documentos deberán organizarse mediante encabezados jerárquicos de Markdown.

Las siguientes reglas serán obligatorias:

- Los encabezados deberán seguir una estructura jerárquica lógica.
- Los encabezados principales deberán utilizar numeración secuencial.
- Cada encabezado representará un único tema.
- No deberán existir encabezados vacíos.
- Cuando una sección exceda el alcance previsto deberá evaluarse su separación en un documento independiente.
- Los títulos deberán ser descriptivos y consistentes con la terminología oficial del Atlas.

---

## 7. Reglas de redacción

La documentación oficial deberá:

- utilizar lenguaje técnico;
- mantener objetividad;
- evitar ambigüedades;
- mantener consistencia terminológica;
- evitar duplicación de contenido;
- definir términos especializados cuando sea necesario;
- utilizar tablas y listas cuando mejoren la comprensión.

### Voz normativa

Cuando el documento establezca obligaciones deberán utilizarse verbos normativos consistentes, tales como:

- deberá;
- podrá;
- no deberá;
- deberá evitar.

Se evitarán expresiones ambiguas o recomendatorias cuando el contenido tenga carácter normativo.

Toda afirmación técnica, científica o normativa deberá sustentarse mediante referencias cuando corresponda.

Los ejemplos deberán identificarse claramente para diferenciarlos de las reglas normativas.

---

## 8. Versionado

Todos los documentos deberán utilizar **Semantic Versioning 2.0.0**.

Las versiones seguirán el formato:

```
MAJOR.MINOR.PATCH
```

### Cambios mayores (MAJOR)

Cambios incompatibles o modificaciones normativas relevantes.

### Cambios menores (MINOR)

Nuevas secciones, ampliaciones o mejoras compatibles.

### Correcciones (PATCH)

Correcciones editoriales, ortográficas o aclaraciones sin impacto normativo.

Toda actualización deberá reflejarse en el campo `updated`.

---

## 9. Validación

Antes de su aprobación, todo documento deberá superar las siguientes verificaciones.

| Validación | Automática | Manual |
|------------|:----------:|:------:|
| YAML válido | ✓ | |
| Orden de metadatos | ✓ | |
| Encabezados jerárquicos | ✓ | |
| Numeración de secciones | ✓ | |
| Identificador único | ✓ | |
| Referencias consistentes | ✓ | ✓ |
| Documentos relacionados existentes | ✓ | ✓ |
| Terminología consistente | | ✓ |
| Calidad editorial | | ✓ |
| Cumplimiento normativo | | ✓ |

Las validaciones automáticas complementan la revisión técnica y editorial realizada durante el proceso de aprobación.

---

## 10. Compatibilidad

Todos los documentos oficiales deberán ser compatibles con:

- CommonMark.
- YAML 1.2.
- Las herramientas oficialmente adoptadas por el Atlas para edición, validación y publicación.

La incorporación de nuevas herramientas no deberá requerir modificaciones a este estándar, salvo que implique cambios en la estructura documental oficial.

---

## 11. Referencias

- GOV-001 — Constitución del Atlas de Fitoterapia.
- ADM-001 — Arquitectura General del Atlas de Fitoterapia.
- EEA-000 — Convenciones Generales.
- ADR-003 — Jerarquía Normativa.
- ADR-004 — Arquitectura antes que Implementación.
- Semantic Versioning Specification 2.0.0.
- YAML 1.2 Specification.
- CommonMark Specification.

---
id: EEA-002
title: Convenciones de Nomenclatura
version: 1.1.1
status: Approved
type: EEA
created: 2026-07-25
updated: 2026-08-15
author: Proyecto Atlas de Fitoterapia
tags:
  - standards
  - naming
  - governance
---

# Convenciones de Nomenclatura

## 1. Propósito

Este estándar define las reglas de nomenclatura para todos los activos del Atlas de Fitoterapia.

Su finalidad es garantizar que documentos, directorios, recursos multimedia, conjuntos de datos y demás componentes puedan identificarse de forma consistente, inequívoca y compatible con herramientas de automatización, control de versiones y publicación.

---

## 2. Alcance

Las disposiciones de este estándar aplican a todos los activos almacenados en los repositorios oficiales del Atlas, incluyendo documentos, imágenes, diagramas, archivos de datos, scripts, plantillas y cualquier otro recurso incorporado al proyecto.

---

## 3. Objetivos

Este estándar tiene como objetivos:

- Establecer reglas uniformes para la nomenclatura de todos los activos del Atlas.
- Garantizar la consistencia entre repositorios.
- Facilitar la automatización y validación de nombres.
- Mantener compatibilidad con sistemas operativos y herramientas de desarrollo.
- Reducir ambigüedades durante la evolución del proyecto.

---

## 4. Convenciones

### 4.1 Relación entre identidad y nomenclatura

El Atlas distingue explícitamente los siguientes conceptos:

| Elemento | Propósito | Puede modificarse |
| -------- | --------- | :---------------: |
| **Identificador (ID)** | Identidad permanente del activo. | No |
| **Nombre del archivo** | Organización física del repositorio. | Sí |
| **Título (`title`)** | Nombre lógico del documento. | Sí |

El identificador constituye la identidad permanente del activo conforme a ADR-002.

El nombre del archivo y el título del documento podrán modificarse cuando exista una justificación técnica, documental o editorial, sin alterar la identidad del activo.

---

### 4.2 Idioma

Los nombres descriptivos deberán redactarse preferentemente en español.

Se conservarán en su idioma original:

- nombres científicos;
- normas internacionales;
- tecnologías;
- marcas registradas;
- denominaciones oficiales.

Ejemplos:

```text
Echinacea purpurea
CommonMark
Quartz
GitHub
PubMed
Semantic Versioning
```

---

### 4.3 Caracteres permitidos

Se utilizarán únicamente:

- letras A-Z;
- números 0-9;
- guion medio (-).

No deberán utilizarse:

- espacios;
- acentos;
- letra ñ;
- caracteres especiales;
- signos de puntuación.

---

### 4.4 Formato general

Los nombres seguirán el formato:

```text
IDENTIFICADOR-Nombre-Descriptivo.ext
```

Ejemplos:

```text
ADR-004-Arquitectura-antes-que-Implementacion.md
EEA-002-Convenciones-de-Nomenclatura.md
MON-001-Echinacea-purpurea.md
```

---

### 4.5 Uso de mayúsculas

Los identificadores conservarán siempre su formato institucional.

Las palabras descriptivas utilizarán **Mayúscula Inicial**.

Ejemplos:

```text
EEA-001-Convenciones-Documentales.md
ADR-003-Jerarquia-Normativa.md
```

---

### 4.6 Singular y plural

Siempre que sea posible se utilizará el singular.

Podrá utilizarse el plural cuando represente la denominación ampliamente aceptada o describa con mayor precisión la naturaleza del recurso.

Ejemplos:

```text
Monografia
```

```text
RecursosGraficos
Datos
Estadisticas
```

---

### 4.7 Directorios

La nomenclatura de directorios deberá distinguir entre directorios institucionales, directorios técnicos y estructuras de conocimiento.

#### Directorios institucionales

Los directorios institucionales representan componentes formales de la arquitectura de `atlas-core`.

Podrán utilizar un prefijo numérico cuando este forme parte de la estructura física aprobada del repositorio.

La estructura institucional vigente es:

```text
00-Gobierno/
10-ADM/
20-ADR/
30-Plantillas/
30-RM/
40-EEA/
```

Estos nombres deberán conservarse mientras formen parte de la arquitectura física aprobada del repositorio.

La modificación, sustitución o incorporación de nuevos directorios institucionales deberá responder a una decisión arquitectónica o de planificación aprobada.

#### Directorios técnicos

Los directorios utilizados por herramientas, automatizaciones o componentes técnicos podrán conservar las convenciones requeridas por dichas tecnologías o por la implementación aprobada.

Dentro de `atlas-core` se reconocen actualmente, entre otros:

```text
.github/
assets/
tools/
```

Estos nombres no representan categorías documentales ni identificadores institucionales.

Por tanto, no deberán interpretarse mediante las reglas aplicables a GOV, ADR, ADM, EEA o TPL.

#### Directorios de conocimiento

Los directorios utilizados para organizar conocimiento científico deberán respetar la arquitectura definida para `atlas-knowledge`.

La estructura inicial existente en dicho repositorio tiene carácter tecnológico y editorial preliminar y no constituye todavía el modelo formal de dominios del Atlas.

Las reglas definitivas para la organización física de dominios, subdominios, entidades y demás componentes del conocimiento deberán establecerse a partir del Modelo de Conocimiento y del Modelo de Información correspondientes.

Hasta entonces, este estándar no deberá utilizarse para anticipar decisiones que correspondan al Release de Arquitectura del Conocimiento.

---

### 4.8 Acrónimos institucionales

Los acrónimos oficiales del Atlas deberán escribirse exactamente conforme a la nomenclatura institucional.

Ejemplos válidos:

```text
GOV
ADR
ADM
EEA
TPL
```

No serán válidas variantes como:

```text
Gov
Adr
adr
Adm
Tpl
```

---

## 5. Validación

Antes de incorporar un activo al repositorio oficial deberán realizarse las siguientes verificaciones.

| Validación | Automática | Manual |
| ---------- | :--------: | :----: |
| Identificador válido | ✓ | |
| Formato del nombre | ✓ | |
| Caracteres permitidos | ✓ | |
| Uso correcto de acrónimos | ✓ | |
| Compatibilidad con sistemas de archivos | ✓ | |
| Singular / plural | ✓ | |
| Correspondencia con el contenido | | ✓ |
| Consistencia con documentos relacionados | | ✓ |

Los activos que incumplan estas reglas no deberán incorporarse al repositorio oficial.

---

## 6. Compatibilidad futura

Las reglas de nomenclatura deberán mantenerse estables aun cuando el Atlas incorpore nuevas herramientas, repositorios, mecanismos de publicación o tecnologías de automatización.

Las modificaciones a este estándar únicamente podrán realizarse mediante el proceso de gobernanza establecido por el Atlas.

---

## 7. Referencias

- GOV-001 — Constitución del Atlas de Fitoterapia.
- ADM-001 — Arquitectura General del Atlas de Fitoterapia.
- ADR-002 — Sistema de Identificación Única.
- ADR-003 — Jerarquía Normativa.
- EEA-000 — Convenciones Generales.
- EEA-001 — Convenciones Documentales.
- ISO 8601 — Date and Time Format.
- Semantic Versioning Specification 2.0.0.

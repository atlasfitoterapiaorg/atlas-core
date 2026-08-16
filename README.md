# Atlas de Fitoterapia

> Arquitectura, gobernanza, estándares y plataforma tecnológica del Atlas de Fitoterapia.

El **Atlas de Fitoterapia** es un proyecto orientado a construir una base de conocimiento científico estructurada, gobernada, trazable e interoperable sobre plantas medicinales y fitoterapia.

El proyecto separa formalmente la **gobernanza y arquitectura** del **conocimiento científico y su publicación**, permitiendo que ambos evolucionen de forma controlada.

Este repositorio, **`atlas-core`**, constituye el núcleo de gobernanza, arquitectura, estándares, planificación y herramientas compartidas del proyecto.

---

## Estado actual

| Elemento | Estado |
| -------- | ------ |
| Proyecto | Atlas de Fitoterapia |
| Repositorio | `atlas-core` |
| Gobernanza | ✅ Consolidada |
| Arquitectura documental | ✅ Consolidada |
| Plataforma tecnológica | ✅ Operativa |
| Validación automática | ✅ Operativa |
| Flujo editorial | ✅ Operativo |
| Publicación web | ✅ Operativa |
| Release activo | v0.3 — Infraestructura Tecnológica |
| Sprint activo | 3.7 — Validación Integral y Cierre |
| Próximo Release | v0.4 — Arquitectura del Conocimiento |

Actualmente se encuentran completados:

* Release v0.1 — Fundación.
* Release v0.2 — Gobernanza.
* Sprint 3.1 — Plataforma Base.
* Sprint 3.2 — Página de Inicio.
* Sprint 3.3 — Identidad Visual y Navegación.
* Sprint 3.4 — Estructura Inicial del Conocimiento.
* Sprint 3.5 — Validación Automática.
* Sprint 3.6 — Plantillas y Flujo Editorial.

El desarrollo continúa dentro del Release v0.3 con el Sprint 3.7 — Validación Integral y Cierre.

---

## Propósito de `atlas-core`

El repositorio `atlas-core` tiene como responsabilidades:

* definir la gobernanza del Atlas;
* mantener la arquitectura general del proyecto;
* registrar decisiones arquitectónicas;
* establecer estándares y convenciones;
* mantener la planificación mediante el ROADMAP;
* conservar trazabilidad de la evolución del proyecto;
* proporcionar herramientas compartidas de validación;
* proporcionar automatizaciones comunes;
* mantener las plantillas gobernadas que correspondan;
* establecer las condiciones técnicas y normativas que deberán respetar los demás componentes del Atlas.

El conocimiento científico no reside en este repositorio.

---

## Arquitectura de repositorios

El Atlas utiliza dos repositorios principales con responsabilidades separadas:

```text
                          Atlas de Fitoterapia
                                 │
                 ┌───────────────┴───────────────┐
                 │                               │
            atlas-core                    atlas-knowledge
                 │                               │
          Gobernanza                         Conocimiento
          Arquitectura                       Contenido
          Estándares                         Quartz
          Planificación                      Publicación
          Plantillas                         Navegación
          Validadores                        Sitio web
          Automatización
```

### `atlas-core`

Contiene:

* gobierno;
* arquitectura;
* decisiones arquitectónicas;
* estándares;
* ROADMAP;
* herramientas;
* automatizaciones;
* validadores;
* plantillas compartidas cuando correspondan.

### `atlas-knowledge`

Contiene:

* conocimiento científico;
* estructura editorial;
* contenido publicado;
* Quartz;
* navegación;
* configuración del sitio;
* generación del sitio web.

La separación entre ambos repositorios permite mantener el conocimiento independiente de su mecanismo de presentación.

---

## Estructura del repositorio

La estructura actual de `atlas-core` es:

```text
atlas-core/
│
├── .github/
│   └── workflows/
│
├── 00-Gobierno/
├── 10-ADM/
├── 20-ADR/
├── 30-Plantillas/
├── 30-RM/
├── 40-EEA/
├── assets/
├── tools/
│
├── .gitignore
├── CHANGELOG.md
├── LICENSE
└── README.md
```

### Responsabilidad de cada componente

| Ruta | Responsabilidad |
| ---- | -------------- |
| `.github/` | Automatización e integración continua mediante GitHub Actions. |
| `00-Gobierno/` | Documentos superiores de gobierno del Atlas. |
| `10-ADM/` | Documentos de arquitectura y diseño del sistema. |
| `20-ADR/` | Registros de decisiones arquitectónicas. |
| `30-Plantillas/` | Plantillas gobernadas y reutilizables del proyecto. |
| `30-RM/` | ROADMAP oficial y planificación del proyecto. |
| `40-EEA/` | Estándares editoriales, documentales y de nomenclatura. |
| `assets/` | Recursos compartidos cuando corresponda. |
| `tools/` | Herramientas de normalización, validación y automatización. |
| `CHANGELOG.md` | Historial consolidado de cambios del proyecto. |
| `LICENSE` | Licencia del repositorio. |
| `README.md` | Descripción ejecutiva y técnica del repositorio. |

---

## Arquitectura documental

La documentación del Atlas se organiza mediante una jerarquía normativa explícita.

```text
        GOV
         │
 ┌───────┴────────┐
 │                │
ADR             ADM
 │                │
 └───────┬────────┘
         │
        EEA
         │
        TPL
         │
 Scientific docs
```

La precedencia normativa es:

```text
GOV
 │
 ├── ADR
 │
 └── ADM
      │
      ▼
     EEA
      │
      ▼
     TPL
      │
      ▼
Documentación científica
```

Cada tipo documental posee una responsabilidad distinta.

### GOV

Define principios superiores de gobierno.

### ADR

Registra decisiones arquitectónicas de carácter estable.

### ADM

Describe modelos y estructuras arquitectónicas.

### EEA

Define estándares editoriales, documentales y de nomenclatura.

### TPL

Representa plantillas que deberán implementar las reglas definidas por la gobernanza y los estándares superiores.

---

## Documentación normativa actual

La capa normativa consolidada actualmente está formada por:

### Gobierno

* GOV-001 — Constitución del Atlas de Fitoterapia.

### Arquitectura

* ADM-001 — Arquitectura General del Atlas.

### Decisiones Arquitectónicas

* ADR-001 — ROADMAP como Documento Vivo.
* ADR-002 — Sistema de Identificación Única.
* ADR-003 — Jerarquía Normativa.
* ADR-004 — Arquitectura antes que Implementación.

### Estándares

* EEA-000 — Convenciones Generales.
* EEA-001 — Convenciones Documentales.
* EEA-002 — Convenciones de Nomenclatura.

### Plantillas

* TPL-001 — Plantilla de Documento Base.

---

## Principios arquitectónicos

La evolución del Atlas se rige, entre otros, por los siguientes principios:

* la arquitectura precede a la implementación;
* el conocimiento se define una única vez y se reutiliza;
* la identidad pertenece al objeto gobernado y no al archivo que lo representa;
* cada documento debe aportar una responsabilidad arquitectónica única;
* la automatización debe implementar reglas existentes y no crear gobernanza implícita;
* el conocimiento debe mantenerse independiente de su mecanismo de presentación;
* la herramienta de edición no constituye la fuente de verdad;
* la documentación debe actualizarse cuando cambien la planificación, arquitectura, gobernanza o estándares;
* se debe evitar la creación de documentación redundante.

---

## Planificación

La evolución del proyecto se administra mediante el **ROADMAP**, que constituye el documento oficial de planificación.

El ROADMAP define:

* Releases;
* Sprints;
* entregables;
* capacidades;
* dependencias;
* prioridades;
* estado del proyecto.

El documento oficial se encuentra en:

```text
30-RM/ROADMAP.md
```

La arquitectura de planificación es:

```text
GOV
 │
 ▼
ROADMAP
 │
 ▼
Release
 │
 ▼
Sprint
 │
 ▼
Entregables / Capacidades
 │
 ▼
Tareas
```

---

## Estado de Releases

```text
v0.1  Fundación                       ✅ Completado
v0.2  Gobernanza                      ✅ Completado
v0.3  Infraestructura Tecnológica     🟡 En progreso
v0.4  Arquitectura del Conocimiento   ⚪ Planeado
v0.5+ Evolución estratégica           ⚪ Pendiente
```

### Release activo

El Release activo es:

```text
v0.3 — Infraestructura Tecnológica
```

Su propósito es proporcionar la infraestructura necesaria para:

* editar contenido;
* validar contenido;
* compilar el sitio;
* automatizar controles;
* publicar el Atlas;
* mantener la separación entre gobernanza y conocimiento;
* soportar posteriormente el modelo formal de conocimiento.

---

## Estado de Sprints

```text
Release v0.1
└── Sprint 0.1  Fundación del Proyecto                ✅

Release v0.2
└── Sprint 0.2  Gobierno del Atlas                    ✅

Release v0.3
├── Sprint 3.1  Plataforma Base                       ✅
├── Sprint 3.2  Página de Inicio                      ✅
├── Sprint 3.3  Identidad Visual y Navegación         ✅
├── Sprint 3.4  Estructura Inicial del Conocimiento   ✅
├── Sprint 3.5  Validación Automática                 ✅
├── Sprint 3.6  Plantillas y Flujo Editorial          ✅
└── Sprint 3.7  Validación Integral y Cierre          🟡
```

---

## Validación automática

`atlas-core` dispone de una capa automática de validación estructural.

El workflow principal es:

```text
Validate Atlas Core
│
├── Validate Front Matter
├── Validate Markdown
├── Validate Naming
├── Validate Links
└── Validate IDs
```

Los controles actualmente implementados son:

### Front Matter

Valida la estructura y metadatos obligatorios de los documentos gobernados.

### Markdown

Comprueba que los archivos Markdown se encuentren normalizados.

### Nomenclatura

Comprueba nombres, identificadores y correspondencia entre archivo, ID y tipo documental.

### Enlaces internos

Comprueba que los enlaces internos Markdown apunten a destinos existentes.

### Identificadores

Detecta identificadores duplicados entre documentos gobernados.

Los controles pueden ejecutarse tanto localmente como mediante GitHub Actions.

---

## Herramientas

El directorio `tools/` contiene actualmente herramientas de normalización y validación, entre ellas:

```text
tools/
├── normalize_markdown.py
├── validate_frontmatter.py
├── validate_markdown.py
├── validate_naming.py
├── validate_links.py
└── validate_ids.py
```

Estas herramientas implementan reglas existentes de los documentos normativos.

No sustituyen ni crean nuevas reglas de gobernanza.

---

## Integración continua

La validación automática se ejecuta mediante GitHub Actions.

El flujo implementado para `atlas-core` contempla:

```text
Cambio
  │
  ▼
develop
  │
  ▼
GitHub Actions
  │
  ▼
Validate Atlas Core
```

También se ejecutan validaciones sobre Pull Requests dirigidos a `main`.

La validación integral del comportamiento de bloqueo de merge y publicación se realizará dentro del Sprint 3.7 — Validación Integral y Cierre.

---

## Flujo de trabajo

El flujo general aprobado utiliza las ramas:

```text
develop
   │
   ▼
Pull Request
   │
   ▼
main
```

`develop` representa la rama de integración de cambios.

`main` representa la rama estable destinada a contener cambios formalmente integrados.

---

## Plataforma de publicación

La publicación del Atlas reside en `atlas-knowledge`.

La arquitectura tecnológica actual es:

```text
                          Usuario
                             │
                             ▼
                      GitHub Pages
                             ▲
                             │
                          Quartz
                             ▲
                             │
                    GitHub Actions
                             ▲
                             │
                    atlas-knowledge
               Conocimiento + Publicación
                             ▲
                             │
                  Gobernanza / Estándares
                             │
                         atlas-core
```

La plataforma utiliza:

* Quartz 5;
* GitHub;
* GitHub Actions;
* GitHub Pages.

La construcción y publicación automática del sitio ya se encuentra operativa.

---

## Sitio público

El sitio público del Atlas es generado desde `atlas-knowledge` mediante Quartz y publicado mediante GitHub Pages.

La estructura inicial navegable actualmente contempla:

```text
Inicio
Dominios
Especies
Principios Activos
Preparados
Enfermedades
Farmacopeas
Referencias
```

Esta estructura constituye un scaffold tecnológico y editorial.

No representa todavía el modelo formal del conocimiento.

---

## Arquitectura del conocimiento

El modelo formal del conocimiento será definido durante el Release v0.4 — Arquitectura del Conocimiento.

La arquitectura conceptual objetivo es:

```text
Atlas
 │
 ▼
Dominios de Conocimiento
 │
 ▼
Subdominios
 │
 ▼
Entidades
 │
 ▼
Relaciones
 │
 ▼
Grafo de Conocimiento
 │
 ▼
Vistas Editoriales
```

Las monografías funcionarán como vistas editoriales construidas a partir de entidades, atributos y relaciones del modelo.

El Release v0.4 contempla actualmente:

* ADR-005 — Modelo Híbrido del Conocimiento.
* ADM-002 — Arquitectura del Modelo de Conocimiento.
* ADM-003 — Dominios de Conocimiento del Atlas.
* ADM-004 — Modelo de Información del Atlas.

---

## Plantillas y flujo editorial

El Sprint 3.6 estableció los mecanismos mínimos necesarios para incorporar contenido de forma consistente sin anticipar el modelo formal de conocimiento.

La primera plantilla gobernada es:

```text
30-Plantillas/
└── TPL-001-Documento-Base.md
```

TPL-001 constituye una plantilla documental base.

No representa todavía una plantilla científica definitiva.

Las plantillas científicas futuras deberán derivarse del Modelo de Información aprobado en el Release v0.4.

### Arquitectura editorial

El flujo editorial validado es:

```text
atlas-core
    │
    ▼
TPL-001
    │
    ▼
Plantillas gobernadas
    │
    ▼
Interfaz de edición
    │
    ▼
atlas-knowledge/content
    │
    ▼
Quartz
    │
    ▼
Sitio generado
```

Las responsabilidades permanecen separadas:

```text
atlas-core
Gobernanza + estándares + plantillas

atlas-knowledge
Conocimiento + contenido + publicación

Obsidian
Interfaz local de edición
```

Obsidian puede utilizarse como interfaz de edición, pero:

* no constituye la fuente de verdad;
* no define la arquitectura del conocimiento;
* no almacena las plantillas oficiales;
* no constituye una dependencia obligatoria del Atlas.

La fuente oficial de las plantillas continúa siendo `atlas-core`.

La fuente oficial del contenido continúa siendo `atlas-knowledge`.

La integración local permite utilizar las plantillas gobernadas desde Obsidian sin duplicarlas físicamente entre repositorios.

La configuración operativa de Obsidian se documenta en el README de `atlas-knowledge`.

---

## Automatización futura

El Atlas contempla como iniciativa estratégica futura el uso de agentes para vigilancia científica.

Estos sistemas podrán eventualmente:

```text
Detectar
   ↓
Recopilar
   ↓
Clasificar
   ↓
Comparar
   ↓
Proponer
```

La incorporación de conocimiento oficial deberá conservar revisión y aprobación humana:

```text
Propuesta
   ↓
Revisión
   ↓
Aprobación humana
   ↓
Incorporación
   ↓
Publicación
```

Esta capacidad no forma parte todavía del alcance activo del proyecto.

---

## Documentación principal

Los documentos principales para comprender el proyecto son:

```text
00-Gobierno/
10-ADM/
20-ADR/
30-Plantillas/
30-RM/
40-EEA/
README.md
CHANGELOG.md
```

Para conocer el estado y planificación vigente debe consultarse:

```text
30-RM/ROADMAP.md
```

Para conocer la evolución histórica debe consultarse:

```text
CHANGELOG.md
```

---

## Historial de cambios

El historial oficial de cambios se mantiene en:

```text
CHANGELOG.md
```

Los cambios del Release v0.3 permanecen bajo:

```text
[Unreleased]
```

hasta que el Release sea cerrado formalmente.

---

## Licencia

Este repositorio utiliza la **MIT License**.

El texto completo se encuentra en:

```text
LICENSE
```

---

## Estado de madurez

```text
Release v0.1  ████████████████████████████████ 100%
Release v0.2  ████████████████████████████████ 100%
Release v0.3  ████████████████████████████░░░░ En progreso
Release v0.4  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ Planeado
```

El proyecto se encuentra actualmente en la validación integral de su infraestructura tecnológica antes de iniciar formalmente la arquitectura del conocimiento.

# Atlas de Fitoterapia

> Arquitectura, gobernanza y estándares del Atlas de Fitoterapia.

El **Atlas de Fitoterapia** es un proyecto orientado a construir una base de conocimiento científico sobre plantas medicinales mediante un modelo de conocimiento estructurado, gobernado y trazable.

Este repositorio (**atlas-core**) constituye el núcleo arquitectónico del proyecto y contiene la documentación que define su gobierno, estándares, reglas y evolución.

---
## Estado actual

- Gobernanza implementada.
- Arquitectura documental implementada.
- Plataforma Quartz operativa.
- Publicación automática habilitada.
- Desarrollo del conocimiento en progreso.
---

# Estado del Proyecto

| Elemento | Estado |
|----------|--------|
| Proyecto | Atlas de Fitoterapia |
| Repositorio | atlas-core |
| Versión | 0.2.0 |
| Estado | Gobernanza consolidada |
| Release activo | v0.3 — Infraestructura Tecnológica |

---

# Objetivos

El repositorio **atlas-core** tiene como finalidad:

- Definir la gobernanza del Atlas.
- Establecer la arquitectura documental.
- Estandarizar la documentación del proyecto.
- Mantener la trazabilidad de las decisiones arquitectónicas.
- Planificar la evolución del Atlas mediante Releases y Roadmaps.
- Proporcionar la base sobre la cual crecerá el conocimiento científico del proyecto.

---

# Estructura del Repositorio

```text
atlas-core
│
├── 00-Gobierno
├── 10-ADM
├── 20-ADR
├── 30-RM
├── 40-EEA
├── tools
├── CHANGELOG.md
├── LICENSE
└── README.md
```

## Descripción

| Directorio | Contenido |
|------------|-----------|
| 00-Gobierno | Documentos de gobierno del Atlas. |
| 10-ADM | Documentos de arquitectura del proyecto. |
| 20-ADR | Registros de decisiones arquitectónicas (Architecture Decision Records). |
| 30-RM | Roadmaps oficiales y su historial de evolución. |
| 40-EEA | Estándares editoriales y convenciones del Atlas. |
| tools | Herramientas, utilidades y automatizaciones del proyecto. |

---

# Arquitectura Documental

La documentación del Atlas se organiza mediante una jerarquía normativa que garantiza consistencia, trazabilidad y evolución controlada.

```text
                 GOV
                  │
        ┌─────────┴─────────┐
        │                   │
      ADR                 ADM
        │                   │
        └─────────┬─────────┘
                  │
                 EEA
                  │
              Documentación
```

Cada categoría documental posee una responsabilidad específica y complementaria dentro de la arquitectura del proyecto.

---

# Planificación

La evolución del proyecto se administra mediante el **ROADMAP**, documento que define:

- Releases.
- Sprints.
- Entregables.
- Prioridades.
- Estado del proyecto.

Los Roadmaps oficiales se encuentran en:

```text
30-RM/
```

---

# Repositorios del Proyecto

El Atlas se divide en repositorios con responsabilidades claramente diferenciadas.

| Repositorio | Propósito |
|-------------|-----------|
| atlas-core | Gobernanza, arquitectura, estándares y planificación. |
| atlas-knowledge | Base de conocimiento científico (desarrollo futuro). |

---

# Documentación Principal

- Constitución del Atlas (GOV).
- Architecture Decision Records (ADR).
- Architecture Management Documents (ADM).
- Estándares Editoriales (EEA).
- ROADMAP.
- CHANGELOG.

---

# Historial de Cambios

El historial oficial del proyecto se mantiene en:

```text
CHANGELOG.md
```

---

# Licencia

Pendiente de definir.

---

# Sitio Web

La publicación del Atlas se realizará mediante **Quartz** sobre **GitHub Pages**, una vez concluida la infraestructura tecnológica definida para el Release v0.3.

---

# Estado de Madurez

```text
Release v0.1  ████████████████████████████████ 100%
Release v0.2  ████████████████████████████████ 100%
Release v0.3  ████████░░░░░░░░░░░░░░░░░░░░░░░░ En progreso
```
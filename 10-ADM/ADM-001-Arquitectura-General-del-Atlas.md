---
id: ADM-001
title: Arquitectura General del Atlas de Fitoterapia
version: 1.1.0
status: Approved
type: ADM
created: 2026-07-25
updated: 2026-07-28
author: Proyecto Atlas de Fitoterapia
tags:
  - architecture
  - atlas
  - governance
---

# Arquitectura General del Atlas de Fitoterapia

## 1. Propósito

Definir la arquitectura general del Atlas de Fitoterapia, estableciendo sus componentes principales, responsabilidades, relaciones y flujo de información.

Este documento constituye la referencia arquitectónica del proyecto y proporciona una visión integral de la solución sin describir detalles específicos de implementación tecnológica ni del modelo conceptual del conocimiento científico.

---

## 2. Alcance

La arquitectura comprende la organización lógica del Atlas de Fitoterapia, incluyendo:

- Componentes principales.
- Organización de los repositorios.
- Flujo de información.
- Flujo de publicación.
- Responsabilidades de cada componente.

Quedan fuera del alcance de este documento:

- La definición del modelo conceptual del conocimiento.
- La estructura de las monografías.
- Los estándares editoriales.
- Las decisiones arquitectónicas particulares (ADR).
- La implementación técnica de herramientas específicas.

---

## 3. Objetivos Arquitectónicos

La arquitectura del Atlas deberá garantizar:

- Escalabilidad.
- Modularidad.
- Gobernanza documental.
- Trazabilidad.
- Reutilización del conocimiento.
- Interoperabilidad.
- Automatización del flujo editorial.
- Independencia tecnológica cuando sea posible.
- Separación entre gobernanza, arquitectura, conocimiento y publicación.

---

## 4. Componentes de la Arquitectura

La arquitectura del Atlas se organiza mediante componentes con responsabilidades claramente definidas.

### atlas-core

Repositorio que concentra la gobernanza del Atlas, la arquitectura, los estándares, las plantillas y la documentación técnica del proyecto.

Contiene, entre otros:

- Documentos GOV.
- Documentos ADM.
- Documentos ADR.
- Estándares EEA.
- Plantillas.
- Herramientas de automatización.
- Documentación técnica.

### atlas-knowledge

Repositorio destinado exclusivamente al conocimiento científico del Atlas.

Contiene, entre otros:

- Monografías.
- Especies vegetales.
- Perfiles bioquímicos.
- Principios activos.
- Preparaciones.
- Enfermedades.
- Referencias científicas.

### Plataforma de publicación

Conjunto de componentes responsables de transformar el contenido aprobado en el sitio público del Atlas.

La implementación tecnológica puede evolucionar sin modificar esta arquitectura.

---

## 5. Vista General de la Arquitectura

```text
                     Atlas de Fitoterapia
                              │
        ┌─────────────────────┴─────────────────────┐
        │                                           │
   atlas-core                              atlas-knowledge
        │                                           │
        │                                           │
Gobierno (GOV)                          Conocimiento científico
Arquitectura (ADM / ADR)                Monografías
Estándares (EEA)                        Especies
Plantillas                              Perfiles bioquímicos
Herramientas                            Principios activos
Documentación                           Preparaciones
                                        Referencias

                └──────────────────────┬──────────────────────┘
                                       │
                             Plataforma de Publicación
                                       │
                                  Sitio Público
```

La arquitectura separa la gobernanza del conocimiento científico, permitiendo que ambos evolucionen de forma independiente.

---

## 6. Responsabilidades

| Componente | Responsabilidad principal |
|------------|---------------------------|
| atlas-core | Gobernar, definir la arquitectura, mantener estándares y administrar la documentación técnica. |
| atlas-knowledge | Administrar el conocimiento científico validado del Atlas. |
| Plataforma de publicación | Publicar únicamente contenido aprobado hacia el sitio público. |

---

## 7. Flujo de Información

```text
Investigación científica
        │
        ▼
Recopilación de evidencia
        │
        ▼
Elaboración del documento
        │
        ▼
Revisión técnica
        │
        ▼
Aprobación
        │
        ▼
Integración en atlas-knowledge
        │
        ▼
Publicación
```

Cada etapa mantiene trazabilidad con la evidencia científica correspondiente.

---

## 8. Flujo de Publicación

```text
Edición
   │
   ▼
Repositorio Git
   │
   ▼
Control de versiones
   │
   ▼
Automatización de publicación
   │
   ▼
Generación del sitio
   │
   ▼
Sitio Público
```

La implementación tecnológica utilizada para este flujo podrá evolucionar sin modificar la arquitectura definida en este documento.

---

## 9. Restricciones Arquitectónicas

La arquitectura del Atlas deberá cumplir las siguientes restricciones:

- La gobernanza reside exclusivamente en `atlas-core`.
- El conocimiento científico reside exclusivamente en `atlas-knowledge`.
- Toda decisión arquitectónica permanente deberá documentarse mediante un ADR.
- Todo documento normativo deberá estar respaldado por los documentos de gobernanza correspondientes.
- Únicamente el contenido aprobado podrá formar parte del proceso de publicación.
- La automatización no deberá modificar contenido aprobado sin intervención humana.

---
## 10. Referencias

- GOV-001 — Constitución del Atlas de Fitoterapia.
- ADR-001 — ROADMAP como Documento Vivo.
- ADR-002 — Sistema de Identificación Única.
- ADR-003 — Jerarquía Normativa.
- ADR-004 — Arquitectura antes que Implementación.
- EEA-000 — Convenciones Generales.
- EEA-001 — Convenciones Documentales.
- EEA-002 — Convenciones de Nomenclatura.

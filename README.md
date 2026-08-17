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
| Plataforma tecnológica | ✅ Validada y operativa |
| Validación automática | ✅ Operativa |
| Controles de merge | ✅ Operativos |
| Flujo editorial | ✅ Operativo |
| Publicación web | ✅ Operativa |
| Release completado más reciente | v0.3 — Infraestructura Tecnológica |
| Release activo | v0.4 — Arquitectura del Conocimiento |
| Sprint activo | 4.1 — Modelo Híbrido del Conocimiento |

Actualmente se encuentran completados:

* Release v0.1 — Fundación.
* Release v0.2 — Gobernanza.
* Release v0.3 — Infraestructura Tecnológica.
* Sprint 3.1 — Plataforma Base.
* Sprint 3.2 — Página de Inicio.
* Sprint 3.3 — Identidad Visual y Navegación.
* Sprint 3.4 — Estructura Inicial del Conocimiento.
* Sprint 3.5 — Validación Automática.
* Sprint 3.6 — Plantillas y Flujo Editorial.
* Sprint 3.7 — Validación Integral y Cierre.

El desarrollo continúa dentro del Release v0.4 con el Sprint 4.1 — Modelo Híbrido del Conocimiento.

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

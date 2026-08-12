# Atlas de Fitoterapia

> Arquitectura, gobernanza y estándares del Atlas de Fitoterapia.

El **Atlas de Fitoterapia** es una plataforma abierta orientada a la organización, documentación y publicación de conocimiento científico sobre plantas medicinales y fitoterapia.

Este repositorio, **`atlas-core`**, constituye el núcleo de gobernanza y arquitectura del proyecto. Contiene las reglas, decisiones, estándares y planificación que gobiernan la evolución del Atlas.

---

## Estado actual

| Elemento | Estado |
|----------|--------|
| Proyecto | Atlas de Fitoterapia |
| Repositorio | `atlas-core` |
| Gobernanza | ✅ Consolidada |
| Plataforma tecnológica | ✅ Operativa |
| Release activo | v0.3 — Infraestructura Tecnológica |
| Sprint activo | 3.5 — Validación Automática |
| Publicación web | ✅ Operativa |

El sitio público es generado mediante Quartz y desplegado automáticamente mediante GitHub Actions y GitHub Pages desde el repositorio `atlas-knowledge`.

---

## Propósito de `atlas-core`

Este repositorio tiene como responsabilidades:

- definir la gobernanza del Atlas;
- mantener la arquitectura general;
- registrar decisiones arquitectónicas;
- establecer estándares y convenciones;
- mantener la planificación mediante el ROADMAP;
- conservar trazabilidad de la evolución del proyecto;
- alojar herramientas compartidas de validación y automatización.

El conocimiento científico no reside en este repositorio.

---

## Arquitectura de repositorios

El Atlas utiliza dos repositorios principales con responsabilidades separadas:

```text
                    Atlas de Fitoterapia
                           │
             ┌─────────────┴─────────────┐
             │                           │
        atlas-core                 atlas-knowledge
             │                           │
      Gobernanza                    Conocimiento
      Arquitectura                  Publicación
      Estándares                    Quartz
      Planificación                 Contenido
      Herramientas

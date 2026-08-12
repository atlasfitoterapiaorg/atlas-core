# Changelog

Todos los cambios relevantes del proyecto **Atlas de Fitoterapia** se documentan en este archivo.

El proyecto adopta las recomendaciones de **Keep a Changelog** y utiliza **Semantic Versioning (SemVer)** para el control de versiones.

---

## [Unreleased]

### Added

#### Infraestructura Tecnológica

* Plataforma de publicación basada en Quartz 5.
* Integración con GitHub Pages.
* Automatización del proceso de publicación mediante GitHub Actions.
* Pipeline de construcción y despliegue desde la rama `main`.
* Configuración del sitio público Atlas de Fitoterapia.
* Página principal institucional del Atlas.
* Navegación inicial del conocimiento.
* Estructura inicial de contenido en `atlas-knowledge`.
* Páginas índice para:

  * Dominios.
  * Especies.
  * Principios Activos.
  * Preparados.
  * Enfermedades.
  * Farmacopeas.
  * Referencias.
* Favicon botánico temporal.
* Identidad visual inicial del Atlas.
* Paleta específica para modo claro.
* Paleta específica para modo oscuro.
* Estilos visuales personalizados mediante `custom.scss`.
* Navegación principal desde la página de inicio.

#### Experiencia de Usuario

* Explorer como navegación secundaria.
* Buscador integrado.
* Vista gráfica del conocimiento.
* Tabla de contenidos.
* Cambio entre modo claro y modo oscuro.
* Navegación responsive para dispositivos móviles.

#### Repositorio

* Flujo de trabajo basado en ramas `develop` y `main`.
* Integración de cambios mediante Pull Request.
* Primer Pull Request formal de `atlas-knowledge` hacia `main`.

---

### Changed

#### Quartz

* Configuración del idioma del sitio a español compatible con Quartz.
* Personalización del título del sitio como `Atlas de Fitoterapia`.
* Personalización del footer.
* Ajuste de la configuración visual de Quartz.
* Incorporación de colores institucionales del Atlas.
* Adaptación de estilos para mantener coherencia entre modo claro y oscuro.

#### Navegación

* La página principal incorpora navegación explícita en el siguiente orden conceptual:

  1. Dominios.
  2. Especies.
  3. Principios Activos.
  4. Preparados.
  5. Enfermedades.
  6. Farmacopeas.
  7. Referencias.
* El Explorer se conserva como navegación secundaria con orden alfabético.

#### Repositorio

* Se fortaleció `.gitignore`.
* Se excluyó `node_modules/` del control de versiones.
* Se excluyó `public/` del control de versiones.
* Se excluyeron cachés y archivos temporales.
* Se excluyeron archivos de entorno.
* Se excluyeron archivos generados por Visual Studio mediante `.vs/`.
* Se eliminaron del índice Git archivos de workspace generados localmente.
* Se eliminó del repositorio el contenido generado de `node_modules`.
* Se eliminó del repositorio el output generado por Quartz.

#### Planificación

* Sprint 3.1 — Plataforma Base cerrado.
* Sprint 3.2 — Página de Inicio cerrado.
* Sprint 3.3 — Identidad Visual y Navegación cerrado.
* Sprint 3.4 — Estructura Inicial del Conocimiento cerrado.
* Sprint 3.5 — Validación Automática establecido como Sprint activo.

---

### Fixed

* Corrección de la configuración regional de Quartz de `es-MX` a `es-ES`.
* Corrección del build local de Quartz.
* Corrección de dependencias generadas que habían sido incorporadas al repositorio.
* Corrección del seguimiento accidental de `public/`.
* Corrección del seguimiento accidental de archivos `.vs`.
* Corrección de variables de identidad visual afectadas por estilos de compatibilidad mediante variables propias del Atlas.
* Validación del favicon publicado en GitHub Pages.
* Validación del despliegue posterior al merge de `develop` hacia `main`.

---

### Validated

* Build local de Quartz.
* Build de Quartz mediante GitHub Actions.
* Generación del artefacto de GitHub Pages.
* Deploy automático a GitHub Pages.
* Sitio público accesible.
* Favicon visible en producción.
* Identidad visual en modo claro.
* Identidad visual en modo oscuro.
* Navegación de escritorio.
* Navegación móvil.
* Search.
* Explorer.
* Graph.
* Table of Contents.
* Flujo:

```text
develop
   │
   ▼
Pull Request
   │
   ▼
main
   │
   ▼
GitHub Actions
   │
   ▼
Quartz Build
   │
   ▼
GitHub Pages
```

---

## [v0.2.0] - 2026-07-28

### Added

#### Gobernanza

* GOV-001 — Constitución del Atlas de Fitoterapia.

#### Arquitectura

* ADM-001 — Arquitectura General del Atlas.

#### Decisiones Arquitectónicas

* ADR-001 — El ROADMAP como Documento Vivo.
* ADR-002 — Sistema de Identificación Única.
* ADR-003 — Jerarquía Normativa.
* ADR-004 — Arquitectura antes que Implementación.

#### Estándares Editoriales

* EEA-000 — Convenciones Generales.
* EEA-001 — Convenciones Documentales.
* EEA-002 — Convenciones de Nomenclatura.

### Changed

* Se consolidó la arquitectura documental del proyecto.
* Se definió la jerarquía normativa oficial.
* Se formalizó el modelo de gobernanza.
* Se reestructuró el ROADMAP como Plan Director del proyecto.
* Se reorganizó la estructura del repositorio.
* Se actualizó completamente la documentación principal del repositorio.

---

## [v0.1.0] - 2026-07-25

### Added

* Creación del repositorio `atlas-core`.
* Creación del repositorio `atlas-knowledge`.
* Configuración inicial del proyecto.
* Incorporación de Git y GitHub.
* Creación del README inicial.
* Creación del ROADMAP inicial.
* Creación del CHANGELOG inicial.
* Definición del modelo de Releases y Sprints.
* Definición de la planificación inicial del Atlas.

---

## Versionado

El proyecto utiliza **Semantic Versioning**.

```text
MAJOR.MINOR.PATCH

MAJOR  Cambios incompatibles
MINOR  Nuevas funcionalidades
PATCH  Correcciones y mejoras
```

La versión correspondiente a un Release únicamente se incorpora al CHANGELOG cuando dicho Release ha sido cerrado formalmente.

Mientras un Release permanezca activo, sus cambios se documentarán bajo `[Unreleased]`.

---

## Referencias

* Keep a Changelog.
* Semantic Versioning.

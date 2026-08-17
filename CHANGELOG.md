# Changelog

Todos los cambios relevantes del proyecto **Atlas de Fitoterapia** se documentan en este archivo.

El proyecto adopta las recomendaciones de **Keep a Changelog** y utiliza **Semantic Versioning (SemVer)** para el control de versiones.

---

## [Unreleased]

Los cambios correspondientes al Release v0.4 — Arquitectura del Conocimiento se registrarán en esta sección hasta su cierre formal.

---

## [v0.3.0] - 2026-08-16

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

#### Validación Automática

* Herramienta de normalización de Markdown mediante `normalize_markdown.py`.
* Validador de Front Matter mediante `validate_frontmatter.py`.
* Validador de Markdown mediante `validate_markdown.py`.
* Validador de nomenclatura mediante `validate_naming.py`.
* Validador de enlaces internos mediante `validate_links.py`.
* Validador de identificadores duplicados mediante `validate_ids.py`.
* Workflow `Validate Atlas Core` integrado con GitHub Actions.
* Ejecución automática de validaciones sobre `push` a `develop`.
* Ejecución automática de validaciones sobre Pull Requests dirigidos a `main`.
* Fallo automático del workflow cuando los validadores detectan condiciones inválidas.
* Protección de `main` mediante controles requeridos.
* Build de Quartz requerido antes de integrar cambios en `atlas-knowledge`.

#### Plantillas y Flujo Editorial

* Directorio gobernado `30-Plantillas/`.
* TPL-001 — Plantilla de Documento Base.
* Soporte formal del tipo documental `TPL` en las convenciones y herramientas de validación.
* Integración de Obsidian como interfaz local de edición de `atlas-knowledge`.
* Configuración versionada de la carpeta de plantillas mediante `.obsidian/templates.json`.
* Plugin nativo Templates de Obsidian habilitado en la configuración versionada del Vault.
* Acceso local desde `atlas-knowledge` hacia las plantillas gobernadas de `atlas-core` mediante enlace simbólico.
* Flujo editorial mínimo documentado en el README de `atlas-knowledge`.

#### Repositorio

* Flujo de trabajo basado en ramas `develop` y `main`.
* Integración de cambios mediante Pull Request.
* Primer Pull Request formal de `atlas-knowledge` hacia `main`.
* Protección de la rama `main` en `atlas-core`.
* Protección de la rama `main` en `atlas-knowledge`.

---

### Changed

#### Quartz

* Configuración del idioma del sitio a español compatible con Quartz.
* Personalización del título del sitio como `Atlas de Fitoterapia`.
* Personalización del footer.
* Ajuste de la configuración visual de Quartz.
* Incorporación de colores institucionales del Atlas.
* Adaptación de estilos para mantener coherencia entre modo claro y oscuro.
* El workflow de `atlas-knowledge` ejecuta el build de Quartz tanto en Pull Requests hacia `main` como después de la integración en `main`.
* El despliegue a GitHub Pages permanece limitado a ejecuciones posteriores a la integración en `main`.

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

#### Gobernanza y Estándares

* EEA-002 — Convenciones de Nomenclatura actualizado para reflejar la estructura física vigente de `atlas-core`.
* Se formalizó la distinción entre directorios institucionales, técnicos y de conocimiento.
* `30-Plantillas/` se reconoció formalmente como directorio institucional.
* Se mantuvo deliberadamente sin definir la estructura definitiva de directorios de conocimiento hasta el Release v0.4.
* Las plantillas científicas definitivas se mantienen diferidas hasta la aprobación del Modelo de Información.

#### Flujo Editorial

* Obsidian se estableció como interfaz opcional de edición y no como fuente de verdad del Atlas.
* Las plantillas oficiales permanecen gobernadas en `atlas-core`.
* El contenido editorial permanece en `atlas-knowledge`.
* La integración local entre ambos repositorios evita duplicar físicamente las plantillas.
* La configuración específica del enlace simbólico se mantiene local y fuera del control de versiones.
* El flujo editorial se mantiene desacoplado de Obsidian para permitir sustituir la herramienta de edición sin modificar la arquitectura del Atlas.

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
* Sprint 3.5 — Validación Automática cerrado.
* Sprint 3.6 — Plantillas y Flujo Editorial cerrado.
* Sprint 3.7 — Validación Integral y Cierre cerrado.
* Release v0.3 — Infraestructura Tecnológica cerrado.
* Release v0.4 — Arquitectura del Conocimiento establecido como Release activo.
* Sprint 4.1 — Modelo Híbrido del Conocimiento establecido como Sprint activo.
* La descripción de la plantilla prevista para Sprint 3.6 se ajustó para reflejar una plantilla documental base sin anticipar el modelo científico del Release v0.4.

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
* Corrección en EEA-002 de referencias a directorios institucionales que ya no correspondían con la estructura física vigente.
* Restauración de archivos internos de Quartz modificados durante pruebas locales para evitar incorporar artefactos de ejecución al repositorio.
* Corrección de la invocación de Quartz en GitHub Actions mediante `node ./quartz/bootstrap-cli.mjs` para asegurar su ejecución en el entorno CI.
* Corrección del contexto requerido del build de Quartz dentro de las reglas de protección de `main`.

---

### Validated

#### Plataforma y Publicación

* Edición local.
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
* Enlaces internos.
* Navegación principal completa sin errores 404.
* Flujo completo de publicación desde `develop` hasta GitHub Pages.

#### Validación Automática

* Normalización de Markdown.
* Validación de Front Matter.
* Validación estructural de Markdown.
* Validación de nomenclatura.
* Validación de enlaces internos.
* Detección de identificadores duplicados.
* Pruebas positivas de los validadores.
* Pruebas negativas de los validadores.
* Fallo del workflow de GitHub Actions ante errores detectados.
* Ejecución reproducible de los controles tanto localmente como mediante CI.
* Bloqueo efectivo del merge en `atlas-core` cuando falla un control requerido.
* Bloqueo efectivo del merge en `atlas-knowledge` cuando falla el build requerido.
* Protección efectiva de `main` mediante Rulesets.
* Imposibilidad de integrar un Pull Request mientras permanezca fallido un control requerido.

#### Plantillas y Flujo Editorial

* TPL-001 compatible con las convenciones documentales vigentes.
* Tipo documental `TPL` reconocido por el validador de nomenclatura.
* Inserción de TPL-001 desde Obsidian.
* Creación de un documento editorial temporal desde Obsidian.
* Almacenamiento del documento de prueba dentro de `atlas-knowledge/content`.
* Procesamiento del documento creado desde Obsidian mediante Quartz.
* Build local de Quartz con el documento editorial de prueba.
* Eliminación posterior del documento temporal utilizado para la validación.
* Exclusión local del enlace simbólico de plantillas del control de versiones.
* Reproducibilidad documentada de la configuración editorial en una estación de trabajo.

#### Flujo de Publicación

Se validó integralmente el flujo:

```text
develop
   │
   ▼
Pull Request
   │
   ▼
Build requerido
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
Artefacto GitHub Pages
   │
   ▼
Deploy
   │
   ▼
GitHub Pages

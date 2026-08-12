---

id: ROADMAP
title: Plan Director del Atlas de Fitoterapia
version: 1.2.0
status: Approved
type: ROADMAP
created: 2026-07-25
updated: 2026-08-12
author: Proyecto Atlas de Fitoterapia
tags:

* roadmap
* governance
* planning

---

# Plan Director del Atlas de Fitoterapia

## 1. Propósito

El ROADMAP constituye el documento oficial de planificación estratégica y operativa del Atlas de Fitoterapia.

Define la evolución del proyecto mediante Releases, Sprints, Entregables y Capacidades, estableciendo el alcance aprobado, las prioridades de desarrollo y el estado real del proyecto.

Conforme al ADR-001, este documento es un documento vivo y representa la única fuente oficial para conocer la planificación vigente del Atlas.

---

## 2. Alcance

Este documento aplica a todo el proyecto Atlas de Fitoterapia.

Toda iniciativa, capacidad, documento, componente arquitectónico o desarrollo tecnológico deberá encontrarse planificado dentro del presente ROADMAP antes de iniciar su ejecución.

---

## 3. Estado General del Proyecto

| Elemento              | Estado                                     |
| --------------------- | ------------------------------------------ |
| Proyecto              | Atlas de Fitoterapia                       |
| Estado general        | 🟢 Plataforma tecnológica operativa        |
| Release activo        | Release v0.3 — Infraestructura Tecnológica |
| Sprint activo         | Sprint 3.5 — Validación Automática         |
| Versión del documento | 1.2.0                                      |
| Última actualización  | 2026-08-12                                 |

---

## 4. Métricas Ejecutivas

| Indicador                       | Valor |
| ------------------------------- | ----: |
| Releases completados            |     2 |
| Release activo                  |  v0.3 |
| Sprints completados             |     5 |
| Sprint activo                   |   3.5 |
| Documentos normativos aprobados |     9 |
| GOV                             |     1 |
| ADR                             |     4 |
| ADM                             |     1 |
| EEA                             |     3 |

---

## 5. Visión Estratégica

Construir el Atlas de Fitoterapia más completo, interoperable y científicamente sustentado en idioma español mediante un modelo de conocimiento estructurado, trazable, reutilizable y gobernado.

---

## 6. Principios de Planificación

La evolución del Atlas se regirá por los siguientes principios:

* La arquitectura precede a la implementación.
* El conocimiento se define una única vez y se reutiliza.
* Cada documento debe aportar una responsabilidad arquitectónica única.
* Cada Sprint deberá generar capacidades concretas y verificables.
* Solo el Release activo y el siguiente se planifican en detalle.
* Los Releases posteriores permanecerán en planificación estratégica hasta su inicio.
* Todo cambio aprobado deberá reflejarse primero en el ROADMAP y posteriormente en el CHANGELOG.
* El Atlas evolucionará por niveles de abstracción.
* La documentación existente se actualizará cuando un Sprint modifique planificación, arquitectura, gobernanza o estándares.
* Se evitará crear documentos nuevos cuando la información pueda incorporarse adecuadamente en documentos existentes.
* Los Sprints priorizarán capacidades funcionales sobre documentación adicional.
* Las automatizaciones deberán respetar la gobernanza y los estándares aprobados.
* El conocimiento deberá mantenerse independiente de su mecanismo de presentación.

---

## 7. Arquitectura de Planificación

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

# 8. Releases

## Release v0.1 — Fundación

**Estado:** ✅ Completado

### Propósito arquitectónico

Establecer la infraestructura inicial del proyecto y crear las condiciones mínimas para comenzar el desarrollo del Atlas.

### Sprint 0.1 — Fundación del Proyecto

**Estado:** ✅ Completado

#### Objetivo

Crear la estructura inicial del Atlas, sus repositorios y las herramientas básicas de trabajo.

#### Entregables

* [x] Crear organización del proyecto.
* [x] Crear repositorio `atlas-core`.
* [x] Crear repositorio `atlas-knowledge`.
* [x] Instalar Git.
* [x] Instalar GitHub Desktop.
* [x] Instalar Obsidian.
* [x] Definir arquitectura inicial.
* [x] Crear estructura inicial del repositorio.
* [x] Crear `README.md`.
* [x] Crear `ROADMAP.md`.
* [x] Crear `CHANGELOG.md`.
* [x] Realizar primer commit oficial.

#### Resultado

El proyecto quedó constituido técnicamente y preparado para formalizar su gobernanza.

---

## Release v0.2 — Gobernanza

**Estado:** ✅ Completado

### Propósito arquitectónico

Definir la gobernanza, arquitectura documental y estándares que regirán todo el Atlas.

### Sprint 0.2 — Gobierno del Atlas

**Estado:** ✅ Completado

#### Objetivo

Formalizar las reglas de gobierno, decisiones arquitectónicas y estándares documentales del proyecto.

#### Entregables

* [x] GOV-001 — Constitución del Atlas de Fitoterapia.
* [x] ADR-001 — ROADMAP como Documento Vivo.
* [x] ADR-002 — Sistema de Identificación Única.
* [x] ADR-003 — Jerarquía Normativa.
* [x] ADR-004 — Arquitectura antes que Implementación.
* [x] ADM-001 — Arquitectura General del Atlas.
* [x] EEA-000 — Convenciones Generales.
* [x] EEA-001 — Convenciones Documentales.
* [x] EEA-002 — Convenciones de Nomenclatura.

#### Capacidades obtenidas

* [x] Gobernanza formal del proyecto.
* [x] Jerarquía normativa definida.
* [x] Identificación única de objetos gobernados.
* [x] Arquitectura documental consolidada.
* [x] Convenciones editoriales consolidadas.
* [x] Convenciones de nomenclatura consolidadas.
* [x] ROADMAP establecido como documento vivo.
* [x] Separación formal entre arquitectura e implementación.

#### Resultado

La capa de gobernanza del Atlas quedó consolidada y se convirtió en la base normativa para los Releases posteriores.

---

## Release v0.3 — Infraestructura Tecnológica

**Estado:** 🟡 En progreso

### Propósito arquitectónico

Implementar la infraestructura tecnológica que soportará el desarrollo, validación, automatización y publicación del Atlas.

### Resultado esperado del Release

Al finalizar el Release v0.3, el Atlas deberá contar con una plataforma funcional capaz de:

* editar contenido;
* validar contenido;
* compilar el sitio;
* publicar automáticamente;
* mantener separación entre gobernanza y conocimiento;
* proporcionar navegación básica;
* soportar el crecimiento del modelo de conocimiento.

---

### Sprint 3.1 — Plataforma Base

**Estado:** ✅ Completado

#### Objetivo

Establecer y validar la infraestructura base de ejecución y publicación del Atlas.

#### Capacidades implementadas

* [x] Node.js instalado y validado.
* [x] npm configurado.
* [x] Quartz 5 instalado.
* [x] Quartz configurado.
* [x] Build local validado.
* [x] GitHub Pages operativo.
* [x] GitHub Actions operativo.
* [x] Flujo automático de despliegue desde `main`.
* [x] Publicación automática del sitio.
* [x] Repositorio `atlas-knowledge` operando como plataforma de publicación.
* [x] `atlas-core` conservado como repositorio de gobernanza, arquitectura y estándares.
* [x] Exclusión de `node_modules` del control de versiones.
* [x] Exclusión de `public/` del control de versiones.
* [x] Exclusión de cachés y archivos temporales.
* [x] `.gitignore` fortalecido.
* [x] Configuración regional de Quartz ajustada a español compatible.
* [x] Validación del pipeline GitHub → Actions → Quartz → GitHub Pages.

#### Arquitectura tecnológica resultante

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

#### Resultado

La plataforma tecnológica base del Atlas quedó operativa tanto localmente como en GitHub.

---

### Sprint 3.2 — Página de Inicio

**Estado:** ✅ Completado

#### Objetivo

Crear la página principal institucional del Atlas y establecer su primera experiencia pública.

#### Capacidades implementadas

* [x] Página principal del Atlas definida.
* [x] Nombre `Atlas de Fitoterapia` incorporado.
* [x] Propósito visible.
* [x] Alcance inicial visible.
* [x] Misión incorporada.
* [x] Principios del proyecto incorporados.
* [x] Estado del proyecto visible.
* [x] Aviso científico incorporado.
* [x] Navegación conceptual descrita.
* [x] Página compilada correctamente mediante Quartz.

#### Resultado

El sitio dejó de ser una instalación genérica de Quartz y comenzó a representar públicamente al Atlas de Fitoterapia.

---

### Sprint 3.3 — Identidad Visual y Navegación

**Estado:** ✅ Completado

#### Objetivo

Dotar al sitio de una identidad visual mínima y establecer una navegación coherente con la arquitectura del Atlas.

#### Capacidades implementadas

##### Identidad

* [x] Nombre del sitio configurado como `Atlas de Fitoterapia`.
* [x] Idioma configurado en español.
* [x] Favicon botánico temporal implementado.
* [x] Paleta visual inicial implementada.
* [x] Modo claro validado.
* [x] Modo oscuro validado.
* [x] Footer institucional configurado.
* [x] Tipografía validada en la interfaz.
* [x] Contraste y legibilidad validados.
* [x] Identidad visual validada en el sitio publicado.

##### Navegación

* [x] Navegación principal incorporada a la página inicial.
* [x] Orden conceptual de navegación definido.
* [x] Explorer validado como navegación secundaria.
* [x] Search validado.
* [x] Graph validado.
* [x] Table of Contents validada.
* [x] Navegación móvil validada.
* [x] Visualización responsive validada.
* [x] Sitio publicado validado mediante GitHub Pages.

#### Navegación principal aprobada

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

El Explorer conserva orden alfabético y funciona como mecanismo secundario de navegación.

#### Decisiones de alcance

La personalización de la página 404 no constituye un criterio necesario para el cierre del Sprint y podrá evaluarse posteriormente si aporta valor funcional.

#### Resultado

El Atlas cuenta con una identidad visual inicial coherente, navegación funcional y experiencia básica validada tanto en escritorio como en dispositivos móviles.

---

### Sprint 3.4 — Estructura Inicial del Conocimiento

**Estado:** ✅ Completado

#### Objetivo

Crear la estructura mínima de navegación del conocimiento sin anticipar todavía el modelo formal que será definido en el Release v0.4.

#### Estructura implementada

```text
content/
├── index.md
├── dominios/
│   └── index.md
├── especies/
│   └── index.md
├── principios-activos/
│   └── index.md
├── preparados/
│   └── index.md
├── enfermedades/
│   └── index.md
├── farmacopeas/
│   └── index.md
└── referencias/
    └── index.md
```

#### Capacidades implementadas

* [x] Crear sección `dominios`.
* [x] Crear sección `especies`.
* [x] Crear sección `principios-activos`.
* [x] Crear sección `preparados`.
* [x] Crear sección `enfermedades`.
* [x] Crear sección `farmacopeas`.
* [x] Crear sección `referencias`.
* [x] Crear página índice para cada sección.
* [x] Incorporar Front Matter mínimo.
* [x] Validar compilación de Quartz con ocho archivos Markdown.
* [x] Confirmar generación correcta de `public/`.
* [x] Versionar la estructura mediante Git.
* [x] Integrar los cambios mediante Pull Request `develop → main`.
* [x] Validar despliegue mediante GitHub Actions.
* [x] Validar navegación desde GitHub Pages.
* [x] Validar nombres visibles de las secciones.
* [x] Validar favicon en producción.
* [x] Validar identidad visual en producción.

#### Restricción

Esta estructura constituye únicamente un scaffold tecnológico y editorial inicial.

No representa todavía el modelo formal de dominios, entidades o relaciones del Atlas.

El modelo definitivo será definido durante el Release v0.4, particularmente mediante ADM-003 y ADM-004.

#### Resultado

El repositorio `atlas-knowledge` dispone de una estructura inicial navegable y publicada que permitirá recibir posteriormente el modelo formal de conocimiento sin anticipar sus decisiones arquitectónicas.

---

### Sprint 3.5 — Validación Automática

**Estado:** 🟡 En progreso

#### Objetivo

Implementar controles automáticos que prevengan la incorporación o publicación de contenido estructuralmente inválido.

#### Capacidades previstas

* [ ] Validación automática de Front Matter.
* [ ] Validación automática de Markdown.
* [ ] Validación automática de nomenclatura.
* [ ] Validación automática de enlaces.
* [ ] Detección de identificadores duplicados.
* [ ] Detección de archivos huérfanos cuando corresponda.
* [ ] Integración de validaciones con GitHub Actions.
* [ ] Bloqueo de publicación ante errores críticos.

#### Principios de implementación

* Las validaciones deberán automatizar reglas existentes.
* No deberán introducir reglas arquitectónicas nuevas fuera de los documentos normativos vigentes.
* Las reglas deberán ser reproducibles tanto localmente como en CI.
* Un error crítico deberá impedir la publicación.
* Las advertencias no críticas deberán ser distinguibles de los errores de bloqueo.

#### Resultado esperado

Todo contenido deberá superar controles automáticos mínimos antes de ser publicado.

---

### Sprint 3.6 — Plantillas y Flujo Editorial

**Estado:** ⚪ Planeado

#### Objetivo

Preparar las plantillas y mecanismos mínimos necesarios para incorporar conocimiento de forma consistente.

#### Capacidades previstas

* [ ] Plantilla base para contenido científico.
* [ ] Plantilla compatible con Front Matter definido.
* [ ] Integración con convenciones EEA.
* [ ] Compatibilidad con Obsidian.
* [ ] Compatibilidad con Quartz.
* [ ] Validación de uso de plantillas.

#### Restricción

Las plantillas científicas definitivas dependerán del Modelo de Información definido en el Release v0.4.

Por tanto, este Sprint solo deberá implementar plantillas que no anticipen decisiones del modelo de conocimiento.

---

### Sprint 3.7 — Validación Integral y Cierre

**Estado:** ⚪ Planeado

#### Objetivo

Validar de extremo a extremo la plataforma antes de cerrar el Release v0.3.

#### Validaciones previstas

* [ ] Edición local.
* [ ] Build local.
* [ ] Commit.
* [ ] Push.
* [ ] Pull Request.
* [ ] Merge hacia `main`.
* [ ] Ejecución de GitHub Actions.
* [ ] Validaciones automáticas.
* [ ] Build Quartz.
* [ ] Generación de artefacto.
* [ ] Deploy GitHub Pages.
* [ ] Navegación.
* [ ] Search.
* [ ] Graph.
* [ ] Enlaces internos.
* [ ] Visualización móvil.
* [ ] Recuperación ante fallo de build.

#### Criterios de cierre

El Release v0.3 se considerará completado cuando:

* [ ] Quartz compile correctamente.
* [ ] GitHub Pages publique automáticamente.
* [ ] GitHub Actions ejecute el pipeline completo.
* [ ] Las validaciones automáticas estén operativas.
* [ ] La navegación sea funcional.
* [ ] El sitio sea accesible públicamente.
* [ ] El flujo `develop → Pull Request → main → GitHub Actions → GitHub Pages` esté validado integralmente.
* [ ] La infraestructura permita comenzar el Release v0.4 sin rediseño técnico.
* [ ] ROADMAP actualizado.
* [ ] CHANGELOG actualizado.

---

## Release v0.4 — Arquitectura del Conocimiento

**Estado:** ⚪ Planeado

### Propósito arquitectónico

Diseñar y aprobar la arquitectura conceptual del Atlas mediante un modelo híbrido orientado por dominios de conocimiento.

### Arquitectura conceptual objetivo

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

Las monografías serán vistas editoriales construidas a partir de entidades, atributos y relaciones del modelo de conocimiento.

---

### Sprint 4.1 — Modelo Híbrido del Conocimiento

**Estado:** ⚪ Planeado

#### Objetivo

Formalizar el modelo conceptual mediante el cual se organizará el conocimiento del Atlas.

#### Entregable

* [ ] ADR-005 — Modelo Híbrido del Conocimiento.

#### Resultado esperado

Definir formalmente que el Atlas será construido por dominios, entidades y relaciones, y no mediante acumulación independiente de documentos.

---

### Sprint 4.2 — Arquitectura del Modelo de Conocimiento

**Estado:** ⚪ Planeado

#### Objetivo

Definir la arquitectura general que conectará dominios, entidades, relaciones y vistas editoriales.

#### Entregable

* [ ] ADM-002 — Arquitectura del Modelo de Conocimiento.

---

### Sprint 4.3 — Dominios de Conocimiento

**Estado:** ⚪ Planeado

#### Objetivo

Definir formalmente los dominios y subdominios que estructurarán el Atlas.

#### Entregable

* [ ] ADM-003 — Dominios de Conocimiento del Atlas.

#### Consideraciones

Los dominios deberán permitir incorporar, entre otros:

* botánica;
* farmacognosia;
* fitoquímica;
* farmacología;
* evidencia clínica;
* seguridad;
* toxicología;
* regulación;
* preparados;
* referencias.

La lista definitiva será definida durante este Sprint.

---

### Sprint 4.4 — Modelo de Información

**Estado:** ⚪ Planeado

#### Objetivo

Definir la estructura formal de la información del Atlas.

#### Entregable

* [ ] ADM-004 — Modelo de Información del Atlas.

#### El modelo deberá definir

* entidades;
* atributos;
* relaciones;
* identificadores;
* cardinalidades;
* metadatos;
* procedencia;
* trazabilidad;
* reglas mínimas de interoperabilidad.

#### Preparación para agentes

El modelo deberá poder ser interpretado tanto por personas como por software, permitiendo posteriormente la integración de sistemas automáticos y agentes de inteligencia artificial.

---

### Principio de diseño del Release v0.4

Cada documento deberá introducir una responsabilidad arquitectónica nueva.

No se crearán:

* catálogos redundantes de entidades;
* diccionarios duplicados;
* glosarios que reproduzcan información existente;
* documentos cuya responsabilidad pueda integrarse en ADM-002, ADM-003 o ADM-004.

---

## 9. Releases Estratégicos

Los Releases posteriores permanecerán en planificación estratégica hasta el inicio formal de su ejecución.

Solo se desarrollarán en detalle cuando el Release precedente permita conocer con suficiente precisión su alcance.

| Release | Propósito                             | Estado                 |
| ------- | ------------------------------------- | ---------------------- |
| v0.5    | Por definir                           | ⚪ Planeación pendiente |
| v0.6    | Por definir                           | ⚪ Planeación pendiente |
| v0.7    | Por definir                           | ⚪ Planeación pendiente |
| v0.8    | Por definir                           | ⚪ Planeación pendiente |
| v0.9    | Por definir                           | ⚪ Planeación pendiente |
| v1.0    | Primera publicación oficial del Atlas | ⚪ Planeación pendiente |

---

## 10. Backlog Estratégico

Las iniciativas registradas en esta sección no forman parte del alcance aprobado.

Solo podrán desarrollarse después de ser evaluadas e incorporadas formalmente a un Release.

| ID     | Iniciativa                                                                   | Estado    |
| ------ | ---------------------------------------------------------------------------- | --------- |
| BP-001 | PROJECT_STATE.md                                                             | Propuesta |
| BP-002 | Sistema de agentes para vigilancia científica y detección de nueva evidencia | Propuesta |

### BP-002 — Vigilancia Científica Automatizada

La iniciativa contempla la incorporación futura de agentes especializados capaces de:

* monitorear nuevas publicaciones científicas;
* detectar nuevos ensayos clínicos;
* identificar cambios en estudios registrados;
* monitorear fuentes botánicas y taxonómicas;
* detectar nueva evidencia de seguridad;
* detectar nueva evidencia fitoquímica;
* identificar metaanálisis y revisiones sistemáticas;
* clasificar información científica;
* identificar duplicados;
* comparar nueva evidencia contra el conocimiento existente;
* proponer actualizaciones del Atlas;
* conservar trazabilidad hacia las fuentes originales.

### Principio de gobernanza

Los agentes podrán:

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

Pero no podrán incorporar conocimiento oficial automáticamente.

La incorporación deberá pasar por:

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

---

## 11. Reglas del ROADMAP

1. El ROADMAP constituye el plan director del Atlas.
2. Todo trabajo deberá encontrarse registrado antes de iniciar su ejecución.
3. Ninguna capacidad, entregable o documento nuevo podrá desarrollarse fuera del alcance definido por un Release.
4. Cada entregable deberá aportar una responsabilidad arquitectónica o capacidad nueva.
5. Se evitará la creación de documentos duplicados o con responsabilidades superpuestas.
6. Los Releases deberán completarse antes de iniciar formalmente el siguiente.
7. Podrán existir trabajos preparatorios o Sprints paralelos dentro del mismo Release cuando no generen dependencias contradictorias.
8. Los Releases posteriores al activo podrán mantenerse únicamente en planificación estratégica.
9. Solo el Release activo y el siguiente se planifican en detalle.
10. Todo cambio aprobado deberá actualizar primero el ROADMAP y posteriormente el CHANGELOG.
11. El ROADMAP deberá reflejar permanentemente el estado real del proyecto.
12. Los Sprints deberán priorizar capacidades funcionales sobre documentación adicional.
13. Al finalizar cada Sprint deberá evaluarse qué documentos existentes requieren actualización.
14. Solo se crearán nuevos documentos cuando exista una necesidad de gobernanza, arquitectura o estandarización que no pueda resolverse mediante documentación existente.
15. El conocimiento deberá mantenerse independiente del mecanismo de presentación.
16. La automatización deberá respetar en todo momento las reglas de gobernanza del Atlas.
17. Las validaciones automáticas deberán implementar reglas existentes y no crear gobernanza implícita.
18. Los cambios destinados a publicación deberán integrarse a `main` mediante el flujo de control aprobado para el repositorio.

---

## 12. Estado del Proyecto

```text
v0.1  Fundación                       ✅ Completado
v0.2  Gobernanza                      ✅ Completado
v0.3  Infraestructura Tecnológica     🟡 En progreso
v0.4  Arquitectura del Conocimiento   ⚪ Planeado
v0.5+ Evolución estratégica           ⚪ Pendiente
```

### Estado de Sprints

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
├── Sprint 3.5  Validación Automática                 🟡
├── Sprint 3.6  Plantillas y Flujo Editorial          ⚪
└── Sprint 3.7  Validación Integral y Cierre          ⚪

Release v0.4
├── Sprint 4.1  Modelo Híbrido del Conocimiento       ⚪
├── Sprint 4.2  Arquitectura del Modelo               ⚪
├── Sprint 4.3  Dominios de Conocimiento              ⚪
└── Sprint 4.4  Modelo de Información                 ⚪
```

### Dependencia entre Releases

```text
v0.1 Fundación
        │
        ▼
v0.2 Gobernanza
        │
        ▼
v0.3 Infraestructura Tecnológica
        │
        ▼
v0.4 Arquitectura del Conocimiento
        │
        ▼
Releases posteriores
```

---

## 13. Referencias

* GOV-001 — Constitución del Atlas de Fitoterapia.
* ADR-001 — ROADMAP como Documento Vivo.
* ADR-002 — Sistema de Identificación Única.
* ADR-003 — Jerarquía Normativa.
* ADR-004 — Arquitectura antes que Implementación.
* ADM-001 — Arquitectura General del Atlas.
* EEA-000 — Convenciones Generales.
* EEA-001 — Convenciones Documentales.
* EEA-002 — Convenciones de Nomenclatura.

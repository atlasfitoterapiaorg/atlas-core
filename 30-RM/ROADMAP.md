---
id: ROADMAP
title: Plan Director del Atlas de Fitoterapia
version: 1.4.0
status: Approved
type: ROADMAP
created: 2026-07-25
updated: 2026-08-25
author: Proyecto Atlas de Fitoterapia
tags:
  - roadmap
  - governance
  - planning
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

| Elemento              | Estado                                              |
| --------------------- | --------------------------------------------------- |
| Proyecto              | Atlas de Fitoterapia                                |
| Estado general        | 🟢 Arquitectura del conocimiento completada         |
| Release activo        | Ninguno — Release v0.5 pendiente de definición      |
| Sprint activo         | Ninguno                                              |
| Versión del documento | 1.4.0                                               |
| Última actualización  | 2026-08-25                                          |

---

## 4. Métricas Ejecutivas

| Indicador                       | Valor |
| ------------------------------- | ----: |
| Releases completados            |     4 |
| Release activo                  |     — |
| Sprints completados             |    13 |
| Sprint activo                   |     — |
| Documentos normativos aprobados |    14 |
| GOV                             |     1 |
| ADR                             |     5 |
| ADM                             |     4 |
| EEA                             |     3 |
| TPL                             |     1 |

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

**Estado:** ✅ Completado

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

**Estado:** ✅ Completado

#### Objetivo

Implementar controles automáticos que prevengan la incorporación de contenido estructuralmente inválido dentro del flujo de integración del Atlas.

#### Capacidades implementadas

* [x] Validación automática de Front Matter.
* [x] Validación automática de Markdown.
* [x] Validación automática de nomenclatura.
* [x] Validación automática de enlaces internos.
* [x] Detección de identificadores duplicados.
* [x] Integración de validaciones con GitHub Actions.
* [x] Ejecución automática sobre `push` a `develop`.
* [x] Ejecución automática sobre Pull Requests dirigidos a `main`.
* [x] Pruebas positivas y negativas de los validadores implementados.
* [x] Fallo del workflow de GitHub Actions cuando una validación detecta errores.

#### Controles implementados

```text
Validate Atlas Core
│
├── Validate Front Matter
├── Validate Markdown
├── Validate Naming
├── Validate Links
└── Validate IDs
```

#### Decisiones de alcance

La detección automática de archivos huérfanos no se implementa en `atlas-core` durante este Sprint.

Esta capacidad resulta más pertinente para `atlas-knowledge`, donde los documentos formarán parte de una estructura navegable y posteriormente de un grafo formal de conocimiento. Su implementación deberá evaluarse cuando exista el modelo de conocimiento correspondiente.

La validación específica de que un fallo de los controles automáticos impida físicamente el merge hacia `main` o la publicación final se difiere al Sprint 3.7 — Validación Integral y Cierre, donde se validará de extremo a extremo el flujo de integración y publicación.

#### Principios de implementación

* Las validaciones automatizan reglas existentes.
* No introducen reglas arquitectónicas nuevas fuera de los documentos normativos vigentes.
* Las reglas son reproducibles tanto localmente como en CI.
* Un error detectado provoca el fallo del workflow de validación.
* La validación integral de las restricciones de merge y publicación corresponde al Sprint 3.7.

#### Resultado

`atlas-core` dispone de una capa automática de validación estructural capaz de detectar errores de Front Matter, Markdown, nomenclatura, enlaces internos e identificadores duplicados.

Los cinco controles se ejecutan mediante GitHub Actions y producen un fallo del workflow cuando detectan una condición inválida.

---

### Sprint 3.6 — Plantillas y Flujo Editorial

**Estado:** ✅ Completado

#### Objetivo

Preparar las plantillas y mecanismos mínimos necesarios para incorporar contenido de forma consistente sin anticipar el modelo formal de conocimiento.

#### Capacidades implementadas

* [x] Plantilla documental base gobernada.
* [x] Plantilla compatible con el Front Matter definido.
* [x] Integración con las convenciones EEA.
* [x] Tipo documental `TPL` validado mediante controles automáticos.
* [x] `TPL-001 — Plantilla de Documento Base` implementada.
* [x] Directorio `30-Plantillas/` incorporado formalmente a las convenciones de nomenclatura.
* [x] Obsidian configurado como interfaz local de edición.
* [x] `atlas-knowledge` validado como Vault de Obsidian.
* [x] Plugin nativo Templates habilitado.
* [x] Acceso local desde Obsidian a las plantillas gobernadas mediante enlace simbólico.
* [x] Configuración `templates` registrada en `.obsidian/templates.json`.
* [x] Flujo de inserción de plantilla desde Obsidian validado.
* [x] Creación de documento editorial de prueba validada.
* [x] Almacenamiento de contenido dentro de `atlas-knowledge/content` validado.
* [x] Compatibilidad con Quartz validada mediante build local.
* [x] Flujo editorial mínimo documentado en `atlas-knowledge`.
* [x] Artefactos de prueba eliminados después de la validación.

#### Flujo editorial validado

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
Obsidian
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

Obsidian funciona como interfaz local de edición y no como fuente de verdad ni como componente arquitectónico obligatorio.

Las plantillas oficiales permanecen gobernadas en `atlas-core`.

El contenido permanece en `atlas-knowledge`.

La integración local mediante enlace simbólico permite evitar la duplicación física de plantillas entre ambos repositorios.

#### Decisiones de alcance

La plantilla implementada durante este Sprint es una plantilla documental base.

No constituye todavía una plantilla científica definitiva ni define la estructura formal de monografías, entidades o vistas editoriales.

Las plantillas científicas definitivas dependerán del Modelo de Información definido durante el Release v0.4.

La configuración específica de cada estación de trabajo, incluyendo el enlace simbólico hacia las plantillas, permanece como configuración local y no constituye una dependencia obligatoria del repositorio.

#### Resultado

El Atlas dispone de un flujo editorial mínimo, reproducible y desacoplado de la herramienta de edición.

Las plantillas se gobiernan desde `atlas-core`, Obsidian puede utilizarlas para crear contenido en `atlas-knowledge` y Quartz puede procesar correctamente los documentos resultantes.

La infraestructura queda preparada para incorporar posteriormente las plantillas científicas derivadas del modelo formal de conocimiento.

---

### Sprint 3.7 — Validación Integral y Cierre

**Estado:** ✅ Completado

#### Objetivo

Validar de extremo a extremo la plataforma antes de cerrar el Release v0.3.

#### Validaciones previstas

* [x] Edición local.
* [x] Build local.
* [x] Commit.
* [x] Push.
* [x] Pull Request.
* [x] Merge hacia `main`.
* [x] Ejecución de GitHub Actions.
* [x] Validaciones automáticas.
* [x] Bloqueo efectivo del merge ante controles requeridos fallidos.
* [x] Bloqueo efectivo de publicación ante errores críticos.
* [x] Build Quartz.
* [x] Generación de artefacto.
* [x] Deploy GitHub Pages.
* [x] Navegación.
* [x] Search.
* [x] Graph.
* [x] Enlaces internos.
* [x] Visualización móvil.
* [x] Recuperación ante fallo de build.

#### Criterios de cierre

El Release v0.3 se considerará completado cuando:

* [x] Quartz compile correctamente.
* [x] GitHub Pages publique automáticamente.
* [x] GitHub Actions ejecute el pipeline completo.
* [x] Las validaciones automáticas estén operativas.
* [x] Los controles requeridos impidan la integración o publicación cuando corresponda.
* [x] La navegación sea funcional.
* [x] El sitio sea accesible públicamente.
* [x] El flujo `develop → Pull Request → main → GitHub Actions → GitHub Pages` esté validado integralmente.
* [x] La infraestructura permita comenzar el Release v0.4 sin rediseño técnico.
* [x] ROADMAP actualizado.
* [x] CHANGELOG actualizado.

---

## Release v0.4 — Arquitectura del Conocimiento

**Estado:** ✅ Completado

### Propósito arquitectónico

Diseñar y aprobar la arquitectura conceptual del Atlas mediante un modelo híbrido de conocimiento estructurado por dominios, entidades, relaciones, afirmaciones, evidencia y procedencia.

### Arquitectura conceptual resultante

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
Afirmaciones y Evidencia
 │
 ▼
Procedencia
 │
 ▼
Grafo de Conocimiento
 │
 ▼
Vistas Editoriales
```

Las monografías se establecen como vistas editoriales construidas a partir del conocimiento gobernado y no como contenedores primarios de identidad.

---

### Sprint 4.1 — Modelo Híbrido del Conocimiento

**Estado:** ✅ Completado

#### Objetivo

Formalizar el modelo conceptual mediante el cual se organizará el conocimiento del Atlas.

#### Entregable

* [x] ADR-005 — Modelo Híbrido del Conocimiento.

#### Capacidades obtenidas

* [x] Separación entre entidades y documentos.
* [x] Relaciones independientes de la representación editorial.
* [x] Integración explícita de afirmaciones, evidencia y procedencia.
* [x] Distinción entre fuente externa e identidad gobernada.
* [x] Preservación de evidencia contradictoria.
* [x] Base arquitectónica para automatización futura sin aprobación automática.

#### Resultado

El Atlas adoptó formalmente un modelo híbrido en el que las entidades y relaciones constituyen la estructura del conocimiento y los documentos actúan como representaciones editoriales.

---

### Sprint 4.2 — Arquitectura del Modelo de Conocimiento

**Estado:** ✅ Completado

#### Objetivo

Definir la arquitectura general que conecta dominios, entidades, relaciones, afirmaciones, evidencia, procedencia, grafo de conocimiento y vistas editoriales.

#### Entregable

* [x] ADM-002 — Arquitectura del Modelo de Conocimiento.

#### Capacidades obtenidas

* [x] Arquitectura conceptual organizada en siete capas.
* [x] Separación formal entre Dominios, Entidades, Relaciones, Afirmaciones y Evidencia, Procedencia, Grafo y Vistas Editoriales.
* [x] Arquitectura taxonómica principal definida.
* [x] Especie establecida como unidad biológica principal para documentación fitoterapéutica.
* [x] Prohibición de herencia automática de propiedades entre niveles taxonómicos.
* [x] Procedencia establecida como propiedad arquitectónica fundamental.

#### Resultado

Quedó definida la arquitectura conceptual sobre la cual pueden desarrollarse dominios, entidades, relaciones y modelos de información sin depender de una tecnología de almacenamiento específica.

---

### Sprint 4.3 — Dominios de Conocimiento

**Estado:** ✅ Completado

#### Objetivo

Definir formalmente los dominios y subdominios que estructuran el Atlas.

#### Entregable

* [x] ADM-003 — Dominios de Conocimiento del Atlas.

#### Dominios aprobados

```text
1. Botánica
2. Farmacognosia
3. Fitoquímica
4. Etnobotánica y Uso Tradicional
5. Farmacología
6. Evidencia Científica y Clínica
7. Uso Terapéutico
8. Seguridad y Toxicología
9. Regulación y Farmacopeas
```

Fuentes y Procedencia se establecieron como capa transversal y no como dominio temático independiente.

#### Capacidades obtenidas

* [x] Límites conceptuales entre los nueve dominios.
* [x] Separación entre taxonomía, farmacognosia y fitoquímica.
* [x] Separación entre uso tradicional, uso terapéutico y evidencia.
* [x] Separación entre actividad farmacológica y evidencia experimental.
* [x] Diferenciación entre calidad farmacognóstica y regulación farmacopéica.
* [x] Principio de cobertura no obligatoria aplicado a todos los dominios.
* [x] Preservación de información contradictoria y ausencia de inferencia automática.

#### Resultado

El Atlas dispone de una organización temática oficial suficientemente definida para estructurar su conocimiento sin convertir los dominios en silos independientes.

---

### Sprint 4.4 — Modelo de Información

**Estado:** ✅ Completado

#### Objetivo

Definir el modelo conceptual de información del Atlas y las reglas mínimas para representar conocimiento estructurado, trazable, interoperable y gobernado.

#### Entregable

* [x] ADM-004 — Modelo de Información del Atlas.

#### Capacidades obtenidas

* [x] Tipos iniciales de entidades definidos.
* [x] Elementos transversales definidos.
* [x] Relaciones semánticas iniciales definidas.
* [x] Cardinalidades conceptuales iniciales establecidas.
* [x] Separación entre entidades, clasificaciones e información contextual.
* [x] Taxón modelado como entidad única diferenciada por nivel taxonómico.
* [x] Parte vegetal modelada como entidad genérica reutilizable.
* [x] Droga vegetal diferenciada de Taxón y Parte vegetal.
* [x] Preparado vegetal incorporado como elemento transversal con identidad cuando el contexto lo requiera.
* [x] Compuesto químico y Clase química definidos como entidades reutilizables.
* [x] Actividad biológica y Mecanismo de acción definidos como entidades.
* [x] Uso terapéutico y Condición de salud definidos como entidades reutilizables.
* [x] Evento adverso representado mediante relación contextual con Condición de salud.
* [x] Contraindicación y Precaución representadas como relaciones o afirmaciones contextuales.
* [x] Interacción definida como entidad contextual.
* [x] Estudio diferenciado de Publicación.
* [x] Revisión sistemática integrada mediante clasificación de Estudio.
* [x] Uso tradicional diferenciado de Uso terapéutico.
* [x] Organización, Farmacopea, Monografía y Disposición normativa definidas como entidades reutilizables.
* [x] Afirmación definida como entidad ligera de gobernanza.
* [x] Evidencia definida como relación transversal calificada y no como entidad.
* [x] Fuente definida como categoría abstracta transversal.
* [x] Procedencia definida como trazabilidad transversal.
* [x] Estado de gobernanza separado del estado científico.
* [x] Identificadores externos diferenciados de la identidad interna del Atlas.
* [x] Modelo conceptual mantenido independiente de su implementación física.

#### Resultado

El Atlas dispone de un Modelo de Información v1.0 suficientemente definido para iniciar posteriormente la materialización técnica del conocimiento sin anticipar una base de datos, ontología, API o tecnología de grafo concreta.

---

### Principio de diseño del Release v0.4

Cada documento introdujo una responsabilidad arquitectónica diferenciada:

```text
ADR-005
→ decisión del modelo híbrido

ADM-002
→ arquitectura del conocimiento

ADM-003
→ dominios del conocimiento

ADM-004
→ modelo conceptual de información
```

No se crearon catálogos, diccionarios o glosarios redundantes cuya responsabilidad pudiera integrarse en estos documentos.

### Resultado del Release

El Release v0.4 queda completado con una arquitectura de conocimiento gobernada que permite avanzar hacia la implementación progresiva del modelo sin depender de la estructura documental inicial ni de una tecnología específica.


## 9. Releases Estratégicos

Los Releases posteriores permanecerán en planificación estratégica hasta el inicio formal de su ejecución.

Solo se desarrollarán en detalle cuando el Release precedente permita conocer con suficiente precisión su alcance.

| Release | Propósito                             | Estado                 |
| ------- | ------------------------------------- | ---------------------- |
| v0.5    | Por definir                           | ⚪ Siguiente Release — pendiente de definición |
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
v0.3  Infraestructura Tecnológica     ✅ Completado
v0.4  Arquitectura del Conocimiento   ✅ Completado
v0.5  Siguiente Release               ⚪ Pendiente de definición
v0.6+ Evolución estratégica           ⚪ Pendiente
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
├── Sprint 3.5  Validación Automática                 ✅
├── Sprint 3.6  Plantillas y Flujo Editorial          ✅
└── Sprint 3.7  Validación Integral y Cierre          ✅

Release v0.4
├── Sprint 4.1  Modelo Híbrido del Conocimiento       ✅
├── Sprint 4.2  Arquitectura del Modelo               ✅
├── Sprint 4.3  Dominios de Conocimiento              ✅
└── Sprint 4.4  Modelo de Información                 ✅
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
v0.5 Pendiente de definición
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
* ADR-005 — Modelo Híbrido del Conocimiento.
* ADM-001 — Arquitectura General del Atlas.
* ADM-002 — Arquitectura del Modelo de Conocimiento.
* ADM-003 — Dominios de Conocimiento del Atlas.
* ADM-004 — Modelo de Información del Atlas.
* EEA-000 — Convenciones Generales.
* EEA-001 — Convenciones Documentales.
* EEA-002 — Convenciones de Nomenclatura.
* TPL-001 — Plantilla de Documento Base.

---
id: EEA-002
title: Convenciones de Nomenclatura
version: 1.2.0
status: Approved
type: EEA
created: 2026-07-25
updated: 2026-08-26
author: Proyecto Atlas de Fitoterapia
tags:
  - standards
  - naming
  - governance
---

# Convenciones de Nomenclatura

## 1. Propósito

Este estándar define las reglas de nomenclatura para todos los activos del Atlas de Fitoterapia.

Su finalidad es garantizar que documentos, directorios, recursos multimedia, conjuntos de datos, entidades de conocimiento y demás componentes puedan identificarse de forma consistente, inequívoca y compatible con herramientas de automatización, control de versiones, validación y publicación.

---

## 2. Alcance

Las disposiciones de este estándar aplican a todos los activos almacenados en los repositorios oficiales del Atlas, incluyendo documentos, entidades de conocimiento, imágenes, diagramas, archivos de datos, scripts, plantillas y cualquier otro recurso incorporado al proyecto.

---

## 3. Objetivos

Este estándar tiene como objetivos:

- Establecer reglas uniformes para la nomenclatura de todos los activos del Atlas.
- Garantizar la consistencia entre repositorios.
- Facilitar la automatización y validación de nombres e identificadores.
- Mantener compatibilidad con sistemas operativos y herramientas de desarrollo.
- Reducir ambigüedades durante la evolución del proyecto.
- Permitir reconocer visualmente el tipo de una entidad de conocimiento mediante su identificador.
- Mantener la separación entre identidad, clasificación, nomenclatura y representación documental.

---

## 4. Convenciones

### 4.1 Relación entre identidad y nomenclatura

El Atlas distingue explícitamente los siguientes conceptos:

| Elemento | Propósito | Puede modificarse |
| -------- | --------- | :---------------: |
| **Identificador (ID)** | Identidad permanente del activo u objeto gobernado. | No |
| **Nombre del archivo** | Organización física del repositorio. | Sí |
| **Título (`title`)** | Nombre lógico o editorial de una representación. | Sí |
| **Nombre científico o descriptivo** | Denominación del objeto representado. | Sí, cuando exista justificación |
| **Clasificación** | Posición o categoría asignada al objeto según el modelo correspondiente. | Sí, mediante gobernanza y trazabilidad |

El identificador constituye la identidad permanente del objeto gobernado conforme a ADR-002.

El nombre del archivo, título, nombre científico, nombre descriptivo y demás atributos podrán modificarse cuando exista una justificación científica, técnica, documental o editorial, sin alterar la identidad del objeto.

Un identificador asignado:

- no deberá reutilizarse;
- no deberá reasignarse a otro objeto;
- no deberá modificarse por cambios editoriales;
- deberá mantenerse cuando el objeto sea archivado, sustituido, reclasificado o declarado obsoleto.

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

Para identificadores institucionales y nombres normalizados se utilizarán únicamente:

- letras A-Z;
- números 0-9;
- guion medio (-).

No deberán utilizarse en identificadores:

- espacios;
- acentos;
- letra ñ;
- caracteres especiales;
- signos de puntuación.

Los contenidos científicos y editoriales no quedan sujetos a esta restricción cuando su correcta representación requiera caracteres propios del idioma, nomenclatura científica o fuente original.

---

### 4.4 Formato general de nombres de archivo institucionales

Cuando un documento institucional utilice su identificador como parte del nombre del archivo, seguirá el formato:

```text
IDENTIFICADOR-Nombre-Descriptivo.ext
```

Ejemplos:

```text
ADR-004-Modelo-Hibrido-del-Conocimiento.md
EEA-002-Convenciones-de-Nomenclatura.md
```

Las entidades de conocimiento no están obligadas a incorporar su identificador en el nombre físico del archivo.

La identidad de una entidad pertenece al objeto gobernado y no a la representación documental que la contiene.

Por ejemplo, una entidad puede tener:

```text
ID:
TAX-SP-000001
```

y representarse mediante:

```text
curcuma-longa.md
```

sin que el nombre del archivo forme parte de su identidad.

---

### 4.5 Uso de mayúsculas

Los identificadores conservarán siempre su formato institucional.

Las palabras descriptivas de documentos institucionales utilizarán **Mayúscula Inicial** cuando corresponda a la convención vigente.

Ejemplos:

```text
EEA-001-Convenciones-Documentales.md
ADR-003-Jerarquia-Normativa.md
```

Los nombres físicos utilizados por estructuras editoriales o técnicas podrán adoptar las convenciones requeridas por la implementación correspondiente.

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

La estructura institucional vigente incluye:

```text
00-Gobierno/
10-ADM/
20-ADR/
30-Plantillas/
30-RM/
40-EEA/
```

Estos nombres deberán conservarse mientras formen parte de la arquitectura física aprobada del repositorio.

La modificación, sustitución o incorporación de nuevos directorios institucionales deberá responder a una decisión arquitectónica, estándar o planificación aprobada.

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

Los directorios utilizados para organizar conocimiento científico deberán respetar los principios definidos por ADR-005, ADM-002, ADM-003 y ADM-004.

La estructura física de `atlas-knowledge` constituye una implementación del modelo y no define por sí misma la identidad, clasificación ni relaciones de las entidades.

En consecuencia:

- una carpeta no constituye una entidad;
- la ubicación física de un archivo no determina su identidad;
- una entidad podrá cambiar de ubicación sin cambiar de ID;
- una vista editorial no deberá confundirse con la entidad que representa;
- la estructura de navegación podrá evolucionar independientemente de la identidad de los objetos gobernados.

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

### 4.9 Identificadores de entidades de conocimiento

Las entidades de conocimiento definidas por el Modelo de Información del Atlas deberán utilizar identificadores permanentes que permitan reconocer visualmente el tipo general de objeto representado.

#### 4.9.1 Formato general

Salvo las especializaciones expresamente definidas en este estándar, los identificadores de entidades utilizarán:

```text
<PREFIJO>-<SECUENCIA>
```

donde:

- `PREFIJO` identifica el tipo de entidad;
- `SECUENCIA` es un número de seis dígitos;
- la secuencia comienza en `000001`;
- los ceros iniciales son obligatorios;
- cada tipo de entidad mantiene su propia secuencia;
- los identificadores se escriben en mayúsculas;
- los identificadores no contienen nombres descriptivos.

Ejemplo:

```text
PVE-000001
```

No será válido:

```text
PVE-Rizoma
PVE-1
pve-000001
PVE_000001
```

#### 4.9.2 Catálogo de prefijos de entidades

El Atlas reconoce inicialmente los siguientes tipos de entidad y prefijos oficiales:

| Entidad | `type` operativo | Prefijo | Ejemplo |
| --- | --- | --- | --- |
| Taxón | `taxon` | `TAX` | `TAX-SP-000001` |
| Parte vegetal | `plant_part` | `PVE` | `PVE-000001` |
| Droga vegetal | `herbal_drug` | `DVE` | `DVE-000001` |
| Preparado vegetal | `herbal_preparation` | `PRE` | `PRE-000001` |
| Compuesto químico | `chemical_compound` | `COM` | `COM-000001` |
| Clase química | `chemical_class` | `CLQ` | `CLQ-000001` |
| Actividad biológica | `biological_activity` | `ACB` | `ACB-000001` |
| Mecanismo de acción | `mechanism_of_action` | `MEC` | `MEC-000001` |
| Uso terapéutico | `therapeutic_use` | `UTE` | `UTE-000001` |
| Condición de salud | `health_condition` | `CSA` | `CSA-000001` |
| Interacción | `interaction` | `INT` | `INT-000001` |
| Estudio | `study` | `EST` | `EST-000001` |
| Publicación | `publication` | `PUB` | `PUB-000001` |
| Uso tradicional | `traditional_use` | `UTR` | `UTR-000001` |
| Comunidad o pueblo | `community` | `COMU` | `COMU-000001` |
| Sistema tradicional | `traditional_system` | `STR` | `STR-000001` |
| Región | `region` | `REG` | `REG-000001` |
| Organización | `organization` | `ORG` | `ORG-000001` |
| Farmacopea | `pharmacopoeia` | `FAR` | `FAR-000001` |
| Monografía | `monograph` | `MON` | `MON-000001` |
| Disposición normativa | `normative_provision` | `NOR` | `NOR-000001` |
| Afirmación | `assertion` | `AFI` | `AFI-000001` |

Este catálogo constituye la nomenclatura inicial de entidades derivada de ADM-004.

La incorporación de un nuevo tipo de entidad requerirá:

1. que el tipo sea compatible con el Modelo de Información vigente;
2. que se defina un prefijo inequívoco;
3. que se actualice este estándar;
4. que se actualicen los mecanismos de validación correspondientes.

No deberán generarse prefijos ad hoc fuera de este catálogo.

#### 4.9.3 Especialización de identificadores taxonómicos

Los taxones incorporarán su rango taxonómico dentro del identificador para facilitar su reconocimiento visual.

El formato será:

```text
TAX-<RANGO>-<SECUENCIA>
```

Los rangos inicialmente soportados son:

| Nivel taxonómico | Código | Ejemplo |
| --- | --- | --- |
| Familia | `FAM` | `TAX-FAM-000001` |
| Género | `GEN` | `TAX-GEN-000001` |
| Especie | `SP` | `TAX-SP-000001` |
| Subespecie | `SSP` | `TAX-SSP-000001` |
| Variedad | `VAR` | `TAX-VAR-000001` |
| Forma | `FOR` | `TAX-FOR-000001` |

Cada rango taxonómico mantendrá su propia secuencia.

Ejemplo inicial:

```text
TAX-FAM-000001 → Zingiberaceae
TAX-GEN-000001 → Curcuma
TAX-SP-000001  → Curcuma longa L.
```

El segmento de rango deberá corresponder al nivel taxonómico registrado en el momento de creación de la entidad.

Conforme al principio de permanencia establecido por ADR-002, una reclasificación taxonómica posterior no autoriza modificar ni reutilizar el identificador ya asignado.

La reclasificación deberá conservarse mediante los mecanismos de trazabilidad, estado y procedencia definidos por el modelo de información.

#### 4.9.4 Secuencias

Las secuencias:

- serán numéricas;
- tendrán seis posiciones;
- comenzarán en `000001`;
- serán únicas dentro de su prefijo o especialización;
- nunca deberán reiniciarse para reutilizar identificadores eliminados;
- nunca deberán asignarse nuevamente a otra entidad.

Ejemplos:

```text
COM-000001
COM-000002
COM-000003
```

Si `COM-000002` deja de utilizarse, el siguiente identificador continúa siendo:

```text
COM-000004
```

y no:

```text
COM-000002
```

#### 4.9.5 Identificadores externos

Los identificadores provenientes de sistemas externos no constituyen IDs del Atlas.

Ejemplos de sistemas externos incluyen:

```text
IPNI
POWO
DOI
PMID
CAS
PubChem
```

Estos identificadores deberán conservarse como información asociada a la entidad correspondiente.

Ejemplo conceptual:

```yaml
id: TAX-SP-000001

external_ids:
  - system: POWO
    value: "..."
  - system: IPNI
    value: "..."
```

No será válido utilizar directamente un identificador externo como identidad primaria de una entidad del Atlas.

#### 4.9.6 Identidad frente a representación

La existencia de un ID no implica que cada entidad deba corresponder a un archivo independiente.

Un objeto gobernado podrá:

- representarse en uno o varios documentos;
- formar parte de una vista editorial;
- participar en múltiples relaciones;
- cambiar de archivo o ubicación;
- ser utilizado por procesos automáticos.

En todos los casos conservará el mismo identificador Atlas.

#### 4.9.7 Asignación

Todo objeto que requiera identidad propia conforme a ADM-004 deberá recibir su identificador antes de incorporarse como entidad gobernada.

La asignación deberá comprobar, como mínimo:

- que el prefijo corresponda al tipo;
- que la secuencia no haya sido utilizada;
- que el identificador no exista previamente;
- que el objeto no haya sido registrado anteriormente bajo otro ID;
- que el formato corresponda a este estándar.

La automatización podrá asistir en la asignación de identificadores, pero no deberá generar identidades duplicadas ni reutilizar secuencias existentes.

---

## 5. Validación

Antes de incorporar un activo al repositorio oficial deberán realizarse las siguientes verificaciones.

| Validación | Automática | Manual |
| ---------- | :--------: | :----: |
| Identificador válido | ✓ | |
| Identificador único | ✓ | |
| Correspondencia entre prefijo y tipo de entidad | ✓ | |
| Correspondencia inicial entre rango e ID taxonómico | ✓ | |
| Formato del nombre | ✓ | |
| Caracteres permitidos | ✓ | |
| Uso correcto de acrónimos | ✓ | |
| Compatibilidad con sistemas de archivos | ✓ | |
| Singular / plural | ✓ | |
| Correspondencia con el contenido | | ✓ |
| Consistencia con documentos relacionados | | ✓ |
| Ausencia de duplicidad conceptual de la entidad | | ✓ |

Los validadores automáticos deberán implementar este estándar sin convertirse en la fuente normativa de la nomenclatura.

La fuente normativa de los prefijos, formatos y reglas de identificación de entidades es este documento.

Los activos que incumplan estas reglas no deberán incorporarse al repositorio oficial hasta que la inconsistencia haya sido resuelta mediante el proceso de gobernanza correspondiente.

---

## 6. Compatibilidad futura

Las reglas de nomenclatura deberán mantenerse estables aun cuando el Atlas incorpore nuevas herramientas, repositorios, mecanismos de publicación, motores de almacenamiento, grafos de conocimiento o tecnologías de automatización.

El diseño de los identificadores no deberá depender de:

- una base de datos específica;
- una ruta física;
- Obsidian;
- Quartz;
- GitHub;
- un formato documental concreto;
- una tecnología de grafos determinada.

La ampliación del catálogo de entidades o prefijos deberá realizarse mediante el proceso de gobernanza establecido por el Atlas.

---

## 7. Referencias

- GOV-001 — Constitución del Atlas de Fitoterapia.
- ADR-002 — Sistema de Identificación Única.
- ADR-003 — Jerarquía Normativa.
- ADR-005 — Modelo Híbrido del Conocimiento.
- ADM-001 — Arquitectura General del Atlas de Fitoterapia.
- ADM-002 — Arquitectura del Modelo de Conocimiento.
- ADM-003 — Dominios de Conocimiento del Atlas.
- ADM-004 — Modelo de Información del Atlas.
- EEA-000 — Convenciones Generales.
- EEA-001 — Convenciones Documentales.
- ISO 8601 — Date and Time Format.
- Semantic Versioning Specification 2.0.0.

# AGENTS.md

## Propósito

Este archivo es el punto de entrada operativo para Codex y otros agentes que trabajen en el Atlas de Fitoterapia.

Las fuentes normativas son los documentos aprobados de gobierno, arquitectura y estándares:

- `00-Gobierno/` — GOV;
- `20-ADR/` — decisiones arquitectónicas;
- `10-ADM/` — modelos de arquitectura e información;
- `40-EEA/` — estándares de aplicación.

Los agentes deberán consultar los documentos aplicables y respetar la jerarquía definida por GOV-001 y ADR-003. Este archivo resume obligaciones operativas; no sustituye ni modifica las fuentes normativas.

## Responsabilidades de los repositorios

`atlas-core` contiene gobierno, arquitectura, estándares, schemas, validadores y herramientas compartidas. Sus schemas son la fuente técnica para los tipos y relaciones actualmente implementados.

`atlas-knowledge` contiene las entidades de conocimiento, sus relaciones, procedencia y representaciones editoriales en Markdown. La ubicación o el nombre de un archivo no determina la identidad de una entidad, conforme a ADR-002, ADR-005 y ADM-004.

Obsidian es la interfaz humana para revisar, navegar y explorar el conocimiento. Quartz es la capa de publicación y visualización. Ninguna de estas herramientas constituye la fuente de verdad de la identidad o del grafo semántico.

## Incorporación de conocimiento

Antes de crear una entidad, el agente deberá:

1. buscar entidades existentes que representen el mismo concepto;
2. reconciliar nombres, identificadores externos y alcance semántico;
3. reutilizar el ID existente cuando corresponda;
4. crear una entidad sólo cuando tenga identidad propia conforme a ADM-004;
5. asignar el ID según EEA-002, sin reutilizar secuencias.

Sólo podrán utilizarse tipos definidos en:

```text
tools/schemas/entities.yaml
```

Sólo podrán utilizarse relaciones definidas y compatibles según:

```text
tools/schemas/relationships.yaml
```

Todo conocimiento generado automáticamente deberá iniciar como:

```yaml
governance_status: proposed
```

Los agentes no deberán aprobar automáticamente el conocimiento que generen.

## Evidencia, procedencia y límites

Toda información científica deberá conservar procedencia verificable cuando corresponda: fuente, DOI, PMID, otros identificadores, URL, versión o edición, fecha de consulta y contexto relevante. No deberán inventarse datos ausentes ni presentarse una fuente como prueba más fuerte de lo que permite su diseño.

Las limitaciones, incertidumbres y contradicciones entre fuentes deberán conservarse de forma trazable, conforme a ADR-005 y ADM-004. No deberán eliminarse ni resolverse mediante inferencias automáticas.

No deberán propagarse propiedades sin evidencia entre niveles u objetos relacionados. En particular:

```text
propiedad del taxón ≠ propiedad de toda parte o preparado
compuesto en una droga ≠ compuesto en todo el taxón
actividad de un preparado ≠ actividad de toda la especie
resultado in vitro ≠ eficacia clínica
uso tradicional ≠ uso terapéutico validado
```

## Relaciones estructuradas y navegación

Las relaciones del Front Matter forman el grafo semántico gobernado y son utilizadas por validadores y agentes. Los wikilinks forman la navegación humana para Obsidian y Quartz.

Ambas representaciones deberán ser coherentes, pero el cuerpo editorial no deberá repetir mecánicamente cada relación estructurada. Las relaciones nuevas deberán usar únicamente tipos y pares autorizados por `tools/schemas/relationships.yaml`, y todos sus targets deberán existir.

## Calidad editorial de las entidades

### Front Matter y cuerpo Markdown

El Front Matter está orientado a máquinas e incluye `id`, `type`, `governance_status`, `relationships`, `external_ids`, `provenance` y demás propiedades estructuradas.

El cuerpo Markdown está orientado a personas. Deberá definir, describir, contextualizar, resumir evidencia, explicar relaciones relevantes, exponer procedencia útil o facilitar navegación. No deberá convertir automáticamente cada campo del Front Matter en una sección visible.

### Secciones vacías y placeholders

No deberán generarse encabezados cuyo único contenido sea “Pendiente de incorporación”, “Pendiente de validación”, “Sin información”, “No disponible” o expresiones equivalentes.

Cuando el schema requiera listas vacías como:

```yaml
external_ids: []
provenance: []
```

éstas permanecerán en el Front Matter, pero no generarán secciones editoriales vacías. La ausencia de información sólo deberá explicarse en el cuerpo cuando sea científicamente relevante.

### Identidad y redacción

La sección de identidad deberá explicar qué es la entidad de forma comprensible e independiente de la fuente que motivó inicialmente su creación. No deberá describir el proceso de generación del archivo.

Cada párrafo visible deberá aportar información útil. Deberá eliminarse el texto creado únicamente para llenar una plantilla o repetir metadatos sin contexto.

No deberán utilizarse referencias ambiguas como “la publicación indica”, “el estudio demuestra”, “la fuente menciona” o “la evidencia señala” sin identificar explícitamente la fuente mediante autor y año, entidad o enlace.

### Procedencia editorial

Cuando `provenance` contenga información útil, el cuerpo deberá exponerla de manera legible cuando sea pertinente para comprender la entidad. Si existe una entidad `publication`, se preferirá un wikilink hacia ella y se evitará repetir innecesariamente la referencia bibliográfica completa.

## Cambios normativos

Las tareas científicas ordinarias no deberán modificar GOV, ADR, ADM ni EEA. Si el conocimiento revela una necesidad normativa o de modelo, el agente deberá documentarla para decisión humana sin cambiar automáticamente esos documentos.

## Validación y responsabilidad

Antes de terminar cambios en `atlas-knowledge`, el agente deberá ejecutar desde ese repositorio:

```powershell
py ..\atlas-core\tools\validate_entities.py .
```

Además deberá comprobar:

- IDs válidos y no duplicados;
- tipos y relaciones reconocidos;
- compatibilidad entre origen y destino;
- existencia de todos los targets;
- coherencia de wikilinks relevantes;
- ausencia de nodos aislados accidentales;
- procedencia y límites de interpretación;
- calidad editorial conforme a este archivo.

El agente deberá corregir los errores provocados por sus propios cambios. No deberá debilitar schemas, validadores o normas para conseguir una validación satisfactoria.

## Entrega

Los cambios deberán quedar revisables. El agente informará archivos modificados, entidades y relaciones afectadas, fuentes incorporadas, validaciones ejecutadas, limitaciones detectadas y decisiones pendientes de aprobación humana.

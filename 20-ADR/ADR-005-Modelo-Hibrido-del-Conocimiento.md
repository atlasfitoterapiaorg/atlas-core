---
id: ADR-005
title: Modelo Híbrido del Conocimiento
version: 1.0.0
status: Approved
type: ADR
created: 2026-08-16
updated: 2026-08-16
author: Proyecto Atlas de Fitoterapia
tags:
  - architecture
  - knowledge
  - knowledge-graph
  - provenance
  - evidence
---

# Modelo Híbrido del Conocimiento

## 1. Contexto

El Atlas de Fitoterapia se concibe como una plataforma de conocimiento científico capaz de integrar información procedente de múltiples dominios y fuentes, incluyendo entidades biológicas, compuestos químicos, preparados, enfermedades, evidencia científica, farmacopeas, bases de datos externas y recursos documentales.

Durante las primeras etapas del proyecto se estableció una infraestructura documental basada en archivos Markdown y una plataforma de publicación mediante Quartz. Esta infraestructura permite crear, mantener, versionar y publicar contenido, pero no constituye por sí misma un modelo formal del conocimiento.

Conforme el Atlas crezca será necesario representar conocimiento que no puede expresarse adecuadamente únicamente como documentos independientes.

Una especie vegetal puede contener múltiples compuestos químicos, participar en diferentes preparados, relacionarse con usos tradicionales, indicaciones terapéuticas, actividades biológicas, riesgos, contraindicaciones y evidencia científica.

Asimismo, una misma afirmación puede encontrarse respaldada por diferentes fuentes y una misma fuente puede proporcionar información sobre numerosas entidades y relaciones.

El Atlas también deberá poder incorporar información procedente de fuentes externas, como bases de datos científicas, publicaciones, farmacopeas y repositorios especializados, preservando en todo momento la trazabilidad de su procedencia.

Por estas razones es necesario definir un modelo que permita representar simultáneamente conocimiento estructurado, evidencia, procedencia y contenido editorial.

---

## 2. Problema

Utilizar exclusivamente documentos como unidad de conocimiento provocaría que la información quedara distribuida y repetida entre múltiples archivos.

Por ejemplo, una relación entre una especie vegetal y un compuesto químico podría aparecer simultáneamente en:

- La monografía de la especie.
- La ficha del compuesto.
- Una publicación científica.
- Una farmacopea.
- Una base de datos externa.
- Una revisión editorial.

Si cada documento mantuviera de forma independiente la misma información, podrían producirse:

- Duplicación de conocimiento.
- Inconsistencias entre documentos.
- Pérdida de trazabilidad.
- Dificultad para identificar la fuente original de una afirmación.
- Dificultad para automatizar relaciones.
- Imposibilidad de determinar cuándo varias fuentes respaldan la misma afirmación.
- Dependencia excesiva de la estructura física de archivos.
- Dificultad para construir grafos de conocimiento.
- Dificultad para integrar agentes de inteligencia artificial o procesos automáticos.

En el extremo contrario, utilizar exclusivamente estructuras de datos eliminaría parte del contexto narrativo necesario para comunicar adecuadamente conocimiento científico complejo.

El Atlas necesita, por tanto, separar el conocimiento estructurado de su representación editorial sin perder la relación entre ambos.

---

## 3. Decisión

El Atlas de Fitoterapia adoptará un **Modelo Híbrido del Conocimiento**.

El modelo distinguirá conceptualmente cinco componentes fundamentales:

```text
Entidades
   │
   ▼
Relaciones
   │
   ▼
Afirmaciones / Evidencia
   │
   ▼
Procedencia
   │
   ▼
Vistas Editoriales
```

Estos componentes podrán interactuar entre sí para formar el conocimiento gobernado por el Atlas.

### 3.1 Entidades

Las entidades representan objetos identificables dentro del dominio de conocimiento del Atlas.

Podrán representar, entre otros conceptos:

- Especies vegetales.
- Compuestos químicos.
- Preparados.
- Enfermedades.
- Actividades biológicas.
- Recursos documentales.
- Fuentes científicas.
- Otros objetos que posteriormente sean reconocidos por el modelo de información.

Toda entidad gobernada deberá respetar el Sistema de Identificación Única establecido por ADR-002.

La identidad de una entidad será independiente de:

- Su nombre.
- Su ubicación física.
- El archivo donde sea descrita.
- La interfaz donde sea presentada.
- La fuente externa que también pueda identificarla.

### 3.2 Relaciones

Las relaciones expresan vínculos semánticos entre entidades y permiten representar explícitamente cómo se conectan los diferentes objetos de conocimiento del Atlas.

Conceptualmente podrán existir relaciones como:

```text
Especie ── contiene ──► Compuesto

Preparado ── utiliza ──► Especie

Compuesto ── presenta actividad ──► Actividad biológica

Especie ── documentada en ──► Farmacopea
```

Las relaciones formarán progresivamente el grafo de conocimiento del Atlas.

Una relación será conceptualmente independiente de cualquier documento editorial en el que pueda ser presentada.

Por tanto:

- Una relación podrá existir aunque todavía no exista una monografía.
- Una relación podrá aparecer en múltiples vistas editoriales.
- Una misma pareja de entidades podrá mantener diferentes tipos de relación.
- Las relaciones podrán estar respaldadas por una o varias afirmaciones.
- Las relaciones deberán preservar trazabilidad hacia la evidencia que las sustenta.

La definición formal de los tipos de relación, sus restricciones y cardinalidades será responsabilidad de documentos arquitectónicos posteriores.

### 3.3 Afirmaciones y evidencia

El Atlas distinguirá entre una relación conceptual y las afirmaciones que sostienen, describen, cuantifican o cuestionan dicha relación.

Una **afirmación** representa una declaración trazable acerca de:

- Una entidad.
- Un atributo.
- Una relación.
- Un valor.
- Una actividad.
- Un efecto.
- Una asociación.
- Una observación científica.

Por ejemplo:

```text
Tagetes erecta
       │
       └── contiene ──► Compuesto X
                           │
                           ├── Afirmación A
                           ├── Afirmación B
                           └── Afirmación C
```

Cada afirmación podrá contar con evidencia propia y procedencia independiente.

Una afirmación no será equivalente automáticamente a una verdad científica definitiva.

El Atlas deberá ser capaz de conservar afirmaciones provenientes de diferentes fuentes incluso cuando:

- Coincidan.
- Se complementen.
- Presenten valores diferentes.
- Utilicen metodologías distintas.
- Se contradigan.

La arquitectura deberá permitir posteriormente establecer estados editoriales o científicos para las afirmaciones.

Conceptualmente podrán existir estados como:

- Importado.
- Pendiente de revisión.
- Verificado.
- Corroborado.
- Contradicho.
- Rechazado.
- Obsoleto.

Estos estados son ilustrativos y no constituyen todavía una especificación formal.

Su definición corresponderá al modelo de información y a los estándares editoriales posteriores.

### 3.4 Procedencia

Toda información incorporada al Atlas deberá poder conservar información suficiente para determinar su procedencia cuando ésta resulte relevante para su trazabilidad.

La procedencia permitirá conocer, según corresponda:

- Fuente de origen.
- Base de datos de origen.
- Publicación original.
- Referencia bibliográfica.
- Identificador externo.
- Fecha de consulta.
- Fecha de incorporación.
- Método de obtención.
- Versión de la fuente.
- Transformaciones realizadas.
- Proceso de importación.
- Relación entre el registro externo y la entidad gobernada por el Atlas.

La procedencia constituye una propiedad fundamental del conocimiento científico administrado por el Atlas.

Un dato externo no deberá convertirse en información anónima después de incorporarse al sistema.

Conceptualmente:

```text
Entidad
   │
   ▼
Relación o atributo
   │
   ▼
Afirmación
   │
   ▼
Procedencia
   │
   ▼
Fuente
   │
   ▼
Referencia original
```

Por ejemplo:

```text
Especie
   │
   └── contiene ──► Compuesto
                         │
                         ▼
                    Afirmación
                         │
                         ▼
                 Base de datos externa
                         │
                         ▼
                 Referencia original
```

Una fuente externa no sustituirá la identidad interna de una entidad gobernada por el Atlas.

### 3.5 Identificadores externos

Las entidades del Atlas podrán mantener correspondencias con identificadores pertenecientes a sistemas externos.

Conceptualmente:

```text
Entidad Atlas
     │
     ├── Identificador Atlas
     ├── Identificador externo A
     ├── Identificador externo B
     └── Identificador externo C
```

Estos identificadores podrán provenir de:

- Bases taxonómicas.
- Bases fitoquímicas.
- Bases químicas.
- Repositorios bibliográficos.
- Farmacopeas.
- Repositorios institucionales.
- Otros sistemas científicos.

Los identificadores externos tendrán como propósito facilitar:

- Interoperabilidad.
- Reconciliación de entidades.
- Detección de duplicados.
- Importación.
- Actualización.
- Referenciación cruzada.
- Trazabilidad.

Ningún identificador externo sustituirá al identificador oficial asignado por el Sistema de Identificación Única del Atlas.

La entidad continuará siendo gobernada internamente por su identificador Atlas.

### 3.6 Fuentes externas

El Atlas podrá incorporar conocimiento procedente de múltiples fuentes externas.

Entre ellas podrán encontrarse:

- Bases de datos científicas.
- Bases fitoquímicas.
- Repositorios taxonómicos.
- Repositorios químicos.
- Publicaciones científicas.
- Revisiones sistemáticas.
- Metaanálisis.
- Farmacopeas.
- Catálogos institucionales.
- Conjuntos de datos científicos.

Ejemplos de fuentes potenciales incluyen:

- Dr. Duke's Phytochemical and Ethnobotanical Databases.
- PubMed.
- Cochrane.
- IPNI.
- Plants of the World Online.
- Repositorios químicos especializados.
- Farmacopeas oficiales.

La inclusión de una fuente en esta lista no implica su aprobación automática como evidencia científica suficiente para cualquier afirmación.

Cada fuente deberá evaluarse conforme a las reglas de evidencia y gobernanza que se definan posteriormente.

Los datos provenientes de fuentes externas deberán incorporarse preservando su procedencia.

### 3.7 Multiplicidad de evidencia

Una misma relación podrá estar respaldada por múltiples afirmaciones procedentes de diferentes fuentes.

Por ejemplo:

```text
Curcuma longa
      │
      └── contiene ──► Curcumina
                           │
             ┌─────────────┼─────────────┐
             │             │             │
             ▼             ▼             ▼
        Fuente A       Fuente B      Fuente C
```

El Atlas no deberá duplicar innecesariamente la entidad o la relación únicamente porque existan diferentes fuentes.

En su lugar, deberá conservar la diversidad de evidencias asociadas.

Esto permitirá posteriormente:

- Evaluar convergencia de evidencia.
- Identificar contradicciones.
- Determinar fuentes independientes.
- Establecer niveles de confianza.
- Evaluar calidad metodológica.
- Detectar información desactualizada.

La forma exacta de representar estas propiedades será definida posteriormente.

### 3.8 Evidencia contradictoria

El Atlas no deberá eliminar automáticamente información únicamente porque contradiga otra fuente previamente registrada.

Cuando existan afirmaciones incompatibles, deberán conservarse de manera trazable hasta que los procesos editoriales o científicos correspondientes determinen su interpretación.

Conceptualmente:

```text
                   Relación
                      │
          ┌───────────┴───────────┐
          │                       │
          ▼                       ▼
   Afirmación A              Afirmación B
     confirma                  contradice
          │                       │
          ▼                       ▼
      Fuente A                 Fuente B
```

Este principio permitirá preservar la historia y evolución del conocimiento científico.

La contradicción entre fuentes constituye información relevante y no deberá resolverse mediante la eliminación silenciosa de registros.

### 3.9 Vistas editoriales

Los documentos, monografías y páginas publicadas constituirán **vistas editoriales del conocimiento**.

Una vista editorial podrá integrar información procedente de múltiples:

- Entidades.
- Relaciones.
- Afirmaciones.
- Evidencias.
- Fuentes.

Por ejemplo:

```text
Entidades
   │
   ├── Especie
   ├── Compuestos
   ├── Preparados
   ├── Actividades
   └── Evidencia
          │
          ▼
      Relaciones
          │
          ▼
      Monografía
```

La monografía no constituirá la identidad de una especie.

Tampoco será necesariamente la única ubicación donde exista información sobre ella.

Será una representación editorial destinada a comunicar de manera estructurada y comprensible el conocimiento gobernado por el Atlas.

Una misma entidad podrá participar en múltiples vistas editoriales.

Una misma vista editorial podrá utilizar múltiples entidades.

### 3.10 Separación entre conocimiento y representación

El Modelo Híbrido del Conocimiento mantiene el principio establecido por ADR-002 de separación entre identidad y representación.

La arquitectura conceptual será:

```text
Objeto gobernado
      │
      ▼
   Identidad
      │
      ▼
   Entidad
      │
      ├── atributos
      ├── relaciones
      ├── afirmaciones
      └── procedencia
               │
               ▼
       Vistas editoriales
               │
               ▼
          Publicación
```

En consecuencia:

- La entidad no será equivalente al archivo.
- La monografía no será equivalente a la entidad.
- Una relación no dependerá de un documento específico.
- Una fuente externa no sustituirá al objeto gobernado.
- Un identificador externo no sustituirá al identificador oficial del Atlas.
- Una representación editorial podrá cambiar sin modificar la identidad del objeto.

---

## 4. Grafo de conocimiento

Las entidades y relaciones del Atlas constituirán progresivamente un grafo de conocimiento.

Conceptualmente:

```text
                         Especie
                  ┌────────┼────────┐
                  │        │        │
                  ▼        ▼        ▼
              Compuesto Preparado  Uso
                  │        │        │
                  ▼        ▼        ▼
              Actividad Evidencia Enfermedad
                  │        │        │
                  └────────┼────────┘
                           ▼
                       Referencias
```

Las afirmaciones y su procedencia proporcionarán el contexto necesario para evaluar y rastrear las relaciones representadas en dicho grafo.

El grafo permitirá progresivamente representar conexiones entre dominios que no serían evidentes mediante una estructura exclusivamente documental.

El grafo conceptual no obliga al Atlas a adoptar en este momento una tecnología específica de base de datos o almacenamiento.

La representación física del grafo será una decisión posterior.

---

## 5. Flujo conceptual del conocimiento

La incorporación de información al Atlas deberá preservar conceptualmente la siguiente cadena:

```text
Fuente
   │
   ▼
Dato u observación
   │
   ▼
Afirmación
   │
   ▼
Entidad / Relación
   │
   ▼
Conocimiento gobernado
   │
   ▼
Vista editorial
   │
   ▼
Publicación
```

Este flujo permitirá diferenciar entre:

- El dato recibido.
- La fuente que lo proporciona.
- La afirmación que representa.
- La estructura de conocimiento a la que se incorpora.
- La forma en que posteriormente se comunica al usuario.

Esta separación será fundamental para permitir procesos futuros de automatización y revisión humana.

---

## 6. Justificación

El Modelo Híbrido del Conocimiento permite combinar las ventajas de diferentes enfoques complementarios.

El conocimiento estructurado proporciona:

- Identidad estable.
- Relaciones explícitas.
- Trazabilidad.
- Capacidad de consulta.
- Automatización.
- Interoperabilidad.
- Construcción de grafos.
- Reutilización de información.
- Reconciliación de entidades.

Las afirmaciones y la procedencia proporcionan:

- Evidencia verificable.
- Historial de origen.
- Capacidad para comparar fuentes.
- Representación de contradicciones.
- Evaluación posterior de confianza.
- Transparencia científica.

Las vistas editoriales proporcionan:

- Contexto científico.
- Explicaciones.
- Narrativa.
- Síntesis.
- Interpretación.
- Presentación comprensible para usuarios humanos.

La combinación de estos enfoques evita que el Atlas dependa exclusivamente de una colección de documentos o de una estructura de datos aislada.

Asimismo, proporciona una base adecuada para futuras automatizaciones, integraciones y agentes de inteligencia artificial sin sacrificar trazabilidad ni gobernanza.

---

## 7. Consecuencias

Como resultado de esta decisión:

- El conocimiento del Atlas no estará definido exclusivamente por archivos Markdown.
- Las entidades constituirán objetos gobernados independientes de sus representaciones documentales.
- Las relaciones entre entidades podrán existir independientemente de una monografía.
- Las afirmaciones deberán poder vincularse con evidencia y procedencia.
- Las fuentes externas deberán conservar su identidad y trazabilidad.
- Los identificadores externos podrán coexistir con el Sistema de Identificación Única del Atlas.
- Una entidad podrá aparecer en múltiples vistas editoriales.
- Una vista editorial podrá utilizar múltiples entidades.
- Una misma relación podrá estar respaldada por múltiples fuentes.
- Una misma fuente podrá respaldar múltiples afirmaciones.
- El modelo deberá permitir representar evidencia contradictoria sin destruir la información original.
- La incorporación de información externa no implicará su aceptación automática como verdad científica.
- El Atlas podrá evolucionar hacia un grafo de conocimiento sin reemplazar necesariamente su infraestructura editorial.
- Las futuras automatizaciones deberán operar respetando identidad, relaciones, evidencia y procedencia.
- Los agentes automáticos no podrán eliminar la trazabilidad de la información incorporada.
- Los documentos continuarán siendo relevantes como mecanismos editoriales, aunque dejarán de ser la única estructura del conocimiento.

---

## 8. Impacto

### Gobernanza

- Sistema de Identificación Única.
- Trazabilidad.
- Reglas de incorporación de conocimiento.
- Gobierno de fuentes externas.
- Procesos de revisión.
- Control de procedencia.

### Arquitectura

- Modelo de conocimiento.
- Modelo de información.
- Dominios de conocimiento.
- Grafo de conocimiento.
- Interoperabilidad.

### Conocimiento

- Entidades.
- Relaciones.
- Afirmaciones.
- Evidencia.
- Procedencia.
- Monografías.
- Referencias.

### Integraciones

- Bases de datos externas.
- Repositorios científicos.
- Farmacopeas.
- Sistemas taxonómicos.
- Identificadores externos.
- Conjuntos de datos.

### Automatización

- Importación de conocimiento.
- Reconciliación de entidades.
- Detección de duplicados.
- Validaciones.
- Evaluación de procedencia.
- Agentes de inteligencia artificial.
- Actualización asistida del conocimiento.

### Publicación

- Generación de monografías.
- Navegación entre entidades.
- Visualización de relaciones.
- Trazabilidad hacia fuentes.
- Presentación de evidencia.

---

## 9. Principios derivados

La adopción del Modelo Híbrido del Conocimiento establece los siguientes principios arquitectónicos:

### 9.1 La identidad pertenece al objeto

La identidad de un objeto gobernado no dependerá del archivo, título, nombre o sistema externo utilizado para representarlo.

### 9.2 El conocimiento debe ser trazable

Siempre que sea aplicable deberá ser posible determinar de dónde proviene una afirmación.

### 9.3 Las fuentes no son equivalentes a la verdad

La existencia de información en una fuente externa no implica automáticamente su aceptación científica por el Atlas.

### 9.4 Las contradicciones deben preservarse

La evidencia contradictoria deberá mantenerse de forma trazable mientras exista relevancia científica o histórica.

### 9.5 Las vistas editoriales no constituyen la fuente de identidad

Las monografías y documentos serán representaciones del conocimiento, no sustitutos de las entidades que describen.

### 9.6 La interoperabilidad no sustituye la gobernanza

Los identificadores externos facilitarán la integración, pero la identidad oficial del objeto continuará siendo administrada por el Atlas.

### 9.7 La automatización deberá preservar procedencia

Ningún proceso automático deberá incorporar conocimiento eliminando su fuente, contexto o trazabilidad.

---

## 10. Implementación

Este ADR establece exclusivamente la decisión arquitectónica de adoptar un Modelo Híbrido del Conocimiento.

No define todavía:

- Esquemas de datos.
- Formatos físicos de almacenamiento.
- Sintaxis de entidades.
- Sintaxis de relaciones.
- Sintaxis de afirmaciones.
- Sintaxis de procedencia.
- Cardinalidades.
- Catálogos de atributos.
- Ontologías específicas.
- Tecnologías de base de datos.
- Motores de grafos.
- APIs.
- Algoritmos de reconciliación.
- Mecanismos automáticos de importación.
- Métodos de puntuación de evidencia.
- Reglas de confianza científica.

Estos elementos serán definidos posteriormente mediante los documentos arquitectónicos y estándares correspondientes.

La evolución prevista es:

```text
ADR-005
Modelo Híbrido del Conocimiento
        │
        ▼
ADM-002
Arquitectura del Modelo de Conocimiento
        │
        ▼
ADM-003
Dominios de Conocimiento del Atlas
        │
        ▼
ADM-004
Modelo de Información del Atlas
        │
        ▼
Estándares
        │
        ▼
Implementación
```

La implementación deberá respetar en todo momento los principios establecidos en ADR-002, ADR-003 y ADR-004.

---

## 11. Criterios arquitectónicos derivados

Los documentos posteriores deberán ser capaces de resolver, como mínimo:

- Cómo se define formalmente una entidad.
- Cómo se define una relación.
- Cómo se representa una afirmación.
- Cómo se vincula una afirmación con su evidencia.
- Cómo se representa la procedencia.
- Cómo se mantienen identificadores externos.
- Cómo se reconcilian registros externos con entidades existentes.
- Cómo se representa evidencia contradictoria.
- Cómo se evita la duplicación de conocimiento.
- Cómo se construyen vistas editoriales a partir del conocimiento estructurado.
- Cómo se preserva la trazabilidad durante procesos automatizados.

Estos puntos no constituyen todavía especificaciones técnicas; representan requisitos arquitectónicos que deberán ser resueltos en los ADM correspondientes.

---

## 12. Referencias

- GOV-001 — Constitución del Atlas de Fitoterapia.
- ADM-001 — Arquitectura General del Atlas de Fitoterapia.
- ADR-002 — Sistema de Identificación Única.
- ADR-003 — Jerarquía Normativa.
- ADR-004 — Arquitectura antes que Implementación.
- W3C Resource Description Framework (RDF).
- W3C PROV — Provenance Data Model.
- FAIR Guiding Principles for Scientific Data Management and Stewardship.

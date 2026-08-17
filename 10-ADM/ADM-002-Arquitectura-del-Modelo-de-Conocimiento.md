---
id: ADM-002
title: Arquitectura del Modelo de Conocimiento
version: 1.0.0
status: Approved
type: ADM
created: 2026-08-16
updated: 2026-08-16
author: Proyecto Atlas de Fitoterapia
tags:
  - architecture
  - knowledge
  - knowledge-graph
  - evidence
  - provenance
---

# Arquitectura del Modelo de Conocimiento

## 1. Propósito

Definir la arquitectura conceptual mediante la cual el Atlas de Fitoterapia organizará, relacionará, validará y representará su conocimiento científico.

Este documento desarrolla arquitectónicamente el Modelo Híbrido del Conocimiento establecido por ADR-005 y determina las capas, responsabilidades y relaciones fundamentales que deberán observar los modelos de información, estándares, herramientas y procesos que se definan posteriormente.

ADM-002 no establece todavía los atributos concretos de las entidades, las cardinalidades de las relaciones ni los esquemas físicos de almacenamiento.

Su propósito es definir **cómo se organiza arquitectónicamente el conocimiento del Atlas**.

---

## 2. Alcance

La arquitectura del modelo de conocimiento comprende:

- La organización del conocimiento mediante dominios y subdominios.
- La representación de objetos mediante entidades.
- La conexión semántica mediante relaciones.
- La representación de afirmaciones y evidencia.
- La preservación de la procedencia.
- La integración conceptual del conocimiento mediante un grafo.
- La separación entre conocimiento estructurado y vistas editoriales.
- La incorporación de información procedente de fuentes externas.
- La separación entre identidad, representación y publicación.
- Los principios arquitectónicos necesarios para permitir automatización futura.

Quedan fuera del alcance de este documento:

- La enumeración definitiva de los dominios de conocimiento.
- El catálogo formal de entidades.
- El catálogo formal de atributos.
- Las cardinalidades.
- Los esquemas de datos.
- Las ontologías específicas.
- Los formatos físicos de almacenamiento.
- Las tecnologías de bases de datos.
- Los motores de grafos.
- Las APIs.
- Los algoritmos de reconciliación.
- Las reglas científicas de evaluación de evidencia.
- Los mecanismos automáticos de importación.
- La estructura editorial detallada de las monografías.

Los dominios serán desarrollados por ADM-003 y el modelo formal de información por ADM-004.

---

## 3. Principio Arquitectónico

El conocimiento del Atlas se organizará mediante una arquitectura híbrida en la que los objetos y sus relaciones constituyen la estructura formal del conocimiento, mientras que los documentos constituyen representaciones editoriales destinadas a comunicar dicho conocimiento.

La arquitectura general será:

```text
Atlas de Fitoterapia
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
        ├── Atributos
        ├── Relaciones
        ├── Afirmaciones
        │      │
        │      ▼
        │   Evidencia
        │      │
        │      ▼
        │  Procedencia
        │
        ▼
Grafo de Conocimiento
        │
        ▼
Vistas Editoriales
        │
        ▼
Publicación
```

Esta arquitectura establece una separación explícita entre:

```text
Conocimiento
     │
     ▼
Representación
     │
     ▼
Publicación
```

El conocimiento no dependerá de un archivo específico para existir como objeto gobernado.

---

## 4. Capas de la Arquitectura del Conocimiento

El modelo se organiza conceptualmente en siete capas.

```text
CAPA 1
Dominios de Conocimiento
        │
        ▼
CAPA 2
Entidades
        │
        ▼
CAPA 3
Relaciones
        │
        ▼
CAPA 4
Afirmaciones y Evidencia
        │
        ▼
CAPA 5
Procedencia
        │
        ▼
CAPA 6
Grafo de Conocimiento
        │
        ▼
CAPA 7
Vistas Editoriales
```

Cada capa mantiene una responsabilidad diferente y deberá poder evolucionar sin eliminar la separación conceptual entre las demás.

---

## 5. Capa de Dominios de Conocimiento

Los dominios constituyen las grandes áreas mediante las cuales se organiza conceptualmente el conocimiento del Atlas.

Su función principal es:

- Clasificar áreas de conocimiento.
- Establecer límites conceptuales.
- Facilitar navegación.
- Organizar entidades relacionadas.
- Permitir crecimiento modular.
- Evitar estructuras documentales monolíticas.
- Facilitar la incorporación futura de nuevos campos científicos.

Los dominios podrán contener subdominios cuando resulte necesario.

Conceptualmente:

```text
Atlas
 │
 ├── Dominio A
 │      ├── Subdominio A1
 │      └── Subdominio A2
 │
 ├── Dominio B
 │
 └── Dominio C
```

Los dominios no deberán confundirse con carpetas, documentos ni tecnologías de almacenamiento.

Un dominio representa una organización conceptual del conocimiento.

ADM-003 definirá los dominios y subdominios oficiales del Atlas.

---

## 6. Capa de Entidades

Las entidades representan objetos identificables dentro del conocimiento gobernado por el Atlas.

Una entidad podrá representar objetos biológicos, químicos, farmacognósticos, terapéuticos, documentales o científicos, entre otros.

Toda entidad gobernada deberá mantener identidad propia conforme al Sistema de Identificación Única establecido por ADR-002.

Conceptualmente:

```text
Objeto gobernado
      │
      ▼
Identidad Atlas
      │
      ▼
Entidad
      │
      ├── atributos
      ├── relaciones
      ├── afirmaciones
      └── procedencia
```

La entidad será independiente de:

- Su nombre.
- Su archivo.
- Su ubicación física.
- Su representación editorial.
- Su página pública.
- La fuente externa que la describa.
- Los identificadores externos asociados.

Por tanto:

```text
Entidad ≠ Archivo
Entidad ≠ Monografía
Entidad ≠ Página web
Entidad ≠ Fuente externa
```

ADM-004 definirá formalmente las entidades reconocidas por el Atlas y sus atributos.

---

## 7. Arquitectura Taxonómica

Debido al enfoque específico del Atlas en fitoterapia, la representación taxonómica tendrá como nivel superior documentado la **Familia**.

La jerarquía taxonómica principal será:

```text
Familia
  │
  ▼
Género
  │
  ▼
Especie
  │
  ▼
Subespecie / Variedad / Forma
cuando exista relevancia
```

Reino, división, clase y orden no formarán parte obligatoria del modelo taxonómico principal del Atlas.

Esta delimitación responde al propósito científico y fitoterapéutico del proyecto y evita incorporar niveles jerárquicos que, aunque taxonómicamente válidos, aportan menor utilidad directa al conocimiento que el Atlas pretende organizar.

### 7.1 Familia

La Familia constituye el nivel taxonómico superior documentado por el Atlas.

Su función será principalmente:

- Organización.
- Agrupación taxonómica.
- Navegación.
- Contextualización.
- Comparación entre géneros relacionados.

### 7.2 Género

El Género permitirá agrupar especies taxonómicamente relacionadas y facilitar:

- Navegación.
- Comparación entre especies.
- Reconciliación taxonómica.
- Integración con fuentes externas.

### 7.3 Especie

La **Especie será la unidad biológica principal para la documentación fitoterapéutica**.

Será el nivel sobre el cual se asociará principalmente conocimiento relacionado con:

- Partes vegetales.
- Drogas vegetales.
- Compuestos.
- Preparados.
- Usos tradicionales.
- Actividades biológicas.
- Indicaciones.
- Evidencia.
- Seguridad.
- Contraindicaciones.
- Interacciones.
- Farmacopeas.
- Referencias científicas.

Conceptualmente:

```text
Familia
   │
   ▼
Género
   │
   ▼
Especie
   │
   ├── partes vegetales
   ├── drogas vegetales
   ├── compuestos
   ├── preparados
   ├── actividades
   ├── usos
   ├── evidencia
   ├── seguridad
   └── fuentes
```

### 7.4 Niveles infraespecíficos

Los niveles inferiores a especie podrán representarse cuando tengan relevancia:

- Taxonómica.
- Fitoquímica.
- Farmacognóstica.
- Científica.
- Terapéutica.
- Regulatoria.

Podrán incluir, según corresponda:

- Subespecies.
- Variedades.
- Formas.

Otros conceptos biológicos o fitoquímicos, como los quimiotipos, no deberán asumirse automáticamente como rangos taxonómicos y deberán modelarse según su naturaleza científica en ADM-004.

---

## 8. No Herencia de Propiedades Taxonómicas

La pertenencia taxonómica no implicará herencia automática de propiedades fitoterapéuticas.

En consecuencia, el Atlas no deberá inferir automáticamente propiedades:

- Fitoquímicas.
- Farmacológicas.
- Terapéuticas.
- Toxicológicas.
- Etnobotánicas.
- Clínicas.

entre niveles taxonómicos.

Por tanto:

```text
Familia ─X─► Género ─X─► Especie
```

y tampoco:

```text
Especie ─X─► Género ─X─► Familia
```

donde `X` representa la prohibición de transferir automáticamente propiedades científicas entre los niveles únicamente por pertenencia taxonómica.

Por ejemplo, la existencia de evidencia terapéutica para una especie no permitirá atribuir automáticamente dicha propiedad:

- A otras especies del mismo género.
- Al género completo.
- A la familia completa.

Toda afirmación deberá mantener evidencia y procedencia propias.

---

## 9. Capa de Relaciones

Las relaciones representan vínculos semánticos explícitos entre entidades.

Permitirán construir progresivamente la estructura conectada del conocimiento.

Conceptualmente:

```text
Entidad A
   │
   └── relación ──► Entidad B
```

Ejemplos conceptuales:

```text
Especie ── contiene ──► Compuesto

Especie ── posee parte ──► Parte vegetal

Droga vegetal ── deriva de ──► Parte vegetal

Preparado ── utiliza ──► Droga vegetal

Compuesto ── asociado con ──► Actividad biológica
```

Estos ejemplos expresan únicamente arquitectura conceptual y no constituyen todavía el catálogo oficial de relaciones.

Las relaciones:

- Serán independientes de los documentos editoriales.
- Podrán participar en diferentes vistas editoriales.
- Podrán contar con múltiples evidencias.
- Podrán mantener procedencia.
- No deberán duplicarse innecesariamente por existir varias fuentes.
- Podrán evolucionar conforme crezca el modelo de información.

La definición formal de relaciones corresponderá a ADM-004.

---

## 10. Capa de Afirmaciones y Evidencia

Una relación, atributo o valor podrá estar sustentado por una o múltiples afirmaciones.

Una afirmación representa una declaración trazable acerca del conocimiento registrado.

Conceptualmente:

```text
Entidad A
   │
   └── relación ──► Entidad B
                       │
                       ├── Afirmación A
                       ├── Afirmación B
                       └── Afirmación C
```

Cada afirmación podrá estar sustentada por evidencia independiente.

Esto permitirá representar situaciones donde distintas fuentes:

- Coincidan.
- Complementen información.
- Proporcionen valores distintos.
- Empleen metodologías diferentes.
- Presenten conclusiones incompatibles.
- Contradigan afirmaciones anteriores.

La arquitectura deberá conservar estas diferencias.

Una afirmación registrada no será equivalente automáticamente a conocimiento científicamente aprobado.

Por tanto:

```text
Afirmación ≠ Verdad científica
```

El grado de validación, calidad, confianza o aceptación científica deberá establecerse mediante procesos y estándares posteriores.

---

## 11. Evidencia Contradictoria

El modelo deberá permitir conservar evidencia contradictoria sin eliminar silenciosamente información.

Conceptualmente:

```text
                    Relación
                       │
          ┌────────────┴────────────┐
          │                         │
          ▼                         ▼
   Afirmación A                Afirmación B
          │                         │
          ▼                         ▼
     Evidencia A                Evidencia B
          │                         │
          ▼                         ▼
      Fuente A                  Fuente B
```

La existencia de contradicción constituye información relevante.

El Atlas deberá preservar:

- La afirmación.
- La evidencia.
- La fuente.
- La procedencia.
- El contexto.
- La eventual resolución editorial o científica.

La arquitectura no deberá resolver contradicciones mediante eliminación automática de registros.

---

## 12. Capa de Procedencia

La procedencia constituye una propiedad arquitectónica fundamental del conocimiento del Atlas.

Toda información incorporada desde una fuente externa deberá poder conservar suficiente contexto para determinar su origen.

Conceptualmente:

```text
Dato u observación
       │
       ▼
Afirmación
       │
       ▼
Entidad / Relación
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

La procedencia deberá permitir, cuando corresponda, identificar:

- Fuente.
- Publicación.
- Base de datos.
- Farmacopea.
- Registro externo.
- Identificador externo.
- Fecha de consulta.
- Fecha de incorporación.
- Versión de la fuente.
- Método de obtención.
- Transformaciones realizadas.
- Referencia original.

Un dato incorporado no deberá perder su contexto de origen.

Por tanto:

```text
Dato externo ≠ Dato anónimo
```

---

## 13. Fuentes Externas

El Atlas podrá integrar información procedente de diferentes sistemas científicos externos.

Las fuentes externas podrán incluir, entre otras:

- Bases taxonómicas.
- Bases fitoquímicas.
- Repositorios químicos.
- Repositorios bibliográficos.
- Publicaciones científicas.
- Revisiones sistemáticas.
- Metaanálisis.
- Farmacopeas.
- Catálogos institucionales.
- Conjuntos de datos científicos.

La arquitectura establece que:

```text
Fuente externa
      │
      ▼
Dato / Observación
      │
      ▼
Afirmación
      │
      ▼
Proceso de gobernanza
      │
      ▼
Conocimiento del Atlas
```

La incorporación de información desde una fuente externa no significará aprobación automática.

En consecuencia:

```text
Fuente ≠ Verdad científica
```

y:

```text
Dato externo ≠ Conocimiento aprobado
```

La aceptación científica dependerá de las reglas editoriales, metodológicas y de evidencia que el Atlas establezca posteriormente.

---

## 14. Identificadores Externos e Interoperabilidad

Las entidades podrán relacionarse con identificadores provenientes de sistemas externos.

Conceptualmente:

```text
Entidad Atlas
     │
     ├── ID Atlas
     ├── ID externo A
     ├── ID externo B
     └── ID externo C
```

Los identificadores externos facilitarán:

- Interoperabilidad.
- Reconciliación.
- Integración de fuentes.
- Detección de duplicados.
- Referenciación cruzada.
- Actualización.
- Trazabilidad.

Sin embargo:

```text
ID externo ≠ Identidad Atlas
```

La identidad oficial continuará siendo la establecida por el Sistema de Identificación Única del Atlas.

---

## 15. Capa del Grafo de Conocimiento

Las entidades y relaciones constituirán progresivamente el grafo de conocimiento del Atlas.

Conceptualmente:

```text
Entidades + Relaciones = Grafo de Conocimiento
```

El grafo permitirá representar conocimiento conectado entre diferentes dominios.

Ejemplo conceptual:

```text
                         Especie
                  ┌────────┼────────┐
                  │        │        │
                  ▼        ▼        ▼
            Parte vegetal Compuesto Preparado
                  │        │        │
                  ▼        ▼        ▼
            Droga vegetal Actividad Uso
                  │        │        │
                  └────────┼────────┘
                           │
                           ▼
                       Evidencia
                           │
                           ▼
                         Fuente
```

El grafo de conocimiento constituye una **representación conceptual de las conexiones entre objetos gobernados**.

Este documento no obliga a utilizar una tecnología específica de base de datos de grafos.

Por tanto:

```text
Grafo conceptual ≠ Motor de grafo
```

ADM-002 no prescribe tecnologías como:

- Neo4j.
- RDF Store.
- GraphDB.
- PostgreSQL.
- JSON-LD.
- Otras tecnologías de persistencia.

Las decisiones de implementación deberán establecerse posteriormente y, cuando tengan carácter arquitectónico permanente, documentarse conforme a ADR-004.

---

## 16. Capa de Vistas Editoriales

Los documentos, monografías, fichas y páginas públicas serán vistas editoriales construidas a partir del conocimiento gobernado.

Conceptualmente:

```text
Entidades
   │
   ├── Relaciones
   ├── Afirmaciones
   ├── Evidencia
   └── Procedencia
          │
          ▼
     Vista Editorial
          │
          ▼
       Publicación
```

Una vista editorial podrá integrar información procedente de múltiples entidades y relaciones.

Del mismo modo, una entidad podrá aparecer en múltiples vistas editoriales.

Por tanto:

```text
Entidad ≠ Vista Editorial
```

y:

```text
Monografía ≠ Entidad
```

La modificación de una representación editorial no deberá alterar por sí misma la identidad del objeto gobernado.

---

## 17. Separación entre Taxonomía y Fitoterapia

La taxonomía constituye una dimensión necesaria para identificar y contextualizar especies, pero no representa por sí sola conocimiento fitoterapéutico.

La arquitectura mantendrá separadas ambas dimensiones:

```text
             TAXONOMÍA
                 │
     Familia → Género → Especie
                         │
                         ▼
                   FITOTERAPIA
                         │
          ┌──────────────┼──────────────┐
          │              │              │
     Droga vegetal   Compuestos     Preparados
          │              │              │
          ▼              ▼              ▼
       Usos         Actividades      Evidencia
          │              │              │
          └──────────────┼──────────────┘
                         ▼
                      Fuentes
```

En consecuencia:

```text
Taxonomía ≠ Fitoterapia
```

aunque ambas dimensiones estarán relacionadas dentro del grafo.

---

## 18. Flujo Conceptual del Conocimiento

El flujo general del conocimiento será:

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
Grafo de conocimiento
   │
   ▼
Vista editorial
   │
   ▼
Publicación
```

Este flujo no implica necesariamente una secuencia técnica de procesamiento.

Representa la arquitectura conceptual mediante la cual una observación externa puede transformarse progresivamente en conocimiento integrado y posteriormente en contenido publicado.

---

## 19. Automatización y Agentes de Inteligencia Artificial

La arquitectura deberá permitir el crecimiento progresivo del Atlas mediante automatización y agentes de inteligencia artificial sin eliminar la gobernanza humana.

Los procesos automáticos podrán participar en actividades como:

- Descubrimiento de fuentes.
- Identificación de entidades.
- Extracción de candidatos a relaciones.
- Detección de identificadores externos.
- Detección de posibles duplicados.
- Identificación de evidencia adicional.
- Detección de contradicciones.
- Generación de propuestas editoriales.

Sin embargo, la automatización deberá preservar:

- Identidad.
- Procedencia.
- Evidencia.
- Contexto.
- Historial.
- Estado de validación.

La automatización no deberá convertir automáticamente datos externos en conocimiento aprobado.

Conceptualmente:

```text
Automatización
      │
      ▼
Descubrimiento / Propuesta
      │
      ▼
Trazabilidad
      │
      ▼
Gobernanza
      │
      ▼
Validación
      │
      ▼
Conocimiento aprobado
```

Este principio permitirá que el Atlas crezca progresivamente sin perder control sobre la calidad y el origen del conocimiento.

---

## 20. Separaciones Arquitectónicas Obligatorias

La arquitectura del conocimiento deberá preservar las siguientes separaciones:

```text
Entidad ≠ Archivo
```

```text
Entidad ≠ Monografía
```

```text
Taxonomía ≠ Fitoterapia
```

```text
Fuente ≠ Verdad científica
```

```text
Dato externo ≠ Conocimiento aprobado
```

```text
Identificador externo ≠ Identidad Atlas
```

```text
Grafo conceptual ≠ Tecnología de almacenamiento
```

```text
Conocimiento ≠ Representación editorial
```

Estas separaciones deberán mantenerse en los modelos y estándares posteriores.

---

## 21. Responsabilidades Arquitectónicas

| Componente | Responsabilidad |
|------------|-----------------|
| Dominios | Organizar conceptualmente grandes áreas del conocimiento. |
| Subdominios | Especializar áreas cuando resulte necesario. |
| Entidades | Representar objetos identificables y gobernados. |
| Atributos | Describir propiedades de las entidades. |
| Relaciones | Expresar conexiones semánticas entre entidades. |
| Afirmaciones | Representar declaraciones trazables sobre entidades, atributos o relaciones. |
| Evidencia | Sustentar o cuestionar afirmaciones. |
| Procedencia | Preservar el origen y contexto del conocimiento. |
| Grafo de conocimiento | Integrar entidades y relaciones en una estructura conectada. |
| Vistas editoriales | Comunicar el conocimiento mediante documentos y publicaciones. |

---

## 22. Dependencias Arquitectónicas

ADM-002 depende de los siguientes documentos:

```text
GOV-001
   │
   ▼
ADR-002
Sistema de Identificación Única
   │
   ▼
ADR-003
Jerarquía Normativa
   │
   ▼
ADR-004
Arquitectura antes que Implementación
   │
   ▼
ADR-005
Modelo Híbrido del Conocimiento
   │
   ▼
ADM-002
Arquitectura del Modelo de Conocimiento
```

ADM-002 servirá a su vez como base para:

```text
ADM-002
Arquitectura del Modelo de Conocimiento
        │
        ├───────────────┐
        ▼               ▼
     ADM-003          ADM-004
 Dominios de       Modelo de
 Conocimiento      Información
        │               │
        └───────┬───────┘
                ▼
            Estándares
                │
                ▼
          Implementación
```

---

## 23. Restricciones Arquitectónicas

La evolución del modelo deberá respetar las siguientes restricciones:

- Toda entidad gobernada deberá mantener identidad estable.
- La especie será la unidad biológica principal para la documentación fitoterapéutica.
- La Familia será el nivel taxonómico superior documentado obligatoriamente.
- No existirá herencia automática de propiedades científicas entre niveles taxonómicos.
- Toda información externa deberá poder conservar procedencia.
- Una fuente externa no constituirá automáticamente evidencia suficiente.
- Una afirmación no constituirá automáticamente una verdad científica aprobada.
- La evidencia contradictoria deberá poder conservarse.
- Los documentos serán representaciones editoriales y no unidades exclusivas de conocimiento.
- El grafo conceptual no dependerá de una tecnología específica.
- La automatización deberá preservar trazabilidad y gobernanza.
- Las decisiones de implementación permanente deberán respetar ADR-004.

---

## 24. Evolución de la Arquitectura

La evolución prevista será:

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
        │
        ▼
Conocimiento estructurado
        │
        ▼
Automatización progresiva
```

ADM-002 deberá permanecer independiente de tecnologías específicas para permitir que la implementación evolucione sin alterar innecesariamente la arquitectura conceptual.

---

## 25. Referencias

- GOV-001 — Constitución del Atlas de Fitoterapia.
- ADM-001 — Arquitectura General del Atlas de Fitoterapia.
- ADR-002 — Sistema de Identificación Única.
- ADR-003 — Jerarquía Normativa.
- ADR-004 — Arquitectura antes que Implementación.
- ADR-005 — Modelo Híbrido del Conocimiento.

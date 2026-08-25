---
id: ADM-003
title: Dominios de Conocimiento del Atlas
version: 1.0.0
status: Approved
type: ADM
created: 2026-08-18
updated: 2026-08-18
author: Proyecto Atlas de Fitoterapia
tags:
  - architecture
  - knowledge
  - domains
  - phytotherapy
  - evidence
  - provenance
---

# Dominios de Conocimiento del Atlas

## 1. Propósito

Definir los dominios y subdominios mediante los cuales el Atlas de Fitoterapia organizará conceptualmente el conocimiento científico, botánico, farmacognóstico, fitoquímico, etnobotánico, farmacológico, clínico, terapéutico, toxicológico y regulatorio relacionado con las plantas medicinales y la fitoterapia.

Este documento desarrolla la Capa de Dominios de Conocimiento establecida por ADM-002 y determina los límites conceptuales necesarios para evitar duplicidad, ambigüedad y mezcla de responsabilidades entre diferentes tipos de conocimiento.

ADM-003 establece **qué áreas de conocimiento reconoce el Atlas y qué responsabilidad conceptual corresponde a cada una**.

No define todavía:

- Entidades formales.
- Atributos.
- Campos obligatorios.
- Cardinalidades.
- Catálogos de relaciones.
- Esquemas de datos.
- Ontologías.
- Formatos físicos de almacenamiento.
- Tecnologías de persistencia.
- Reglas de extracción automática.
- Plantillas editoriales definitivas.

Estos elementos corresponderán principalmente a ADM-004 y a los estándares que deriven posteriormente de dicho modelo.

---

## 2. Alcance

ADM-003 establece los siguientes dominios temáticos oficiales del Atlas:

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

Adicionalmente, establece **Fuentes y Procedencia como capa transversal** aplicable a todos los dominios y no como dominio temático independiente.

Conceptualmente:

```text
Atlas de Fitoterapia
│
├── Botánica
├── Farmacognosia
├── Fitoquímica
├── Etnobotánica y Uso Tradicional
├── Farmacología
├── Evidencia Científica y Clínica
├── Uso Terapéutico
├── Seguridad y Toxicología
└── Regulación y Farmacopeas
          │
          │
          ▼
   Todos sustentados por
   Fuentes y Procedencia
```

---

## 3. Principio de Cobertura No Obligatoria

La existencia de un dominio, subdominio o tipo de conocimiento dentro de esta arquitectura **no obliga a que todas las entidades del Atlas dispongan de información para todos sus elementos**.

La estructura de dominios define qué conocimiento puede representar el Atlas.

Cada elemento deberá documentarse únicamente cuando exista información:

- Pertinente.
- Suficientemente sustentada.
- Trazable.
- Aplicable al objeto representado.

Por tanto:

```text
Elemento del modelo
      │
      ├── existe información sustentada
      │      └──► se documenta
      │
      ├── no existe información disponible
      │      └──► no se inventa
      │
      ├── existe información contradictoria
      │      └──► se preservan las afirmaciones
      │           y su procedencia
      │
      └── no resulta aplicable
             └──► no se fuerza su inclusión
```

La ausencia de información no deberá completarse mediante inferencia automática.

Este principio aplica transversalmente a todos los dominios y deberá ser respetado por:

- Personas.
- Procesos editoriales.
- Herramientas.
- Sistemas de integración.
- Automatizaciones.
- Agentes de inteligencia artificial.

---

## 4. Principio de Separación de Responsabilidades

Cada dominio representa una responsabilidad conceptual diferente.

Una misma entidad podrá participar en múltiples dominios sin que ello implique duplicar su identidad.

Por ejemplo:

```text
Curcumina
   │
   ├── composición química
   │      → Fitoquímica
   │
   ├── actividad biológica
   │      → Farmacología
   │
   ├── estudios que la investigan
   │      → Evidencia Científica y Clínica
   │
   └── riesgos documentados
          → Seguridad y Toxicología
```

Por tanto:

```text
Entidad compartida ≠ conocimiento duplicado
```

y:

```text
Dominio ≠ silo independiente
```

Los dominios organizan perspectivas diferentes de un conocimiento interconectado.

---

# 5. Dominio: Botánica

## 5.1 Propósito

El dominio Botánica representa el conocimiento necesario para identificar, clasificar, describir y contextualizar biológicamente los organismos vegetales documentados por el Atlas.

Responde principalmente a preguntas como:

```text
¿Qué organismo vegetal es?
¿Cómo se clasifica?
¿Cómo se reconoce?
¿Cómo es?
¿Dónde ocurre?
¿En qué condiciones vive?
```

## 5.2 Subdominios

Botánica podrá comprender:

```text
Botánica
├── Taxonomía y nomenclatura
├── Morfología
├── Anatomía vegetal
├── Identificación botánica
├── Distribución geográfica
├── Hábitat y ecología
└── Fenología
```

### 5.2.1 Taxonomía y nomenclatura

Comprende la clasificación e identidad nomenclatural del organismo vegetal.

La arquitectura taxonómica principal seguirá lo establecido en ADM-002:

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

Podrá comprender información relacionada con:

- Familia.
- Género.
- Especie.
- Niveles infraespecíficos pertinentes.
- Nombre científico.
- Autoría botánica.
- Sinónimos.
- Nombre aceptado.
- Historia nomenclatural cuando resulte relevante.

La especie continuará siendo la unidad biológica principal para la documentación fitoterapéutica.

No existirá herencia automática de propiedades científicas entre niveles taxonómicos.

### 5.2.2 Morfología

Comprende la descripción externa de la planta y sus principales estructuras cuando exista información pertinente.

Podrá considerar:

- Hábito de crecimiento.
- Raíz.
- Tallo.
- Hoja.
- Flor.
- Fruto.
- Semilla.
- Otros caracteres morfológicos relevantes.

### 5.2.3 Anatomía vegetal

Comprende la organización interna de tejidos y estructuras vegetales cuando dicha información exista y resulte pertinente.

La anatomía botánica deberá distinguirse de los caracteres microscópicos empleados específicamente para autenticar una droga vegetal.

Conceptualmente:

```text
Anatomía de la planta
→ Botánica

Caracteres microscópicos utilizados para
identificar una droga vegetal
→ Farmacognosia
```

### 5.2.4 Identificación botánica

Comprende conocimiento destinado a reconocer y diferenciar correctamente una entidad vegetal.

Podrá considerar:

- Caracteres diagnósticos.
- Diferenciación entre especies próximas.
- Especies morfológicamente similares.
- Claves o criterios de identificación cuando estén disponibles.

### 5.2.5 Distribución geográfica

Describe dónde ocurre una especie o taxón.

Podrá incluir, según disponibilidad:

- Países.
- Regiones.
- Distribución nativa.
- Distribución introducida.
- Otros contextos biogeográficos pertinentes.

### 5.2.6 Hábitat y ecología

Describe las condiciones ambientales y ecológicas relacionadas con la presencia de una planta.

Podrá incluir:

- Ecosistema.
- Hábitat.
- Altitud.
- Clima.
- Suelo.
- Asociaciones ecológicas relevantes.

### 5.2.7 Fenología

Describe fenómenos biológicos periódicos o estacionales.

Podrá comprender:

- Floración.
- Fructificación.
- Brotación.
- Otros periodos estacionales relevantes.

La existencia del subdominio Fenología no obliga a documentar esta información para todas las especies.

---

# 6. Dominio: Farmacognosia

## 6.1 Propósito

El dominio Farmacognosia representa el conocimiento relacionado con la identidad, autenticidad, características y calidad de las drogas vegetales empleadas con fines medicinales.

Responde principalmente a:

```text
¿Qué droga vegetal es?
¿De qué parte vegetal procede?
¿Cómo puede identificarse?
¿Cómo se determina su autenticidad?
¿Cómo se evalúa su calidad?
```

## 6.2 Subdominios

```text
Farmacognosia
├── Droga vegetal
├── Parte vegetal de origen
├── Identificación farmacognóstica
│   ├── caracteres macroscópicos
│   └── caracteres microscópicos
├── Autenticidad
├── Pureza
├── Criterios de calidad
├── Adulteración y sustitución
├── Marcadores de calidad
└── Métodos de control
```

### 6.2.1 Droga vegetal

Representa el material vegetal reconocido y utilizado como materia prima medicinal.

Deberá mantenerse conceptualmente separado del taxón y de la parte vegetal:

```text
Taxón
   │
   ▼
Parte vegetal
   │
   ▼
Droga vegetal
```

Una especie podrá originar diferentes drogas vegetales.

### 6.2.2 Identificación farmacognóstica

Comprende las características empleadas para autenticar una droga vegetal.

Podrá incluir:

- Caracteres macroscópicos.
- Caracteres microscópicos.
- Rasgos diagnósticos.
- Otros procedimientos de identificación pertinentes.

### 6.2.3 Autenticidad

Comprende los elementos que permiten establecer que el material corresponde efectivamente a la droga vegetal declarada.

### 6.2.4 Pureza

Comprende criterios relacionados con la ausencia o presencia aceptable de materiales, sustancias o condiciones que afecten la calidad de la droga vegetal.

### 6.2.5 Criterios de calidad

Comprende parámetros utilizados para evaluar la calidad farmacognóstica de una droga vegetal.

Podrán documentarse únicamente cuando exista una fuente pertinente que los sustente.

### 6.2.6 Adulteración y sustitución

Comprende información relacionada con:

- Sustitución por otras especies.
- Uso de materiales vegetales incorrectos.
- Mezclas no declaradas.
- Adulteraciones.
- Confusiones relevantes para autenticidad o seguridad.

### 6.2.7 Marcadores de calidad

Un compuesto químico podrá actuar como marcador empleado para control de calidad.

Se mantendrá la siguiente separación:

```text
Compuesto o marcador químico
→ Fitoquímica

Uso de ese compuesto como criterio
de identidad, estandarización o calidad
→ Farmacognosia
```

### 6.2.8 Métodos de control

Comprende métodos utilizados para verificar identidad, autenticidad, pureza o calidad cuando exista información pertinente y suficientemente sustentada.

---

# 7. Dominio: Fitoquímica

## 7.1 Propósito

El dominio Fitoquímica representa la composición química de las plantas, partes vegetales y drogas vegetales, así como la clasificación, distribución, variabilidad y biosíntesis de sus componentes.

Responde principalmente a:

```text
¿Qué compuestos contiene?
¿A qué clases químicas pertenecen?
¿Cómo se distribuyen?
¿Cómo varían?
¿Cómo se biosintetizan cuando esta información se conoce?
```

## 7.2 Subdominios

```text
Fitoquímica
├── Compuestos químicos
├── Clases y grupos químicos
├── Metabolitos primarios
├── Metabolitos secundarios
├── Perfil fitoquímico
├── Distribución de compuestos
├── Marcadores químicos
├── Variabilidad química
└── Biosíntesis
    ├── precursores
    ├── intermediarios
    └── vías biosintéticas
```

### 7.2.1 Compuestos químicos

Los compuestos químicos constituyen objetos individuales que podrán relacionarse con plantas, partes vegetales, drogas vegetales y otros objetos del Atlas.

### 7.2.2 Metabolitos

Los metabolitos primarios y secundarios representan clasificaciones aplicables a los compuestos.

Conceptualmente:

```text
Compuesto químico
      │
      └── clasificación
             │
             ├── metabolito primario
             └── metabolito secundario
```

Un metabolito no deberá duplicarse como una entidad distinta únicamente por pertenecer a una categoría metabólica.

### 7.2.3 Perfil fitoquímico

El perfil fitoquímico representa el conjunto de compuestos químicos detectados o caracterizados en un material vegetal bajo un contexto determinado.

Conceptualmente:

```text
Especie
   │
   ▼
Parte / droga vegetal
   │
   ▼
Perfil fitoquímico
   │
   ├── compuesto A
   ├── compuesto B
   └── compuesto C
```

Un perfil fitoquímico podrá variar dependiendo de factores como:

- Parte vegetal.
- Taxón.
- Origen.
- Condiciones ambientales.
- Etapa de desarrollo.
- Material analizado.
- Método de obtención.
- Método analítico.

Estos factores no constituyen todavía campos formales; su representación corresponderá a ADM-004 cuando resulte necesaria.

### 7.2.4 Marcadores químicos

Un compuesto podrá ser reconocido como marcador químico.

Su existencia como compuesto corresponde a Fitoquímica.

Su empleo como criterio de calidad corresponde a Farmacognosia.

### 7.2.5 Variabilidad química

Comprende diferencias documentadas en la composición química de materiales vegetales.

La existencia de variación química no deberá interpretarse automáticamente como diferencia taxonómica.

### 7.2.6 Biosíntesis

Comprende información disponible acerca de la formación biológica de metabolitos.

Podrá considerar:

- Precursores.
- Intermediarios.
- Vías biosintéticas.
- Otros componentes pertinentes de la biosíntesis.

La biosíntesis será documentada cuando exista información científica suficientemente sustentada y aporte valor para comprender la formación, clasificación o variabilidad de los metabolitos.

No constituye información obligatoria para todos los compuestos.

---

# 8. Dominio: Etnobotánica y Uso Tradicional

## 8.1 Propósito

Este dominio representa el conocimiento acerca de la relación histórica, cultural y tradicional entre comunidades humanas y plantas utilizadas con fines medicinales.

Responde principalmente a:

```text
¿Quién utiliza o utilizó la planta?
¿Dónde?
¿En qué contexto cultural?
¿Para qué finalidad tradicional?
¿Qué parte se utiliza?
¿Cómo se prepara tradicionalmente?
```

## 8.2 Alcance conceptual

Podrá comprender:

- Grupo humano o comunidad.
- Región.
- Sistema tradicional.
- Parte utilizada.
- Preparación tradicional.
- Finalidad tradicional.
- Vía tradicional de administración.
- Contexto histórico.
- Contexto cultural.
- Prácticas tradicionales relacionadas.
- Fuentes etnográficas, históricas o tradicionales.

La definición formal de estos objetos corresponderá a ADM-004.

## 8.3 Separación entre uso tradicional y uso terapéutico contemporáneo

El Atlas mantendrá explícitamente:

```text
Uso tradicional
≠
Indicación terapéutica validada
```

y:

```text
Historia de uso
≠
Evidencia clínica
```

Un mismo propósito podrá aparecer tanto en Etnobotánica y Uso Tradicional como en Uso Terapéutico, siempre que se representen como afirmaciones distintas, con fuentes y contextos propios.

---

# 9. Dominio: Farmacología

## 9.1 Propósito

Farmacología representa las actividades biológicas, efectos y mecanismos asociados a sustancias, compuestos, drogas vegetales o preparados estudiados.

Responde principalmente a:

```text
¿Qué actividad biológica presenta?
¿Qué efecto farmacológico se observa?
¿Qué mecanismo puede explicar ese efecto?
¿Cómo interactúa con sistemas biológicos?
```

## 9.2 Subdominios

```text
Farmacología
├── Actividad biológica
├── Mecanismo de acción
├── Farmacodinámica
└── Farmacocinética
```

Los subdominios se documentarán únicamente cuando exista información pertinente.

## 9.3 Separación entre Farmacología y Evidencia

Farmacología describe **qué actividad, efecto o mecanismo se afirma**.

Evidencia Científica y Clínica describe **qué estudios sustentan, limitan, contradicen o contextualizan esa afirmación**.

Por tanto:

```text
Farmacología
= QUÉ efecto o mecanismo se describe

Evidencia
= CÓMO se sustenta esa descripción
```

Un resultado experimental aislado no deberá convertirse automáticamente en propiedad farmacológica confirmada.

```text
Resultado experimental
≠
Propiedad farmacológica confirmada
```

---

# 10. Dominio: Evidencia Científica y Clínica

## 10.1 Propósito

Este dominio representa los estudios, investigaciones y síntesis de evidencia utilizados para sustentar, limitar, contextualizar o contradecir afirmaciones científicas del Atlas.

Responde principalmente a:

```text
¿Cómo sabemos esto?
¿Qué estudio lo investigó?
¿En qué modelo?
¿En qué población?
¿Qué resultados se obtuvieron?
¿Existen resultados contradictorios?
```

## 10.2 Estructura conceptual

```text
Evidencia Científica y Clínica
│
├── Evidencia preclínica
│   ├── In vitro
│   ├── Ex vivo
│   ├── In vivo animal
│   └── In silico
│       cuando resulte pertinente
│
└── Evidencia clínica
    ├── Estudios observacionales
    ├── Ensayos clínicos
    └── Síntesis de evidencia
        ├── Revisiones sistemáticas
        └── Metaanálisis
```

Esta estructura es conceptual y no constituye todavía una clasificación metodológica exhaustiva.

## 10.3 Evidencia preclínica

Podrá comprender estudios:

- In vitro.
- Ex vivo.
- In vivo en animales.
- In silico cuando resulte científicamente pertinente.

La evidencia preclínica no deberá interpretarse automáticamente como demostración de eficacia clínica en seres humanos.

```text
Evidencia preclínica
≠
Eficacia clínica demostrada
```

## 10.4 Evidencia clínica

Comprende estudios realizados en seres humanos y síntesis de dichos estudios.

Podrá incluir:

- Estudios observacionales.
- Ensayos clínicos.
- Revisiones sistemáticas.
- Metaanálisis.

Las revisiones sistemáticas y los metaanálisis representan tipos o métodos de síntesis de evidencia.

La organización que produce una revisión no deberá confundirse con el tipo de evidencia.

Conceptualmente:

```text
Organización / productor
≠
Tipo de evidencia
```

## 10.5 Evidencia contradictoria

El dominio deberá permitir representar estudios que:

- Coincidan.
- Difieran.
- Produzcan resultados negativos.
- Presenten resultados incompatibles.
- Limiten afirmaciones existentes.
- Contradigan conclusiones anteriores.

La contradicción deberá conservarse y permanecer trazable conforme a ADM-002.

---

# 11. Dominio: Uso Terapéutico

## 11.1 Propósito

El dominio Uso Terapéutico representa aplicaciones clínicas o terapéuticas contemporáneas reconocidas, propuestas o investigadas para una planta, droga vegetal, preparado u otro objeto pertinente.

Responde principalmente a:

```text
¿Para qué condición se utiliza o propone?
¿Quién reconoce ese uso?
¿En qué población?
¿Bajo qué condiciones?
¿Con qué forma de utilización?
```

## 11.2 Categorías conceptuales de uso

El Atlas deberá poder distinguir, cuando resulte pertinente:

```text
Uso Terapéutico
├── Uso oficialmente reconocido
├── Uso respaldado por monografía científico-técnica
├── Uso investigado clínicamente
└── Uso tradicional
    └── vinculado con
        Etnobotánica y Uso Tradicional
```

Estas categorías no representan automáticamente niveles equivalentes de respaldo científico.

## 11.3 Fuentes para el uso terapéutico

Las fuentes podrán comprender, de manera priorizada y según pertinencia:

```text
1. Autoridades regulatorias
2. Monografías científico-técnicas reconocidas
3. Guías clínicas y consensos
4. Revisiones sistemáticas y metaanálisis
5. Ensayos clínicos
6. Estudios observacionales
```

Esta enumeración orienta la procedencia del conocimiento y no constituye por sí misma una escala formal de calidad de evidencia.

La evaluación metodológica específica deberá definirse posteriormente.

## 11.4 Separación entre uso y evidencia

```text
Uso Terapéutico
= QUÉ aplicación clínica se reconoce,
  propone o investiga

Evidencia Científica y Clínica
= QUÉ estudios sustentan,
  limitan o contradicen ese uso
```

Por tanto:

```text
Indicación o uso terapéutico
≠
Evidencia clínica
```

La existencia de un ensayo que investigue un uso no deberá convertir automáticamente dicho uso en una indicación terapéutica oficialmente reconocida.

## 11.5 Contexto terapéutico

Cuando la información exista, un uso terapéutico podrá requerir contexto relacionado con:

- Condición o indicación.
- Población.
- Dosis.
- Vía de administración.
- Duración.
- Forma de uso.
- Preparado o intervención.
- Condiciones particulares de utilización.

ADM-003 reconoce estos conceptos pero no los establece todavía como atributos formales.

---

# 12. Dominio: Seguridad y Toxicología

## 12.1 Propósito

Este dominio representa riesgos, limitaciones, eventos adversos y demás condiciones de seguridad relacionadas con el uso de plantas, drogas vegetales, compuestos o preparados.

Responde principalmente a:

```text
¿Qué riesgos se conocen?
¿Qué toxicidad se ha documentado?
¿Qué contraindicaciones existen?
¿Qué precauciones deben considerarse?
¿Qué interacciones se conocen?
¿Qué poblaciones requieren atención especial?
```

## 12.2 Subdominios

```text
Seguridad y Toxicología
├── Toxicidad
├── Reacciones adversas
├── Contraindicaciones
├── Precauciones
├── Interacciones
├── Poblaciones especiales
└── Señales de seguridad
```

## 12.3 Contraindicación y precaución

Se mantendrá conceptualmente la diferencia:

```text
Contraindicación
= condición en la cual el uso debe evitarse
  conforme a la fuente aplicable

Precaución
= condición que requiere valoración,
  vigilancia o consideración especial
```

La formulación concreta deberá preservar el significado de la fuente de procedencia y no deberá ampliarse automáticamente.

## 12.4 Señales de seguridad

Una señal de seguridad representa información que puede justificar investigación o vigilancia adicional.

Por tanto:

```text
Señal de seguridad
≠
Riesgo clínicamente confirmado
```

## 12.5 Separación entre seguridad y evidencia

```text
Seguridad y Toxicología
= QUÉ riesgo o condición de seguridad se describe

Evidencia
= CÓMO se sustenta, limita,
  contradice o contextualiza esa afirmación
```

---

# 13. Dominio: Regulación y Farmacopeas

## 13.1 Propósito

Este dominio representa el contexto oficial, normativo y farmacopéico relacionado con plantas medicinales, drogas vegetales, preparados y demás objetos relevantes para el Atlas.

Responde principalmente a:

```text
¿Qué organismo reconoce o regula este objeto?
¿Existe una monografía oficial?
¿En qué farmacopea aparece?
¿Cuál es su estatus regulatorio?
¿Qué disposición normativa resulta aplicable?
```

## 13.2 Subdominios

```text
Regulación y Farmacopeas
├── Farmacopeas
│   └── Monografías farmacopéicas
├── Monografías regulatorias no farmacopéicas
├── Estatus regulatorio
├── Disposiciones normativas
└── Reconocimiento oficial
```

## 13.3 Tipos conceptuales de monografía

El Atlas deberá ser capaz de distinguir conceptualmente:

```text
Monografía
├── Farmacopéica
│   └── pertenece a una farmacopea
│
├── Regulatoria / terapéutica
│   └── emitida por una autoridad
│       u organismo regulatorio
│
└── Científica / técnica
    └── emitida por una organización
        científica o técnica
```

La clasificación formal de documentos corresponderá a ADM-004.

## 13.4 Farmacopeas y drogas vegetales

La relación farmacopéica no deberá asumirse siempre directamente entre especie y farmacopea.

Cuando corresponda, la relación conceptual será:

```text
Especie
   │
   ▼
Parte vegetal
   │
   ▼
Droga vegetal
   │
   ▼
Monografía farmacopéica
   │
   ▼
Farmacopea
```

Una misma especie podrá originar diversas drogas vegetales y éstas podrán encontrarse documentadas de forma diferente por distintas fuentes.

## 13.5 Separación con Farmacognosia

Los criterios técnicos de identidad y calidad pertenecen conceptualmente a Farmacognosia.

La fuente normativa que establece dichos criterios pertenece a Regulación y Farmacopeas.

```text
Criterio de calidad
→ Farmacognosia

Farmacopea o monografía
que establece el criterio
→ Regulación y Farmacopeas
```

## 13.6 Cobertura regulatoria progresiva

El Atlas no intentará mantener una reproducción exhaustiva y en tiempo real de todas las regulaciones y farmacopeas existentes.

La cobertura será:

```text
Cobertura de fuentes
→ priorizada y progresiva

Actualización
→ incremental

Mantenimiento
→ apoyado por automatización

Cambio detectado
→ sujeto a gobernanza
```

La detección automática de una modificación regulatoria no implicará actualización automática del conocimiento aprobado.

---

# 14. Fuentes y Procedencia como Capa Transversal

Fuentes y Procedencia no constituirán un dominio temático independiente.

Representan una capacidad transversal de trazabilidad aplicable a todos los dominios.

Conceptualmente:

```text
Botánica ───────────────────┐
Farmacognosia ──────────────┤
Fitoquímica ────────────────┤
Etnobotánica ───────────────┤
Farmacología ───────────────┤
Evidencia ──────────────────┼──► Procedencia
Uso Terapéutico ────────────┤
Seguridad y Toxicología ────┤
Regulación y Farmacopeas ───┘
```

La regla fundamental será:

```text
Los dominios describen
QUÉ conocimiento representa el Atlas.

La procedencia describe
DE DÓNDE proviene ese conocimiento.
```

La procedencia deberá preservar suficiente información para permitir determinar el origen y contexto de una afirmación conforme a ADM-002.

Cuando corresponda podrá conservar información como:

- Fuente.
- Tipo de fuente.
- Organización.
- Publicación.
- Identificador externo.
- URL de referencia.
- Fecha de consulta.
- Fecha de incorporación.
- Edición.
- Versión.
- Estado de vigencia.
- Referencia original.
- Transformaciones realizadas.

ADM-004 determinará qué elementos deberán representarse formalmente.

---

# 15. Autoridad de las Fuentes según el Tipo de Conocimiento

El Atlas no establecerá una única fuente externa como autoridad universal para todos los tipos de información.

La fuente pertinente dependerá de la naturaleza del conocimiento.

Conceptualmente:

```text
Tipo de conocimiento
│
├── Nomenclatura botánica
│      └── fuente nomenclatural pertinente
│
├── Estatus taxonómico
│      └── fuente taxonómica pertinente
│
├── Droga vegetal
│      └── farmacopea o monografía pertinente
│
├── Compuesto químico
│      └── repositorio químico pertinente
│
├── Uso terapéutico
│      └── fuente regulatoria, científica
│          o clínica pertinente
│
└── Evidencia científica
       └── estudio, publicación o
           repositorio científico pertinente
```

Por tanto:

```text
Fuente autorizada para un dato
≠
Autoridad universal del Atlas
```

La selección y priorización formal de fuentes podrá establecerse mediante estándares posteriores.

---

# 16. Conocimiento Temático frente a Evidencia

Para evitar que los estudios científicos se conviertan automáticamente en propiedades aceptadas, ADM-003 establece la siguiente separación transversal:

```text
Dominios temáticos
= QUÉ sabemos, describimos o afirmamos

Evidencia Científica y Clínica
= CÓMO se sustenta, limita,
  contradice o contextualiza ese conocimiento
```

Por ejemplo:

```text
Compuesto presente
→ Fitoquímica

Actividad antiinflamatoria propuesta
→ Farmacología

Uso para una condición clínica
→ Uso Terapéutico

Riesgo hepático
→ Seguridad y Toxicología

Estudio que sustenta cualquiera
de las afirmaciones anteriores
→ Evidencia Científica y Clínica
```

La existencia de evidencia no deberá eliminar la procedencia propia de la afirmación.

---

# 17. Preparados, Procesamiento y Tecnología

ADM-003 no establece por ahora un dominio independiente denominado Preparados, Procesamiento o Tecnología.

La información relacionada con preparados deberá ubicarse según su contexto científico.

Conceptualmente:

```text
Preparación tradicional
→ Etnobotánica y Uso Tradicional

Droga vegetal y tratamiento
farmacognóstico pertinente
→ Farmacognosia

Extracto utilizado en un estudio
→ contexto de Evidencia

Forma o intervención terapéutica
→ Uso Terapéutico

Extracto estandarizado y marcador
→ Farmacognosia + Fitoquímica
  según corresponda
```

La arquitectura podrá incorporar posteriormente un dominio específico para procesamiento, preparaciones o tecnología cuando exista:

- Volumen suficiente de conocimiento.
- Diferenciación conceptual clara.
- Fuentes recurrentes.
- Necesidad científica demostrada.
- Justificación arquitectónica.

La creación futura de dicho dominio deberá realizarse mediante la evolución gobernada del modelo.

---

# 18. Relaciones entre Dominios

Los dominios no son estructuras aisladas.

Conceptualmente, el conocimiento podrá conectarse de la siguiente manera:

```text
Botánica
   │
   ▼
Especie
   │
   ├──────────────► Farmacognosia
   │                    │
   │                    ▼
   │               Droga vegetal
   │
   ├──────────────► Fitoquímica
   │                    │
   │                    ▼
   │                 Compuestos
   │                    │
   │                    ▼
   ├──────────────► Farmacología
   │                    │
   │                    ▼
   │                 Actividades
   │
   ├──────────────► Etnobotánica
   │                    │
   │                    ▼
   │             Usos tradicionales
   │
   ├──────────────► Uso Terapéutico
   │                    │
   │                    ▼
   │               Indicaciones
   │
   ├──────────────► Seguridad
   │
   └──────────────► Regulación

Todas las afirmaciones
          │
          ▼
       Evidencia
          │
          ▼
      Procedencia
```

Este esquema es únicamente conceptual.

El catálogo formal de entidades y relaciones será responsabilidad de ADM-004.

---

# 19. Separaciones Conceptuales Obligatorias

El modelo deberá preservar, como mínimo, las siguientes separaciones:

```text
Taxón ≠ Droga vegetal
```

```text
Parte vegetal ≠ Droga vegetal
```

```text
Compuesto químico ≠ Perfil fitoquímico
```

```text
Compuesto químico ≠ Clasificación metabólica
```

```text
Marcador químico ≠ Criterio de calidad
```

```text
Uso tradicional ≠ Indicación terapéutica validada
```

```text
Historia de uso ≠ Evidencia clínica
```

```text
Actividad farmacológica ≠ Estudio que la investiga
```

```text
Resultado experimental ≠ Propiedad confirmada
```

```text
Indicación terapéutica ≠ Evidencia clínica
```

```text
Señal de seguridad ≠ Riesgo clínicamente confirmado
```

```text
Criterio de calidad ≠ Farmacopea que lo establece
```

```text
Fuente ≠ Verdad científica
```

```text
Procedencia ≠ Dominio temático
```

Estas separaciones deberán mantenerse en ADM-004 y en los estándares posteriores.

---

# 20. Extensibilidad de los Dominios

La arquitectura de dominios deberá permitir evolución progresiva.

Podrán incorporarse en el futuro:

- Nuevos subdominios.
- Nuevas especializaciones.
- Nuevos tipos de conocimiento.
- Nuevas áreas científicas.

La incorporación de un nuevo dominio independiente deberá justificarse por:

1. Existencia de una responsabilidad conceptual diferenciada.
2. Volumen recurrente de conocimiento.
3. Fuentes suficientemente identificables.
4. Necesidad de evitar mezcla con dominios existentes.
5. Valor para la arquitectura general del Atlas.

No deberá crearse un dominio únicamente porque un tema pueda existir conceptualmente.

---

# 21. Automatización y Dominios

Los agentes y procesos automáticos podrán descubrir y proponer información perteneciente a cualquiera de los dominios definidos.

Sin embargo:

```text
Información encontrada
        │
        ▼
Clasificación propuesta
        │
        ▼
Dominio / Subdominio
        │
        ▼
Procedencia preservada
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

La automatización no deberá:

- Inventar información ausente.
- Completar elementos no documentados mediante inferencia no autorizada.
- Transformar evidencia preclínica en eficacia clínica.
- Transformar un uso tradicional en indicación clínica.
- Transformar un resultado experimental en propiedad confirmada.
- Transferir propiedades automáticamente entre especies.
- Convertir información externa en conocimiento aprobado sin gobernanza.
- Eliminar contradicciones.
- Perder la procedencia original.

---

# 22. Responsabilidades por Dominio

| Dominio | Responsabilidad principal |
|---|---|
| Botánica | Identidad, clasificación, descripción y contexto biológico de la planta. |
| Farmacognosia | Identidad, autenticidad y calidad de la droga vegetal. |
| Fitoquímica | Composición, clasificación, distribución, variabilidad y biosíntesis química. |
| Etnobotánica y Uso Tradicional | Contexto histórico, cultural y tradicional del uso de plantas. |
| Farmacología | Actividades biológicas, efectos y mecanismos. |
| Evidencia Científica y Clínica | Estudios y evidencia que sustentan, limitan o contradicen afirmaciones. |
| Uso Terapéutico | Aplicaciones clínicas o terapéuticas reconocidas, propuestas o investigadas. |
| Seguridad y Toxicología | Riesgos, toxicidad, contraindicaciones, interacciones y condiciones de seguridad. |
| Regulación y Farmacopeas | Contexto oficial, normativo, farmacopéico y regulatorio. |
| Procedencia | Trazabilidad transversal del origen y contexto del conocimiento. |

---

# 23. Dependencias Arquitectónicas

ADM-003 depende principalmente de:

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
   │
   ▼
ADM-003
Dominios de Conocimiento del Atlas
```

ADM-003 constituirá una entrada directa para:

```text
ADM-003
Dominios de Conocimiento
        │
        ▼
ADM-004
Modelo de Información
        │
        ▼
Entidades
Atributos
Relaciones
        │
        ▼
Estándares
        │
        ▼
Implementación
```

---

# 24. Restricciones Arquitectónicas

La evolución del conocimiento deberá respetar las siguientes restricciones:

- Los dominios representan áreas conceptuales y no estructuras físicas de almacenamiento.
- La existencia de un subdominio no obliga a documentarlo para todas las entidades.
- La ausencia de datos no deberá completarse mediante inferencia automática.
- Toda afirmación deberá poder mantener procedencia.
- Las contradicciones deberán conservarse.
- La evidencia deberá permanecer diferenciada del conocimiento que sustenta.
- Un uso tradicional no deberá convertirse automáticamente en indicación terapéutica.
- Un resultado preclínico no deberá convertirse automáticamente en eficacia clínica.
- No existirá herencia automática de propiedades entre niveles taxonómicos.
- La especie continuará siendo la unidad biológica principal para la documentación fitoterapéutica.
- Fuentes y Procedencia constituirán una capa transversal.
- No existirá una fuente externa universal para todos los tipos de conocimiento.
- La cobertura regulatoria y farmacopéica será priorizada y progresiva.
- La automatización deberá preservar identidad, contexto, evidencia y procedencia.
- Los campos, atributos y relaciones formales deberán definirse en ADM-004.
- Las decisiones tecnológicas deberán respetar ADR-004.

---

# 25. Evolución del Modelo

La secuencia arquitectónica será:

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
Dominios de Conocimiento
        │
        ▼
ADM-004
Modelo de Información
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

ADM-003 deberá evolucionar únicamente cuando exista una necesidad conceptual suficientemente justificada.

La incorporación de nuevos contenidos dentro de un dominio existente no requerirá modificar este documento mientras no cambie la arquitectura conceptual del dominio.

---

# 26. Referencias

- GOV-001 — Constitución del Atlas de Fitoterapia.
- ADM-001 — Arquitectura General del Atlas de Fitoterapia.
- ADM-002 — Arquitectura del Modelo de Conocimiento.
- ADR-002 — Sistema de Identificación Única.
- ADR-003 — Jerarquía Normativa.
- ADR-004 — Arquitectura antes que Implementación.
- ADR-005 — Modelo Híbrido del Conocimiento.

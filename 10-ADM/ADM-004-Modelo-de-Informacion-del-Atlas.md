---
id: ADM-004
title: Modelo de Información del Atlas
version: 1.0.0
status: Approved
type: ADM
created: 2026-08-25
updated: 2026-08-25
author: Proyecto Atlas de Fitoterapia
tags:
  - architecture
  - knowledge
  - information-model
  - entities
  - relationships
  - evidence
  - provenance
---

# Modelo de Información del Atlas

## 1. Propósito

Definir el modelo conceptual de información mediante el cual el Atlas de Fitoterapia representará entidades, relaciones, afirmaciones, evidencia, fuentes, procedencia, clasificaciones e información contextual de forma estructurada, trazable, gobernada y extensible.

Este documento desarrolla la arquitectura establecida por ADM-002 y los dominios de conocimiento definidos por ADM-003.

ADM-004 establece principalmente:

- Los tipos iniciales de entidades reconocidos por el Atlas.
- Las responsabilidades conceptuales de dichas entidades.
- Las principales relaciones entre ellas.
- Los elementos que deberán representarse mediante clasificaciones o información contextual y no mediante entidades independientes.
- La representación conceptual de afirmaciones y evidencia.
- La función de las fuentes.
- La preservación de procedencia.
- El manejo de identificadores externos.
- Los estados de gobernanza y soporte científico.
- Las cardinalidades conceptuales iniciales.
- Los principios para la evolución futura del modelo.

ADM-004 define **qué información puede representar el Atlas y cómo se conecta conceptualmente**.

No define todavía:

- Base de datos.
- Motor de grafos.
- RDF.
- OWL.
- JSON Schema.
- YAML Schema.
- SQL.
- GraphQL.
- APIs.
- Estructura física de archivos.
- Estructura definitiva de carpetas.
- Índices.
- Claves físicas.
- Estrategias de persistencia.
- Algoritmos de reconciliación.
- Reglas detalladas de extracción automática.
- Implementaciones concretas de inteligencia artificial.

Por tanto:

```text
ADM-004
= modelo conceptual de información

Implementación física
= decisión posterior
```

---

## 2. Alcance

El modelo comprende información perteneciente a los dominios definidos por ADM-003:

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

Fuentes y Procedencia permanecen como componentes transversales aplicables a todos los dominios.

El modelo reconoce diferentes clases de elementos:

```text
Modelo de Información
│
├── Entidades
├── Relaciones
├── Clasificaciones
├── Información contextual
├── Afirmaciones
├── Evidencia
├── Fuentes
├── Procedencia
└── Identificadores externos
```

No todo concepto documentado por el Atlas deberá convertirse en una entidad independiente.

La decisión de otorgar identidad propia a un objeto deberá responder a una necesidad real de:

- Reutilización.
- Interconexión.
- Trazabilidad.
- Navegación.
- Gobernanza.
- Referenciación independiente.

---

## 3. Principios Generales del Modelo

### 3.1 Identidad independiente de la representación

Las entidades representan objetos del conocimiento y no archivos específicos.

Por tanto:

```text
Entidad ≠ Archivo

Entidad ≠ Página web

Entidad ≠ Monografía editorial

Entidad ≠ Fuente externa
```

Una entidad podrá ser representada en múltiples documentos o vistas sin perder su identidad.

---

### 3.2 Identidad interna del Atlas

Toda entidad gobernada deberá disponer de una identidad propia conforme al Sistema de Identificación Única establecido por ADR-002.

Conceptualmente:

```text
Objeto gobernado
      │
      ▼
   ID Atlas
      │
      ▼
    Entidad
```

Los identificadores provenientes de sistemas externos facilitarán reconciliación e interoperabilidad, pero no sustituirán la identidad del Atlas.

Por tanto:

```text
ID externo ≠ ID Atlas
```

---

### 3.3 Cobertura no obligatoria

La existencia de una entidad, relación, atributo, clasificación o bloque de información en este modelo no obliga a que todos los objetos del Atlas dispongan de dicha información.

Un elemento deberá documentarse únicamente cuando exista información:

- Pertinente.
- Aplicable.
- Suficientemente sustentada.
- Trazable.

Por tanto:

```text
Existe información pertinente
        │
        ▼
   se documenta

No existe información
        │
        ▼
   no se inventa
```

La ausencia de información no deberá completarse mediante inferencia automática.

---

### 3.4 Contexto antes que generalización

El Atlas deberá conservar el contexto específico en el que una propiedad, observación, actividad, composición, efecto o resultado haya sido documentado.

Por ejemplo:

```text
Propiedad observada en un preparado vegetal
              │
              X
              ▼
No implica automáticamente
la misma propiedad para todo el taxón
```

De igual forma, la presencia de un compuesto en una parte vegetal no permitirá atribuir automáticamente ese compuesto a todas las partes del organismo.

---

### 3.5 No herencia automática de propiedades

La pertenencia taxonómica no generará herencia automática de conocimiento:

- Fitoquímico.
- Farmacológico.
- Terapéutico.
- Clínico.
- Toxicológico.
- Etnobotánico.
- Regulatorio.

La existencia de información para una especie no permitirá transferirla automáticamente:

- A otras especies del mismo género.
- Al género completo.
- A la familia.
- A niveles taxonómicos relacionados.

Toda afirmación deberá conservar su propio contexto, evidencia y procedencia.

---

### 3.6 Separación entre conocimiento y evidencia

El conocimiento representado y los objetos que lo sustentan deberán mantenerse conceptualmente separados.

```text
Conocimiento
→ expresa qué se afirma

Evidencia
→ expresa qué sustenta, limita,
  contextualiza o contradice
  lo afirmado
```

---

### 3.7 Separación entre gobernanza y soporte científico

El estado administrativo o editorial de una afirmación no será equivalente al grado de soporte científico que ésta posea.

Por tanto:

```text
Estado de gobernanza
≠
Estado científico o de soporte
```

---

### 3.8 Extensibilidad gobernada

El catálogo establecido por ADM-004 constituye el modelo inicial del Atlas y no deberá interpretarse como una ontología cerrada.

Podrán incorporarse nuevos:

- Tipos de entidad.
- Relaciones.
- Clasificaciones.
- Contextos.
- Tipos documentales.

cuando el crecimiento real del conocimiento demuestre su necesidad.

Dicha evolución deberá realizarse mediante los mecanismos de gobernanza correspondientes.

---

### 3.9 Cardinalidad flexible

Las cardinalidades serán flexibles por defecto y únicamente se restringirán cuando:

- La naturaleza conceptual del objeto lo exija.
- Exista una regla científica aplicable.
- Una decisión de arquitectura lo determine.
- Una regla de gobernanza lo establezca.

No se impondrá unicidad artificial cuando el conocimiento pueda ser:

- Compuesto.
- Multifuente.
- Multimaterial.
- Multicomponente.
- Contextual.

---

## 4. Estructura General del Modelo

Conceptualmente:

```text
Dominios de conocimiento
        │
        ▼
     Entidades
        │
        ▼
    Relaciones
        │
        ▼
Conocimiento estructurado
        │
        ▼
    Afirmaciones
        │
        ▼
     Evidencia
        │
        ▼
      Fuentes
        │
        ▼
    Procedencia
```

Estos componentes constituyen el núcleo conceptual que posteriormente podrá materializarse como grafo de conocimiento.

---

# 5. Entidades Biológicas y Farmacognósticas

## 5.1 Taxón

Taxón representa una entidad biológica clasificada.

El Atlas utilizará una sola entidad conceptual `Taxón` para representar los diferentes niveles de la jerarquía taxonómica.

No se crearán entidades distintas denominadas Familia, Género o Especie.

En su lugar:

```text
Taxón
└── Nivel taxonómico
```

### 5.1.1 Conceptos taxonómicos

**Taxón:** entidad biológica clasificada.

**Nivel taxonómico:** posición que ocupa un taxón dentro de la clasificación.

**Jerarquía taxonómica:** secuencia ordenada de niveles taxonómicos.

La jerarquía principal será:

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

Familia constituye el nivel superior documentado obligatoriamente por la arquitectura del Atlas.

La especie continúa siendo la unidad biológica principal para la documentación fitoterapéutica.

### 5.1.2 Información conceptual del Taxón

Un Taxón podrá contener, cuando corresponda:

```text
Taxón
├── ID Atlas
├── nombre científico
├── autoría botánica
├── sinónimos
├── nivel taxonómico
├── estatus taxonómico
├── identificadores externos
└── procedencia
```

La lista anterior no constituye todavía un esquema físico obligatorio.

### 5.1.3 Relaciones principales

```text
Taxón
├── pertenece a ──► Taxón
├── posee parte ──► Parte vegetal
└── origina ──────► Droga vegetal
```

La relación `pertenece a` representará principalmente la jerarquía taxonómica inmediata.

Ejemplo:

```text
Especie ── pertenece a ──► Género

Género ── pertenece a ──► Familia
```

---

## 5.2 Parte vegetal

Parte vegetal representa una estructura vegetal genérica y reutilizable.

Ejemplos:

```text
Raíz
Rizoma
Tallo
Corteza
Hoja
Flor
Fruto
Semilla
```

La entidad no deberá duplicarse por cada taxón.

Por tanto:

```text
Rizoma
→ Parte vegetal reutilizable
```

y no:

```text
Rizoma de Curcuma longa
→ nueva entidad automática
```

La especificidad se establecerá mediante relaciones.

Conceptualmente:

```text
Taxón
  │
  └── posee parte ──► Parte vegetal
```

La Parte vegetal podrá participar posteriormente en relaciones farmacognósticas, fitoquímicas, etnobotánicas y científicas.

---

## 5.3 Droga vegetal

Droga vegetal representa un material vegetal definido utilizado o reconocido dentro de un contexto:

- Medicinal.
- Farmacognóstico.
- Tradicional.
- Terapéutico.
- Científico.
- Farmacopéico.
- Regulatorio.

Deberá mantenerse conceptualmente separada de Taxón y Parte vegetal.

```text
Taxón
   │
   ▼
Parte vegetal
   │
   ▼
Droga vegetal
```

Esto no implica que cada elemento sea una transformación física del anterior, sino que representan niveles conceptualmente diferentes del conocimiento.

Una droga vegetal podrá mantener información como:

```text
Droga vegetal
├── ID Atlas
├── denominación
├── Taxón o Taxones de origen
├── Parte o Partes vegetales de origen
├── estado o forma del material
├── perfil fitoquímico
├── identificadores externos
└── procedencia
```

### 5.3.1 Estado o forma del material

Características como:

- Fresco.
- Seco.
- Entero.
- Cortado.
- Triturado.
- Pulverizado.

serán características de la droga vegetal y no entidades independientes.

### 5.3.2 Relaciones mínimas

```text
Droga vegetal
├── procede de ──► 1..n Taxón
└── procede de ──► 1..n Parte vegetal
```

Una droga vegetal podrá tener más de un taxón o parte vegetal de origen cuando exista una razón documental, científica, tradicional o regulatoria que lo sustente.

---

# 6. Preparado Vegetal

Preparado vegetal constituye un elemento transversal del modelo.

No constituye por sí mismo un dominio temático independiente.

Se representará como objeto con identidad propia cuando un preparado concreto necesite ser:

- Diferenciado.
- Reutilizado.
- Relacionado con estudios.
- Asociado con evidencia.
- Vinculado con usos terapéuticos.
- Caracterizado fitoquímicamente.
- Documentado mediante monografías.
- Evaluado desde seguridad.

Podrá representar, cuando resulte pertinente:

```text
Extracto
Tintura
Infusión
Decocción
Extracto estandarizado
Otros preparados definidos
```

La existencia de una preparación descrita de forma tradicional no obliga automáticamente a crear una entidad Preparado vegetal.

Conceptualmente:

```text
Preparación tradicional simple
→ puede permanecer como contexto
  del Uso tradicional

Preparado definido que necesita
identidad propia
→ Preparado vegetal
```

### 6.1 Relaciones

```text
Preparado vegetal
├── deriva de ──► 1..n Droga vegetal
├── deriva de ──► 0..n Preparado vegetal
├── contiene / presenta ──► Compuesto químico
├── estudiado en ─────────► Estudio
├── asociado con ─────────► Uso terapéutico
└── documentado en ───────► Monografía
```

La relación entre preparados podrá utilizarse para representar cadenas como:

```text
Droga vegetal
      │
      ▼
   Extracto
      │
      ▼
Extracto estandarizado
```

sin imponer todavía un modelo tecnológico de procesamiento.

La evidencia obtenida para un preparado específico no deberá transferirse automáticamente a:

- La droga vegetal completa.
- Todo preparado derivado de la misma droga.
- El Taxón completo.

---

# 7. Entidades Fitoquímicas

## 7.1 Compuesto químico

Compuesto químico representa una sustancia química individual identificable y reutilizable dentro del conocimiento del Atlas.

Podrá relacionarse con:

- Drogas vegetales.
- Preparados vegetales.
- Partes vegetales.
- Actividades biológicas.
- Mecanismos de acción.
- Estudios.
- Usos terapéuticos.
- Interacciones.
- Seguridad.
- Marcadores de calidad.

Información conceptual inicial:

```text
Compuesto químico
├── ID Atlas
├── nombre preferido
├── sinónimos
├── identificadores externos
├── tipo de metabolito
├── pertenece a ──► Clase química
└── procedencia
```

ADM-004 no obliga inicialmente a incorporar:

- Fórmula molecular.
- Masa molecular.
- Propiedades fisicoquímicas extensas.

Estos elementos podrán incorporarse posteriormente si el crecimiento real del Atlas demuestra su necesidad.

### 7.1.1 Tipo de metabolito

Tipo de metabolito será una clasificación y no una entidad.

Inicialmente podrá representar:

```text
Metabolito primario
Metabolito secundario
```

Si la clasificación no se encuentra suficientemente documentada, deberá permanecer ausente.

---

## 7.2 Clase química

Clase química será una entidad reutilizable destinada a representar agrupaciones químicas con utilidad para:

- Clasificación.
- Navegación.
- Organización.
- Reutilización.
- Relaciones jerárquicas.

Podrá contener:

```text
Clase química
├── ID Atlas
├── nombre preferido
├── sinónimos
├── definición
└── procedencia
```

La definición deberá documentarse únicamente cuando exista una fuente pertinente.

### 7.2.1 Relaciones

```text
Compuesto químico
   │
   └── pertenece a ──► Clase química
```

y:

```text
Clase química
   │
   └── subclase de ──► Clase química
```

Esto permitirá jerarquías como:

```text
Compuestos fenólicos
        │
        ▼
    Polifenoles
        │
        ▼
   Curcuminoides
```

---

## 7.3 Perfil fitoquímico

Perfil fitoquímico no será una entidad independiente.

Representará un conjunto estructurado de información acerca de la composición química documentada para un material bajo un contexto determinado.

Se asociará principalmente con:

```text
Droga vegetal
Preparado vegetal
```

y podrá, cuando resulte necesario, asociarse con otros materiales vegetales.

Podrá incluir:

- Compuestos detectados.
- Clases químicas.
- Metabolitos primarios.
- Metabolitos secundarios.
- Marcadores químicos.
- Concentraciones.
- Abundancias relativas.
- Variabilidad química.
- Información biosintética pertinente.

La concentración o abundancia de un compuesto no será considerada una propiedad intrínseca universal del compuesto.

Conceptualmente:

```text
Compuesto
      │
      ▼
presente en determinado
material y contexto
      │
      ▼
Concentración / abundancia
```

La información deberá conservar el contexto necesario para su interpretación.

---

# 8. Entidades Farmacológicas

## 8.1 Actividad biológica

Actividad biológica será una entidad reutilizable destinada a representar categorías de acción biológica.

Ejemplos:

```text
Actividad antiinflamatoria
Actividad antioxidante
Actividad antimicrobiana
Actividad citotóxica
```

Podrá contener:

```text
Actividad biológica
├── ID Atlas
├── nombre preferido
├── sinónimos
├── definición
└── procedencia
```

Una actividad biológica representa una categoría conceptual y no un resultado experimental concreto.

Por tanto:

```text
Actividad biológica
≠
Efecto observado
```

---

## 8.2 Mecanismo de acción

Mecanismo de acción será una entidad reutilizable destinada a representar explicaciones acerca de cómo ocurre una acción biológica o farmacológica.

Podrá contener:

```text
Mecanismo de acción
├── ID Atlas
├── nombre preferido
├── sinónimos
├── definición
└── procedencia
```

Conceptualmente:

```text
Actividad biológica
= qué tipo de acción ocurre

Mecanismo de acción
= cómo ocurre

Efecto observado
= qué cambio concreto fue medido
```

Un mecanismo no deberá considerarse conocido únicamente porque se haya documentado una actividad.

### 8.2.1 Relaciones farmacológicas

```text
Compuesto químico
├── asociado con ──► Actividad biológica
└── actúa mediante ──► Mecanismo de acción
```

También podrán existir:

```text
Droga vegetal
   └── asociada con ──► Actividad biológica

Preparado vegetal
   └── asociado con ──► Actividad biológica
```

Cuando exista información suficiente:

```text
Actividad biológica
   └── explicada por ──► Mecanismo de acción
```

La relación deberá conservar evidencia y contexto suficientes.

---

## 8.3 Efecto observado

Efecto observado no será una entidad independiente por defecto.

Representará información contextual acerca de un cambio medido u observado dentro de:

- Un estudio.
- Un ensayo.
- Un experimento.
- Una exposición.
- Otra observación documentada.

Ejemplo:

```text
Actividad:
antiinflamatoria

Efecto observado:
reducción de TNF-α bajo
condiciones experimentales específicas
```

Por tanto:

```text
Resultado experimental
≠
Propiedad farmacológica confirmada
```

---

## 8.4 Farmacodinámica

Farmacodinámica no será una entidad.

Constituirá información estructurada contextual cuando esté disponible.

Podrá incluir:

- Relación dosis-respuesta.
- Potencia.
- Eficacia.
- Afinidad.
- Parámetros farmacodinámicos pertinentes.

La existencia de esta categoría no obliga a documentarla para todos los objetos farmacológicos.

---

## 8.5 Farmacocinética

Farmacocinética no será una entidad.

Constituirá información estructurada contextual.

Podrá incluir, cuando exista información:

- Absorción.
- Distribución.
- Metabolismo.
- Eliminación.
- Biodisponibilidad.
- Vida media.
- Otros parámetros pertinentes.

La información farmacocinética deberá conservar contexto relativo, cuando corresponda, a:

- Compuesto.
- Preparado.
- Dosis.
- Vía de administración.
- Población.
- Especie experimental.
- Formulación.
- Diseño del estudio.

---

# 9. Uso Terapéutico

## 9.1 Uso terapéutico

Uso terapéutico será una entidad asociativa y contextual destinada a representar una aplicación contemporánea:

- Reconocida.
- Propuesta.
- Investigada.
- Documentada.

de un objeto fitoterapéutico frente a una determinada condición de salud.

Podrá relacionarse principalmente con:

- Droga vegetal.
- Preparado vegetal.
- Compuesto químico.

La asociación directa con un Taxón deberá utilizarse únicamente cuando la fuente realmente formule el conocimiento a ese nivel.

Conceptualmente:

```text
Objeto terapéutico
       │
       ▼
Uso terapéutico
       │
       ▼
Condición de salud
```

Podrá contener, cuando exista información:

```text
Uso terapéutico
├── ID Atlas
├── objeto terapéutico
├── Condición de salud
├── tipo o estatus del uso
├── población
├── dosis
├── frecuencia
├── vía
├── duración
├── forma de uso
├── condiciones de uso
└── procedencia
```

La lista anterior representa información conceptual y no implica obligatoriedad universal.

### 9.1.1 Estatus del uso terapéutico

El estatus será una clasificación y no una entidad.

Podrá distinguir, entre otros contextos:

- Uso oficialmente reconocido.
- Uso respaldado por monografía científica o técnica.
- Uso clínicamente investigado.

La clasificación deberá evolucionar mediante estándares posteriores.

### 9.1.2 Reglas

```text
Uso terapéutico
≠
Evidencia clínica
```

```text
Uso terapéutico
≠
Uso tradicional
```

```text
Resultado de ensayo clínico
≠
Indicación terapéutica oficialmente reconocida
```

La evidencia correspondiente deberá conservarse de forma independiente.

---

## 9.2 Condición de salud

Condición de salud será una entidad reutilizable destinada a representar condiciones clínicas, síntomas, trastornos, enfermedades u otros estados de salud pertinentes para el Atlas.

Podrá utilizarse transversalmente en:

- Uso Terapéutico.
- Seguridad.
- Evidencia Científica.
- Uso Tradicional.
- Interacciones.

La condición deberá conservar una sola identidad reutilizable cuando el concepto sea el mismo.

Por ejemplo:

```text
Náusea
→ Condición de salud
```

Cuando aparezca en contexto de seguridad:

```text
Preparado X
   │
   └── asociado con evento adverso ──► Náusea
```

No deberá crearse una entidad adicional denominada `Evento adverso: Náusea`.

---

# 10. Seguridad y Toxicología

## 10.1 Eventos adversos

Evento adverso no constituye una entidad independiente.

Se representará mediante una relación contextual entre un objeto de exposición y una Condición de salud.

Conceptualmente:

```text
Objeto de exposición
      │
      └── asociado con evento adverso
                     │
                     ▼
             Condición de salud
```

El contexto podrá incorporar:

- Dosis.
- Frecuencia.
- Severidad.
- Población.
- Exposición.
- Temporalidad.
- Evidencia.
- Procedencia.

---

## 10.2 Contraindicación

Contraindicación no será una entidad independiente.

Se representará como relación o afirmación contextual.

Conceptualmente:

```text
Objeto
  │
  └── contraindicado en ──► Condición / contexto
```

Una contraindicación deberá entenderse como una situación documentada en la que el uso de un objeto debe evitarse conforme a la fuente aplicable.

La existencia de una contraindicación no deberá extrapolarse a otros objetos relacionados sin evidencia propia.

---

## 10.3 Precaución

Precaución no será una entidad independiente.

Se representará mediante relación o afirmación contextual.

```text
Objeto
  │
  └── requiere precaución en ──► Condición / contexto
```

Precaución representará situaciones que requieran:

- Evaluación adicional.
- Vigilancia.
- Seguimiento.
- Consideración especial.

sin implicar necesariamente contraindicación absoluta.

---

## 10.4 Señales de seguridad y toxicidad

Toxicidad observada y señal de seguridad no serán entidades independientes por defecto.

Representarán información contextual o estados de una afirmación.

Una señal de seguridad no deberá interpretarse automáticamente como riesgo clínicamente confirmado.

Por tanto:

```text
Señal de seguridad
≠
Riesgo confirmado
```

---

## 10.5 Interacción

Interacción será una entidad contextual con identidad propia cuando sea necesario representar una relación estructurada entre dos o más participantes.

Podrá contener:

```text
Interacción
├── ID Atlas
├── participante A
├── participante B
├── tipo
├── mecanismo
├── efecto
├── severidad
├── recomendación
├── evidencia
└── procedencia
```

Los participantes podrán incluir:

- Droga vegetal.
- Preparado vegetal.
- Compuesto químico.
- Otra planta.
- Alimento.
- Medicamento.
- Otro objeto pertinente.

ADM-004 no incorpora `Medicamento` como entidad propia del Atlas en esta versión.

Cuando un participante se encuentre fuera del alcance principal del modelo, podrá utilizarse una referencia controlada a un objeto externo.

---

# 11. Evidencia Científica y Clínica

## 11.1 Estudio

Estudio será una entidad científica destinada a representar de forma estructurada una investigación.

No deberá limitarse a funcionar como simple referencia bibliográfica.

Podrá contener, cuando exista información:

```text
Estudio
├── ID Atlas
├── identificación
├── tipo / diseño
├── objetivo
├── población o modelo
├── intervención / exposición
├── comparador
├── variables o desenlaces relevantes
├── resultados
├── limitaciones
├── conclusiones de los autores
├── relación con afirmaciones
└── procedencia
```

El propósito será conservar información suficiente para interpretar y reutilizar científicamente el estudio sin reproducir innecesariamente la publicación completa.

### 11.1.1 Tipo y diseño de estudio

Tipo y diseño serán clasificaciones y no entidades independientes.

Podrán comprender inicialmente:

```text
Estudios primarios
├── in vitro
├── ex vivo
├── in vivo animal
├── observacional
└── ensayo clínico

Estudios secundarios
└── revisión sistemática
```

Una revisión sistemática podrá incorporar metaanálisis.

El metaanálisis podrá representarse como método o característica del estudio cuando corresponda y no como entidad independiente.

### 11.1.2 Resultados y conclusiones

Resultados y conclusiones serán elementos diferentes.

```text
Resultado
= observación o medición obtenida

Conclusión
= interpretación realizada por los autores
```

Por tanto:

```text
Resultado
≠
Conclusión
```

y:

```text
Conclusión de los autores
≠
Verdad científica
```

Las conclusiones deberán permanecer atribuidas a sus autores o fuente correspondiente.

---

## 11.2 Publicación

Publicación será una entidad documental destinada a representar el vehículo mediante el cual se comunica conocimiento científico.

Podrá incluir:

```text
Publicación
├── ID Atlas
├── título
├── autores
├── año
├── revista o medio
├── DOI
├── PMID
├── otros identificadores externos
└── procedencia
```

Un estudio y una publicación representan conceptos distintos.

Por tanto:

```text
Estudio ≠ Publicación
```

Un estudio podrá producir múltiples publicaciones.

Una publicación podrá describir uno o varios estudios o elementos de conocimiento.

### 11.2.1 Relación

```text
Estudio
   │
   └── reportado en ──► Publicación
```

Las cardinalidades serán flexibles.

---

## 11.3 Síntesis de evidencia

Síntesis de evidencia no será una entidad independiente en el modelo inicial.

Las revisiones sistemáticas serán representadas mediante la entidad Estudio y clasificadas como estudios secundarios.

Cuando una revisión incorpore metaanálisis, éste se registrará como característica metodológica correspondiente.

---

# 12. Etnobotánica y Uso Tradicional

## 12.1 Uso tradicional

Uso tradicional será la entidad principal para representar conocimiento acerca de prácticas tradicionales o históricas documentadas para una planta, parte vegetal o material relacionado.

Podrá incluir cuando exista información:

```text
Uso tradicional
├── ID Atlas
├── Taxón u objeto vegetal asociado
├── Parte vegetal utilizada
├── finalidad tradicional
├── preparación tradicional
├── vía tradicional
├── contexto cultural
├── contexto histórico
├── Comunidad / pueblo
├── Sistema tradicional
├── Región
└── procedencia
```

La ausencia de información sobre comunidad, sistema tradicional o región no invalidará el registro de un uso tradicional suficientemente documentado.

Por tanto:

```text
Uso tradicional
      │
      ├── Comunidad documentada
      │      → se registra
      │
      └── Comunidad no documentada
             → no se infiere
```

### 12.1.1 Regla de separación

```text
Uso tradicional
≠
Uso terapéutico validado
```

La documentación de un uso tradicional no deberá interpretarse automáticamente como demostración:

- Farmacológica.
- Clínica.
- Terapéutica.
- Regulatoria.

---

## 12.2 Comunidad / pueblo

Comunidad / pueblo será una entidad opcional.

Se utilizará únicamente cuando una fuente documente suficientemente un grupo humano concreto asociado con determinado conocimiento tradicional.

No será obligatorio asignar comunidad a todos los usos tradicionales.

---

## 12.3 Sistema tradicional

Sistema tradicional será una entidad opcional.

Podrá representar sistemas médicos o tradiciones suficientemente identificables y documentadas.

No deberá inferirse la pertenencia de una práctica a un sistema tradicional únicamente por su origen geográfico.

---

## 12.4 Región

Región será una entidad reutilizable opcional cuando resulte necesario representar un contexto geográfico de forma independiente.

Podrá utilizarse en:

- Etnobotánica.
- Distribución botánica.
- Procedencia.
- Regulación.
- Otros contextos cuando corresponda.

Podrá permitir relaciones jerárquicas entre regiones en desarrollos posteriores.

---

## 12.5 Preparación tradicional

Preparación tradicional no será una entidad independiente por defecto.

Será información contextual del Uso tradicional.

Podrá evolucionar hacia identidad propia únicamente cuando exista una necesidad demostrada de reutilización o interconexión.

---

# 13. Regulación y Farmacopeas

## 13.1 Organización

Organización será una entidad reutilizable para representar instituciones u organizaciones relevantes para distintos dominios.

Podrá incluir:

```text
Organización
├── ID Atlas
├── nombre
├── acrónimo
├── identificadores externos
└── procedencia
```

El rol de una Organización será contextual y no constituirá una entidad independiente.

Podrá clasificarse según corresponda como:

- Organización científica.
- Organización internacional.
- Autoridad regulatoria.
- Autoridad sanitaria.
- Organización técnica.
- Otro rol pertinente.

Una misma Organización podrá desempeñar diferentes funciones.

---

## 13.2 Farmacopea

Farmacopea será una entidad documental y normativa reutilizable.

Podrá incluir:

```text
Farmacopea
├── ID Atlas
├── nombre
├── abreviatura
├── organización responsable
├── jurisdicción
├── edición / versión
└── procedencia
```

La existencia de una edición nueva no deberá eliminar automáticamente el conocimiento histórico correspondiente a versiones anteriores cuando éste resulte relevante.

---

## 13.3 Monografía

Monografía será una entidad documental única.

No se crearán entidades distintas para cada categoría de monografía.

En su lugar se utilizará una clasificación:

```text
Tipo de monografía
├── Farmacopéica
├── Regulatoria / terapéutica
└── Científica / técnica
```

Las relaciones podrán incluir:

```text
Monografía
├── emitida por ──► Organización
├── pertenece a ──► Farmacopea
└── documenta ────► Objeto del Atlas
```

No toda monografía deberá pertenecer a una Farmacopea.

Por tanto:

```text
Monografía farmacopéica
→ puede pertenecer a Farmacopea

Monografía científica o técnica
→ no necesariamente
```

---

## 13.4 Disposición normativa

Disposición normativa será una entidad documental destinada a representar instrumentos regulatorios concretos.

Podrá representar:

- Norma.
- Reglamento.
- Resolución.
- Disposición oficial.
- Documento regulatorio equivalente.

Podrá incluir, cuando corresponda:

```text
Disposición normativa
├── ID Atlas
├── identificación
├── versión
├── jurisdicción
├── organización emisora
├── vigencia
└── procedencia
```

Relaciones principales:

```text
Disposición normativa
├── emitida por ──► Organización
└── regula ───────► Objeto del Atlas
```

---

## 13.5 Estatus regulatorio

Estatus regulatorio no será una entidad independiente.

Representará información contextual dependiente de elementos como:

- Jurisdicción.
- Organización.
- Fecha.
- Disposición aplicable.
- Objeto regulado.

Por tanto:

```text
Estatus regulatorio
≠
Propiedad universal del objeto
```

---

# 14. Afirmación

Afirmación será una entidad ligera de gobernanza y trazabilidad.

Su función principal será formalizar que determinado conocimiento o relación existe dentro del modelo gobernado.

No deberá convertirse en un contenedor universal que duplique el contexto especializado almacenado en cada dominio.

Conceptualmente:

```text
Dominio
→ conserva conocimiento
  y contexto especializado

Afirmación
→ formaliza y gobierna
  ese conocimiento
```

Una Afirmación podrá contener conceptualmente:

```text
Afirmación
├── ID Atlas
├── objeto, valor o relación afirmada
├── estado de gobernanza
├── estado científico / soporte
├── evidencia asociada
└── procedencia
```

La forma física exacta deberá determinarse posteriormente.

Una Afirmación no será equivalente automáticamente a conocimiento verdadero o definitivamente aceptado.

Por tanto:

```text
Afirmación ≠ Verdad científica
```

---

# 15. Evidencia

Evidencia no será una entidad independiente.

Se define como:

> Relación trazable mediante la cual una o más fuentes aportan soporte, limitación, contextualización o contradicción respecto de una afirmación del Atlas.

Conceptualmente:

```text
Afirmación
├── sustentada por ──────► Fuente
├── limitada por ────────► Fuente
├── contradicha por ─────► Fuente
└── contextualizada por ─► Fuente
```

Por tanto:

```text
Estudio
= objeto científico

Publicación
= objeto documental

Monografía
= objeto documental o regulatorio

Farmacopea
= objeto normativo

Evidencia
= papel que uno o varios
  de estos objetos desempeñan
  respecto de una afirmación
```

Una misma Afirmación podrá estar asociada simultáneamente con:

- Evidencia favorable.
- Evidencia limitada.
- Evidencia contradictoria.
- Diferentes niveles o contextos de soporte.

La arquitectura deberá preservar estas diferencias.

---

# 16. Fuente

Fuente será una categoría abstracta transversal que engloba los objetos capaces de funcionar como origen documentado del conocimiento.

No constituye necesariamente una entidad concreta adicional.

Podrán actuar como Fuente:

```text
Estudio
Publicación
Monografía
Farmacopea
Disposición normativa
Organización
Registro externo
Base de datos
Otro objeto autorizado
```

Por tanto:

```text
Fuente
= categoría abstracta
  que agrupa objetos
  capaces de originar conocimiento
```

El objeto concreto conservará su propia identidad.

No deberá crearse automáticamente una segunda entidad Fuente que duplique al objeto original.

---

# 17. Procedencia

Procedencia será un componente transversal destinado a conservar la trazabilidad del origen del conocimiento.

Podrá aplicarse a:

- Entidades.
- Relaciones.
- Afirmaciones.
- Valores.
- Datos contextuales.
- Resultados.
- Clasificaciones cuando resulte necesario.

Podrá conservar, según disponibilidad:

```text
Procedencia
├── fuente concreta
├── identificador externo
├── URL o referencia
├── edición / versión
├── fecha de consulta
├── fecha de incorporación
├── contexto de obtención
└── transformaciones relevantes
```

No todos los elementos serán obligatorios en todos los casos.

Se distinguirá cuando corresponda entre:

```text
URL de la fuente general

URL del registro específico

URL de la publicación original
```

La ausencia de URL pública no invalidará una fuente legítima.

### 17.1 Principio de trazabilidad

Todo conocimiento incorporado desde una fuente externa deberá conservar trazabilidad suficiente para determinar razonablemente:

```text
qué información se incorporó
        │
        ▼
de qué objeto o fuente provino
        │
        ▼
en qué contexto fue obtenida
```

Por tanto:

```text
Dato externo
≠
Dato anónimo
```

---

# 18. Autoridad de la Fuente

El Atlas no reconocerá una fuente única como autoridad universal para todos los tipos de información.

La autoridad deberá depender del tipo de conocimiento documentado.

Conceptualmente:

```text
Tipo de dato
│
├── Nomenclatura botánica
│      → fuente nomenclatural autorizada
│
├── Estatus taxonómico
│      → fuente taxonómica autorizada
│
├── Droga vegetal
│      → farmacopea o monografía aplicable
│
├── Compuesto químico
│      → repositorio químico autorizado
│
└── Evidencia científica
       → publicación o fuente científica
          correspondiente
```

La incorporación de información desde una fuente no implica aprobación científica automática.

Por tanto:

```text
Fuente aceptada
≠
Afirmación aprobada
```

---

# 19. Relaciones

Las relaciones representan vínculos semánticos explícitos entre objetos del conocimiento.

El Atlas utilizará un vocabulario controlado de relaciones.

Cada tipo de relación podrá definir conceptualmente:

```text
Relación
├── nombre
├── definición
├── tipo de origen permitido
├── tipo de destino permitido
└── reglas semánticas
```

No será necesario convertir cada tipo de relación en una entidad científica independiente.

### 19.1 Relación y afirmación

Una relación establece que determinado tipo de vínculo existe dentro del modelo.

Una instancia concreta de dicha relación podrá constituir una Afirmación gobernada.

Conceptualmente:

```text
Tipo de relación:

Compuesto químico
── pertenece a ──►
Clase química
```

Caso concreto:

```text
Curcumina
── pertenece a ──►
Curcuminoides
```

La existencia del caso concreto podrá ser gobernada mediante una Afirmación.

Por tanto:

```text
Relación
≠
Afirmación
```

---

## 19.2 Vocabulario inicial de relaciones

El vocabulario inicial podrá incluir:

```text
pertenece a
posee parte
procede de
deriva de
contiene
presenta
subclase de
asociado con
actúa mediante
explicada por
tiene uso terapéutico
se refiere a
participa en
estudia
reportado en
utiliza
documenta
pertenece a farmacopea
emitido por
regula
contraindicado en
requiere precaución en
asociado con evento adverso
sustentada por
limitada por
contradicha por
contextualizada por
```

Este catálogo no será cerrado.

Las nuevas relaciones deberán incorporarse mediante evolución gobernada.

---

# 20. Relaciones Biológicas y Farmacognósticas

Las relaciones principales serán:

```text
Taxón
├── pertenece a ──► Taxón
├── posee parte ──► Parte vegetal
└── origina ──────► Droga vegetal
```

y:

```text
Droga vegetal
├── procede de ──► Taxón
└── procede de ──► Parte vegetal
```

No deberán utilizarse relaciones redundantes cuando una sola relación semánticamente definida sea suficiente.

---

# 21. Relaciones Fitoquímicas

Las principales relaciones serán:

```text
Droga vegetal
└── contiene / presenta ──► Compuesto químico

Preparado vegetal
└── contiene / presenta ──► Compuesto químico

Compuesto químico
└── pertenece a ──► Clase química

Clase química
└── subclase de ──► Clase química
```

La relación directa:

```text
Taxón
── contiene ──►
Compuesto químico
```

deberá utilizarse únicamente cuando la fuente permita formular legítimamente el conocimiento a nivel del Taxón.

Se preferirá preservar la especificidad del material estudiado.

---

# 22. Relaciones Farmacológicas

Podrán incluir:

```text
Compuesto químico
├── asociado con ──► Actividad biológica
└── actúa mediante ──► Mecanismo de acción
```

```text
Droga vegetal
└── asociada con ──► Actividad biológica
```

```text
Preparado vegetal
└── asociado con ──► Actividad biológica
```

y cuando exista evidencia suficiente:

```text
Actividad biológica
└── explicada por ──► Mecanismo de acción
```

La existencia de una actividad no obliga a documentar un mecanismo.

---

# 23. Relaciones de Uso Terapéutico

Conceptualmente:

```text
Droga vegetal
Preparado vegetal
Compuesto químico
      │
      ▼
tiene uso terapéutico
      │
      ▼
Uso terapéutico
      │
      ▼
se refiere a
      │
      ▼
Condición de salud
```

Se deberá evitar atribuir automáticamente a un Taxón completo una evidencia que corresponda únicamente a una droga o preparado particular.

---

# 24. Relaciones de Seguridad

Podrán representarse:

```text
Objeto
── asociado con evento adverso ──► Condición de salud
```

```text
Objeto
── contraindicado en ──► Condición / contexto
```

```text
Objeto
── requiere precaución en ──► Condición / contexto
```

Las relaciones deberán conservar suficiente información de contexto para evitar interpretar una advertencia como propiedad universal cuando dependa de:

- Dosis.
- Población.
- Preparación.
- Ruta.
- Duración.
- Exposición.
- Interacción.
- Fuente.

---

# 25. Relaciones de Evidencia Científica

Estudio podrá relacionarse con múltiples objetos de conocimiento mediante una relación general:

```text
Estudio
── estudia ──►
Objeto de conocimiento
```

El objeto podrá ser, entre otros:

- Taxón.
- Droga vegetal.
- Preparado vegetal.
- Compuesto químico.
- Actividad biológica.
- Uso terapéutico.
- Condición de salud.
- Interacción.

No será obligatorio crear una relación distinta para cada tipo de objeto estudiado.

La relación documental principal será:

```text
Estudio
── reportado en ──►
Publicación
```

---

# 26. Relaciones Etnobotánicas

Uso tradicional podrá relacionarse con:

```text
Uso tradicional
├── asociado con ──► Taxón
├── utiliza ───────► Parte vegetal
├── asociado con ──► Comunidad / pueblo
├── asociado con ──► Sistema tradicional
├── localizado en ─► Región
└── relacionado con ──► Condición de salud
```

Salvo la identificación del objeto vegetal correspondiente, el resto de relaciones podrán ser opcionales cuando la fuente no proporcione suficiente información.

La relación con una Condición de salud conservará su naturaleza tradicional y no se convertirá automáticamente en Uso terapéutico.

---

# 27. Relaciones Regulatorias y Documentales

Podrán incluir:

```text
Monografía
├── emitida por ──► Organización
├── pertenece a ──► Farmacopea
└── documenta ────► Objeto del Atlas
```

```text
Farmacopea
└── emitida o mantenida por ──► Organización
```

```text
Disposición normativa
├── emitida por ──► Organización
└── regula ───────► Objeto del Atlas
```

La relación `pertenece a Farmacopea` sólo deberá utilizarse cuando corresponda.

---

# 28. Estado de Gobernanza

Estado de gobernanza será una clasificación controlada destinada a indicar en qué etapa de aceptación se encuentra una Afirmación.

Inicialmente:

```text
Estado de gobernanza
├── Propuesta
├── En revisión
└── Aprobada
```

### 28.1 Propuesta

La afirmación ha sido incorporada como candidata a formar parte del conocimiento gobernado, pero aún no ha completado el proceso de revisión correspondiente.

### 28.2 En revisión

La afirmación se encuentra sometida al proceso de validación aplicable.

### 28.3 Aprobada

La afirmación ha cumplido las reglas de gobernanza requeridas para incorporarse formalmente al conocimiento aprobado del Atlas.

Aprobada no significa científicamente definitiva.

---

# 29. Estado Científico o de Soporte

El estado científico representa cómo se comporta la evidencia disponible respecto de una Afirmación.

Inicialmente podrá comprender:

```text
Estado científico / soporte
├── Sustentada
├── Limitada
└── Contradicha
```

### 29.1 Sustentada

Existe evidencia pertinente que proporciona soporte a la afirmación bajo el contexto evaluado.

### 29.2 Limitada

Existe evidencia de soporte, pero presenta restricciones relevantes relacionadas con:

- Calidad.
- Cantidad.
- Diseño.
- Generalización.
- Consistencia.
- Contexto.
- Otras limitaciones pertinentes.

### 29.3 Contradicha

Existe evidencia relevante que se opone total o parcialmente a la afirmación.

Estos estados no deberán interpretarse necesariamente como mutuamente excluyentes en sentido científico.

Podrán coexistir fuentes en diferentes direcciones.

Por ejemplo:

```text
Afirmación
├── Estado de gobernanza:
│      Aprobada
│
└── Evidencia:
       ├── Estudios que sustentan
       └── Estudios que contradicen
```

La arquitectura deberá conservar ambas dimensiones.

---

# 30. Identificadores Externos

Los identificadores externos permitirán reconciliación e interoperabilidad con sistemas externos.

No sustituirán la identidad interna.

Conceptualmente:

```text
Entidad Atlas
├── ID Atlas
└── Identificadores externos
```

Cada identificador externo podrá conservar:

```text
Identificador externo
├── sistema
├── valor
├── URL del registro
└── fecha de consulta
```

Ejemplos conceptuales:

```text
Taxón
├── ID Atlas
├── IPNI
└── POWO
```

```text
Compuesto químico
├── ID Atlas
├── PubChem
└── ChEBI
```

```text
Publicación
├── ID Atlas
├── DOI
└── PMID
```

Se mantendrán las siguientes reglas:

```text
ID externo
≠
ID Atlas
```

```text
No existe identificador fiable
→ no se inventa
```

```text
Existen varios identificadores
→ se conservan cuando resulten pertinentes
```

```text
Existe conflicto
→ se conserva procedencia
  y se somete a reconciliación
```

También deberá distinguirse entre:

```text
Sistema externo
≠
Identificador externo
≠
URL del registro
```

---

# 31. Cardinalidades Conceptuales

Las cardinalidades iniciales constituyen restricciones conceptuales y no decisiones físicas de implementación.

### 31.1 Taxón

```text
Taxón
└── pertenece a ──► 0..1 Taxón superior inmediato
```

El nivel superior documentado por el Atlas podrá no disponer de un Taxón padre dentro del modelo.

---

### 31.2 Droga vegetal

```text
Droga vegetal
├── procede de ──► 1..n Taxón
└── procede de ──► 1..n Parte vegetal
```

---

### 31.3 Preparado vegetal

```text
Preparado vegetal
├── deriva de ──► 1..n Droga vegetal
└── deriva de ──► 0..n Preparado vegetal
```

La primera cardinalidad podrá ser refinada posteriormente si aparecen casos legítimos de preparados derivados exclusivamente de otros preparados cuya droga de origen sea inferible mediante la cadena de relaciones.

ADM-004 no obliga todavía a resolver esa normalización físicamente.

---

### 31.4 Compuesto químico

```text
Compuesto químico
└── pertenece a ──► 0..n Clase química
```

La ausencia de clasificación química documentada no invalida la identidad del compuesto.

---

### 31.5 Estudio

```text
Estudio
└── estudia ──► 1..n objetos de conocimiento
```

---

### 31.6 Publicación

```text
Publicación
└── reporta ──► 0..n Estudios
```

Una publicación podrá existir como fuente válida aun cuando no represente formalmente un Estudio dentro del Atlas.

---

### 31.7 Monografía

```text
Monografía
└── documenta ──► 1..n objetos
```

---

### 31.8 Afirmación

```text
Afirmación
└── relacionada con ──► 0..n Fuentes
```

Una Afirmación podrá existir temporalmente en estado Propuesta antes de que su evidencia haya sido formalmente vinculada.

Las reglas de aprobación podrán exigir posteriormente determinadas condiciones mínimas de evidencia o procedencia.

---

## 31.9 Principio de flexibilidad

No se impondrá unicidad cuando el conocimiento real pueda presentar:

- Varias fuentes.
- Varios materiales.
- Varios taxones.
- Varias partes vegetales.
- Varias intervenciones.
- Varios estudios.
- Varias publicaciones.
- Varias conclusiones.
- Evidencia contradictoria.

Por tanto:

```text
Cardinalidad conceptual
≠
Cardinalidad física de almacenamiento
```

---

# 32. Modelo Integrado

El modelo conceptual general puede representarse de manera simplificada como:

```text
                         Atlas
                           │
                           ▼
                        Taxón
                           │
                 ┌─────────┴─────────┐
                 │                   │
                 ▼                   ▼
           Parte vegetal       Uso tradicional
                 │
                 ▼
           Droga vegetal
                 │
                 ▼
         Preparado vegetal
                 │
       ┌─────────┼──────────┐
       │         │          │
       ▼         ▼          ▼
 Compuestos     Uso      Seguridad
       │    terapéutico
       │         │
       ▼         ▼
 Clase química  Condición
       │        de salud
       ▼
  Actividad
  biológica
       │
       ▼
 Mecanismo
 de acción
```

El conocimiento generado alrededor de estos objetos podrá ser gobernado mediante:

```text
Conocimiento estructurado
         │
         ▼
     Afirmación
         │
         ├── sustentada por ──► Fuente
         ├── limitada por ────► Fuente
         ├── contradicha por ─► Fuente
         └── contextualizada por ─► Fuente
                                      │
                                      ▼
                                  Procedencia
```

Las fuentes podrán incluir:

```text
Estudio
Publicación
Monografía
Farmacopea
Disposición normativa
Organización
Otros objetos autorizados
```

y los estudios se conectarán documentalmente mediante:

```text
Estudio
   │
   └── reportado en ──► Publicación
```

---

# 33. Separación entre Modelo Conceptual e Implementación

ADM-004 establece semántica y arquitectura conceptual.

No determina todavía cómo se implementará físicamente cada elemento.

En consecuencia, este documento no obliga a utilizar:

```text
RDF
OWL
JSON
YAML
SQL
Neo4j
PostgreSQL
GraphQL
Document database
Graph database
Triple store
```

Tampoco determina que cada entidad deba corresponder necesariamente a:

- Un archivo.
- Una tabla.
- Una colección.
- Un nodo físico.
- Una página Markdown.
- Un documento editorial.

Las decisiones de implementación deberán respetar este modelo, pero podrán elegir la representación técnica más apropiada.

---

# 34. Automatización

Las herramientas automáticas y agentes de inteligencia artificial podrán:

- Identificar posibles entidades.
- Detectar relaciones.
- Extraer candidatos a afirmaciones.
- Localizar fuentes.
- Asociar identificadores externos.
- Proponer reconciliaciones.
- Detectar contradicciones.
- Detectar cambios.
- Proponer nueva información.

Sin embargo:

```text
Descubrimiento automático
≠
Aprobación automática
```

y:

```text
Extracción automática
≠
Verdad científica
```

Las automatizaciones deberán conservar, cuando corresponda:

- Fuente.
- Contexto.
- Procedencia.
- Transformaciones.
- Estado de gobernanza.

No deberán completar información ausente mediante inferencias presentadas como hechos.

---

# 35. Evolución del Modelo

La presente versión constituye el modelo inicial de información del Atlas.

No deberá entenderse como una enumeración definitiva de todos los objetos científicos que el proyecto podrá representar.

Podrán surgir posteriormente necesidades de modelar de forma independiente conceptos como:

- Métodos analíticos.
- Productos.
- Formulaciones.
- Medicamentos.
- Proteínas.
- Enzimas.
- Genes.
- Dianas moleculares.
- Rutas metabólicas.
- Intervenciones.
- Poblaciones.
- Preparaciones tradicionales específicas.
- Otros objetos científicos.

Su incorporación requerirá demostrar que poseen suficiente:

- Identidad.
- Reutilización.
- Interconexión.
- Valor científico.
- Valor de navegación.
- Necesidad de gobernanza.

No deberán crearse entidades únicamente por anticipar necesidades hipotéticas.

---

# 36. Consecuencias Arquitectónicas

La adopción de este modelo implica que:

1. El Atlas podrá representar conocimiento independientemente de sus documentos editoriales.

2. Una entidad podrá participar en múltiples dominios sin duplicar su identidad.

3. La misma Condición de salud podrá reutilizarse en contextos terapéuticos, toxicológicos, clínicos y tradicionales.

4. Los compuestos químicos podrán reutilizarse entre múltiples drogas vegetales y preparados.

5. Las clases químicas podrán formar jerarquías propias.

6. Las actividades biológicas y mecanismos podrán reutilizarse entre distintos objetos.

7. La evidencia correspondiente a un preparado vegetal no se transferirá automáticamente al Taxón completo.

8. Los usos tradicionales permanecerán conceptualmente separados de los usos terapéuticos contemporáneos.

9. Los resultados científicos permanecerán diferenciados de las conclusiones de los autores.

10. Las conclusiones de los autores no serán tratadas automáticamente como verdad científica.

11. Las contradicciones podrán conservarse sin eliminar información.

12. Fuente y Procedencia serán transversales a todos los dominios.

13. Los identificadores externos facilitarán interoperabilidad sin sustituir la identidad del Atlas.

14. El modelo podrá evolucionar sin obligar a modificar inmediatamente su tecnología de almacenamiento.

15. Las vistas editoriales podrán construirse posteriormente a partir del conocimiento estructurado.

---

# 37. Relación con Documentos Arquitectónicos

ADM-004 deberá interpretarse de acuerdo con la jerarquía normativa del Atlas.

Conceptualmente:

```text
GOV
 │
 ▼
ADR
 │
 ▼
ADM
 │
 ├── ADM-002
 │     Arquitectura del Modelo
 │     de Conocimiento
 │
 ├── ADM-003
 │     Dominios de Conocimiento
 │
 └── ADM-004
       Modelo de Información
```

ADM-004 desarrolla y concreta:

- La Capa de Entidades definida por ADM-002.
- La Capa de Relaciones definida por ADM-002.
- La arquitectura de Afirmaciones y Evidencia.
- La Capa de Procedencia.
- Los dominios establecidos por ADM-003.
- El modelo híbrido establecido por ADR-005.
- El principio de identidad gobernada establecido por ADR-002.

Los estándares posteriores deberán respetar las decisiones aquí establecidas.

---

# 38. Decisiones Consolidadas

ADM-004 establece las siguientes decisiones principales:

```text
Taxón
→ entidad única para niveles taxonómicos
```

```text
Familia / Género / Especie
→ niveles taxonómicos
  y no tipos de entidad independientes
```

```text
Parte vegetal
→ entidad genérica reutilizable
```

```text
Droga vegetal
→ entidad farmacognóstica específica
```

```text
Preparado vegetal
→ elemento transversal con identidad
  cuando el contexto lo requiera
```

```text
Compuesto químico
→ entidad
```

```text
Clase química
→ entidad jerarquizable
```

```text
Perfil fitoquímico
→ información contextual
  y no entidad
```

```text
Tipo de metabolito
→ clasificación
```

```text
Actividad biológica
→ entidad
```

```text
Mecanismo de acción
→ entidad
```

```text
Efecto observado
→ información contextual
```

```text
Farmacodinámica
→ información contextual
```

```text
Farmacocinética
→ información contextual
```

```text
Uso terapéutico
→ entidad asociativa
```

```text
Condición de salud
→ entidad reutilizable
```

```text
Evento adverso
→ relación contextual
  con Condición de salud
```

```text
Contraindicación
→ relación / afirmación contextual
```

```text
Precaución
→ relación / afirmación contextual
```

```text
Interacción
→ entidad contextual
```

```text
Estudio
→ entidad científica
```

```text
Publicación
→ entidad documental
```

```text
Síntesis de evidencia
→ clasificación dentro de Estudio
```

```text
Uso tradicional
→ entidad
```

```text
Comunidad / pueblo
Sistema tradicional
Región
→ entidades opcionales
```

```text
Organización
→ entidad reutilizable
```

```text
Farmacopea
→ entidad
```

```text
Monografía
→ entidad única
  con clasificación por tipo
```

```text
Disposición normativa
→ entidad
```

```text
Afirmación
→ entidad ligera de gobernanza
```

```text
Evidencia
→ relación transversal calificada
  y no entidad
```

```text
Fuente
→ categoría abstracta transversal
```

```text
Procedencia
→ trazabilidad transversal
```

```text
Relaciones
→ vocabulario semántico controlado
```

```text
Estado de gobernanza
→ Propuesta / En revisión / Aprobada
```

```text
Estado científico
→ Sustentada / Limitada / Contradicha
```

```text
Identificador externo
→ información de interoperabilidad
  y no identidad del Atlas
```

---

# 39. Estado de la Decisión

El presente ADM establece el **Modelo de Información v1.0 del Atlas de Fitoterapia**.

Su aprobación habilita el desarrollo posterior de:

- Estándares de entidades.
- Catálogos de relaciones.
- Reglas de identificadores.
- Esquemas de procedencia.
- Modelos de afirmaciones.
- Reglas de evidencia.
- Esquemas físicos de datos.
- Herramientas de validación.
- Automatizaciones.
- Vistas editoriales derivadas.

Cualquier cambio que altere de forma sustancial:

- Los tipos fundamentales de entidad.
- La responsabilidad conceptual de las entidades.
- La separación entre conocimiento, evidencia y fuente.
- El modelo de identidad.
- La estructura de relaciones.
- El principio de procedencia.

deberá evaluarse mediante el mecanismo de gobernanza arquitectónica correspondiente.

---

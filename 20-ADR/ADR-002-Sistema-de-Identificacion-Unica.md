\---

id: ADR-002

title: Sistema de Identificación Única

version: 1.1.0

status: Approved

type: ADR

created: 2026-07-25

updated: 2026-07-28

author: Proyecto Atlas de Fitoterapia

tags:

&#x20; - architecture

&#x20; - governance

&#x20; - identification

&#x20; - traceability

\---



\# Sistema de Identificación Única



\## 1. Contexto



El Atlas de Fitoterapia se concibe como una plataforma de conocimiento científico capaz de representar entidades pertenecientes a diferentes dominios, incluyendo documentos normativos, entidades biológicas, compuestos químicos, enfermedades, evidencia científica y recursos documentales.



Durante la fase de diseño se identificó que los nombres de las entidades pueden cambiar con el tiempo debido a actualizaciones taxonómicas, cambios editoriales, nuevas clasificaciones o revisiones científicas.



Asimismo, la estabilidad de la identidad constituye un requisito indispensable para preservar la trazabilidad, garantizar la interoperabilidad y permitir la evolución ordenada del conocimiento administrado por el Atlas.



Por esta razón se consideró necesario separar la identidad de una entidad de su nombre, ubicación o representación documental, garantizando así su estabilidad durante todo su ciclo de vida.



\---



\## 2. Problema



Utilizar nombres como mecanismo de identificación genera ambigüedad y dificulta la trazabilidad del conocimiento.



Una misma entidad puede:



\- Cambiar de nombre.

\- Cambiar de clasificación.

\- Aparecer en múltiples documentos.

\- Relacionarse con numerosas entidades diferentes.

\- Mantener relaciones que deben conservarse entre distintas versiones del conocimiento.



Sin un sistema de identificación permanente resulta imposible garantizar referencias estables, automatizar relaciones entre entidades o mantener la consistencia del Atlas conforme evolucione.



\---



\## 3. Decisión



El Atlas de Fitoterapia adoptará un Sistema de Identificación Única (SIU) basado en identificadores permanentes, independientes de los nombres, títulos, ubicaciones físicas o formatos de representación.



Toda entidad gobernada por el Atlas deberá contar con un identificador único, permanente, estable y no reutilizable, asignado desde el momento de su creación.



Los identificadores constituirán la referencia oficial de cada objeto gobernado y deberán utilizarse en relaciones, referencias, trazabilidad, automatizaciones, integraciones y procesos de análisis.



Los nombres científicos, nombres comunes, títulos de documentos y cualquier otro atributo descriptivo podrán modificarse cuando exista justificación científica, editorial o técnica, sin afectar la identidad del objeto.



\### Principio de separación entre identidad y representación



El Atlas distingue explícitamente los siguientes conceptos:



| Concepto | Definición |

|----------|------------|

| \*\*Objeto gobernado\*\* | Elemento administrado por el Atlas cuya existencia debe ser identificada y trazable durante todo su ciclo de vida. |

| \*\*Identidad\*\* | Propiedad permanente que distingue de forma única a un objeto gobernado. La identidad permanece inalterada durante todo su ciclo de vida. |

| \*\*Representación\*\* | Forma en que un objeto gobernado es descrito, documentado o visualizado. Una representación puede modificarse sin alterar la identidad del objeto. |

| \*\*Documento\*\* | Artefacto editorial utilizado para representar, describir, gobernar o comunicar uno o varios objetos gobernados. |



En consecuencia, la identidad pertenece al objeto gobernado y no a su representación documental. Los documentos constituyen representaciones editables utilizadas para describir, organizar o gobernar dichos objetos, mientras que los identificadores permanentes garantizan su estabilidad, trazabilidad e interoperabilidad a lo largo del tiempo.



\---



\## 4. Justificación



La adopción de un Sistema de Identificación Única proporciona una base sólida para el crecimiento del Atlas de Fitoterapia y garantiza la estabilidad del conocimiento a largo plazo.



Esta decisión permite desacoplar la identidad de un objeto gobernado de sus atributos descriptivos, evitando que cambios editoriales, taxonómicos o científicos afecten las relaciones previamente establecidas.



Asimismo, facilita la interoperabilidad entre documentos, la automatización de procesos, la integración con herramientas externas, la generación de grafos de conocimiento y la trazabilidad completa de la información científica.



La identificación permanente constituye un requisito fundamental para preservar la consistencia del Atlas conforme aumente el número de entidades y relaciones.



\---



\## 5. Consecuencias



Como resultado de esta decisión:



\- Toda entidad gobernada por el Atlas deberá recibir un identificador único antes de incorporarse al proyecto.

\- Los identificadores nunca serán reutilizados.

\- Los cambios de nombre no modificarán la identidad del objeto.

\- Las relaciones entre entidades utilizarán identificadores permanentes.

\- Los documentos deberán referenciar entidades mediante sus identificadores oficiales cuando corresponda.

\- Los identificadores deberán mantenerse aun cuando un objeto sea archivado, sustituido o declarado obsoleto.

\- Las automatizaciones futuras podrán utilizar el Sistema de Identificación Única como mecanismo principal de integración.



\---



\## 6. Impacto



Esta decisión afecta a los siguientes componentes del Atlas:



\### Gobernanza



\- Gobierno documental.

\- Arquitectura.

\- Estándares.



\### Conocimiento



\- Ontología.

\- Monografías.

\- Plantillas.

\- Entidades científicas.



\### Automatización



\- Automatizaciones.

\- Validaciones.

\- Integraciones.



\### Publicación



\- Publicación mediante Quartz.

\- Navegación.

\- Referencias internas.



\### Evolución futura



\- Integraciones con agentes de inteligencia artificial.

\- Interoperabilidad con sistemas externos.

\- Grafos de conocimiento.



El Sistema de Identificación Única constituye una decisión arquitectónica fundacional y deberá mantenerse estable durante todo el ciclo de vida del Atlas.



\---



\## 7. Implementación



La implementación de esta decisión comprende:



1\. Definir la sintaxis oficial de los identificadores.

2\. Establecer las reglas de asignación.

3\. Definir categorías y convenciones de nomenclatura.

4\. Incorporar mecanismos de validación.

5\. Actualizar las plantillas para soportar identificadores permanentes.

6\. Incorporar el uso obligatorio de identificadores en las relaciones entre entidades.



Este ADR establece únicamente la decisión arquitectónica de adoptar un Sistema de Identificación Única y el principio de separación entre identidad y representación. La especificación técnica será desarrollada en los documentos de arquitectura y estándares correspondientes.



\---



\## 8. Referencias



\- GOV-001 — Constitución del Atlas de Fitoterapia.

\- ADM-001 — Arquitectura General del Atlas de Fitoterapia.

\- ADR-001 — El ROADMAP como Documento Vivo de Planificación.

\- EEA-000 — Convenciones Generales.

\- ISO 11179 — Metadata Registries.

\- Wilkinson, M. D., et al. (2016). \*The FAIR Guiding Principles for Scientific Data Management and Stewardship\*. Scientific Data, 3, 160018.

\- W3C Resource Description Framework (RDF).

\- W3C SKOS — Simple Knowledge Organization System.


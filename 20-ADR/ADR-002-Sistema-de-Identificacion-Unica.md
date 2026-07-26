\# ADR-002



\# Sistema de Identificación Única



\---



\## 1. Información del documento



| Campo | Valor |

|-------|-------|

| Identificador | ADR-002 |

| Versión | 1.0 |

| Estado | Aprobado |

| Fecha | 2026-07-25 |

| Tipo | Architecture Decision Record |

| Autor | Proyecto Atlas de Fitoterapia |



\### Documentos relacionados



\- GOV-001

\- ADR-001

\- EEA-000

\- ADM-001



\---



\## 2. Contexto



El Atlas de Fitoterapia se concibe como una plataforma de conocimiento científico capaz de representar entidades pertenecientes a diferentes dominios, incluyendo documentos normativos, entidades biológicas, compuestos químicos, enfermedades, evidencia científica y recursos documentales.



Durante la fase de diseño se identificó que los nombres de las entidades pueden cambiar con el tiempo debido a actualizaciones taxonómicas, cambios editoriales, nuevas clasificaciones o revisiones científicas.



Por esta razón se consideró necesario separar la identidad de una entidad de su nombre, ubicación o representación documental, garantizando así su estabilidad a lo largo del tiempo.



\---



\## 3. Problema



Utilizar nombres como mecanismo de identificación genera ambigüedad y dificulta la trazabilidad.



Una misma entidad puede:



\- cambiar de nombre;

\- cambiar de clasificación;

\- aparecer en múltiples documentos;

\- relacionarse con numerosas entidades diferentes.



Sin un sistema de identificación permanente resulta imposible garantizar referencias estables, automatizar relaciones entre entidades o mantener la consistencia del conocimiento conforme el Atlas evolucione.



\---



\## 4. Decisión



El Atlas de Fitoterapia adoptará un Sistema de Identificación Única (SIU) basado en identificadores permanentes, independientes de los nombres, títulos, ubicaciones físicas o formatos de representación.



Toda entidad administrada por el Atlas deberá contar con un identificador único, persistente y no reutilizable, asignado desde su creación.



Los identificadores constituirán la referencia oficial de cada entidad y deberán utilizarse en relaciones, enlaces, trazabilidad, automatizaciones y procesos de integración.



Los nombres científicos, nombres comunes, títulos de documentos y demás atributos descriptivos podrán modificarse cuando exista justificación científica o editorial, sin afectar la identidad de la entidad.



El sistema distinguirá explícitamente entre:



\- \*\*Entidades de conocimiento\*\*, que representan objetos del dominio (por ejemplo, plantas, compuestos, enfermedades, metabolitos, preparados, estudios clínicos o referencias bibliográficas).

\- \*\*Documentos\*\*, que representan artefactos editoriales destinados a describir, organizar o normar el conocimiento (por ejemplo, monografías, estándares, ADR, ADM o guías).



La identidad pertenece a la entidad; el documento constituye únicamente una representación estructurada de dicha entidad.



\---



\## 5. Justificación



La adopción de un Sistema de Identificación Única proporciona una base sólida para el crecimiento del Atlas de Fitoterapia y garantiza la estabilidad del conocimiento a largo plazo.



Esta decisión permite desacoplar la identidad de una entidad de sus atributos descriptivos, evitando que cambios editoriales, taxonómicos o científicos afecten las relaciones previamente establecidas.



Asimismo, facilita la interoperabilidad entre documentos, la automatización de procesos, la integración con herramientas externas, la generación de grafos de conocimiento y la trazabilidad completa de la información científica.



La identificación permanente constituye un requisito fundamental para preservar la consistencia del Atlas conforme aumente el número de entidades y relaciones.



\---



\## 6. Consecuencias



Como resultado de esta decisión:



\- Toda entidad deberá recibir un identificador único antes de incorporarse al Atlas.

\- Los identificadores nunca serán reutilizados.

\- Los cambios de nombre no modificarán la identidad de la entidad.

\- Las relaciones entre entidades utilizarán identificadores permanentes.

\- Los documentos deberán referenciar entidades mediante sus identificadores oficiales cuando corresponda.

\- Las automatizaciones futuras podrán utilizar el Sistema de Identificación Única como mecanismo principal de integración.



\---



\## 7. Impacto



Esta decisión afecta a todos los componentes del Atlas, incluyendo:



\- Gobernanza documental.

\- Arquitectura del conocimiento.

\- Ontología.

\- Monografías.

\- Plantillas.

\- Automatizaciones.

\- Publicación mediante Quartz.

\- Integraciones futuras con agentes de inteligencia artificial y otras herramientas de análisis.



El Sistema de Identificación Única se considera una decisión arquitectónica fundacional y deberá mantenerse estable a lo largo del ciclo de vida del proyecto.



\---



\## 8. Implementación



La especificación técnica del Sistema de Identificación Única, incluyendo la sintaxis de los identificadores, reglas de asignación, categorías, validaciones y convenciones de nomenclatura, será desarrollada en los documentos de arquitectura y estándares correspondientes.



Este ADR establece únicamente la decisión de adoptar un sistema de identificación permanente y el principio de separación entre identidad y representación.



\---



\## 9. Referencias



\- GOV-001 – Constitución del Atlas de Fitoterapia.

\- ADR-001 – ROADMAP como Documento Vivo.

\- ISO 11179 — Metadata Registries.

\- Wilkinson, M. D., et al. (2016). \*The FAIR Guiding Principles for scientific data management and stewardship\*. Scientific Data, 3, 160018.

\- W3C Resource Description Framework (RDF).

\- W3C SKOS – Simple Knowledge Organization System.


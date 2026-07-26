\---

id: ADR-003

title: Jerarquía Normativa

version: 1.0

status: Approved

type: ADR

created: 2026-07-25

updated: 2026-07-25

author: Proyecto Atlas de Fitoterapia

tags:

&#x20; - governance

&#x20; - architecture

&#x20; - hierarchy

\---



\# ADR-003



\# Jerarquía Normativa



\---



\## 1. Información del documento



| Campo | Valor |

|-------|-------|

| Identificador | ADR-003 |

| Versión | 1.0 |

| Estado | Aprobado |

| Fecha | 2026-07-25 |

| Tipo | Architecture Decision Record |

| Autor | Proyecto Atlas de Fitoterapia |



\### Documentos relacionados



\- GOV-001

\- ADR-001

\- ADR-002



\---



\## 2. Contexto



El Atlas de Fitoterapia está conformado por diferentes tipos de documentos con responsabilidades específicas, incluyendo documentos de gobierno, decisiones arquitectónicas, modelos de diseño, estándares editoriales, plantillas y documentos científicos.



Conforme el proyecto evolucione será necesario garantizar que estos documentos mantengan una relación jerárquica clara, evitando contradicciones y definiendo qué documento prevalece cuando exista un conflicto normativo.



Una jerarquía normativa bien definida facilita la gobernanza, preserva la coherencia del proyecto y proporciona un mecanismo objetivo para la toma de decisiones futuras.



\---



\## 3. Problema



Sin una jerarquía normativa pueden presentarse situaciones como:



\- Un estándar contradice una decisión arquitectónica.

\- Una plantilla implementa reglas diferentes a las establecidas.

\- Una monografía incumple una convención editorial.

\- Dos documentos establecen instrucciones incompatibles.



En ausencia de reglas de precedencia, estas situaciones generan ambigüedad y dificultan el mantenimiento del Atlas.



\---



\## 4. Decisión



El Atlas adopta la siguiente jerarquía normativa, donde cada nivel deriva su autoridad del nivel superior.



```text

GOV

&#x20;│

&#x20;▼

ADR

&#x20;│

&#x20;▼

ADM

&#x20;│

&#x20;▼

EEA

&#x20;│

&#x20;▼

TPL

&#x20;│

&#x20;▼

Documentos científicos

```



Cada nivel deberá respetar las disposiciones del nivel superior y no podrá establecer reglas que las contradigan.



\---



\## 5. Justificación



La jerarquía normativa proporciona un marco de autoridad claro para todos los documentos del Atlas de Fitoterapia.



Al definir explícitamente la precedencia entre los distintos tipos documentales se evita la aparición de reglas contradictorias, duplicidad de responsabilidades y ambigüedad en la toma de decisiones.



Esta estructura facilita la evolución controlada del proyecto, permite distribuir responsabilidades entre diferentes niveles de documentación y garantiza que las decisiones estratégicas permanezcan alineadas con los principios establecidos en GOV-001.



La separación jerárquica también mejora la mantenibilidad del Atlas al permitir que los cambios se realicen en el nivel correspondiente sin afectar innecesariamente al resto de la documentación.



Como principio general, un documento de nivel inferior podrá ampliar o especializar las disposiciones de un documento superior, pero nunca reducir, contradecir o invalidar su alcance.



\---



\## 6. Consecuencias



La adopción de esta jerarquía normativa implica que:



\- Las decisiones deberán documentarse en el nivel documental que corresponda.

\- Todo nuevo tipo documental deberá incorporarse explícitamente dentro de la jerarquía del Atlas.

\- Las revisiones documentales deberán considerar las dependencias entre documentos.

\- Los conflictos normativos podrán resolverse aplicando el principio de precedencia establecido en este ADR.

\- La evolución del Atlas podrá realizarse de forma ordenada sin comprometer la coherencia documental.



\---



\## 7. Impacto



Esta decisión afecta a todos los componentes del Atlas, incluyendo:



\- Gobernanza.

\- Arquitectura.

\- Estándares.

\- Plantillas.

\- Monografías.

\- Ontología.

\- Automatizaciones.

\- Publicación mediante Quartz.

\- Integraciones futuras.



La jerarquía normativa constituye el mecanismo formal mediante el cual se preservará la consistencia documental durante todo el ciclo de vida del proyecto.



\---



\## 8. Implementación



La jerarquía normativa deberá aplicarse durante la creación, revisión y actualización de todos los documentos del Atlas.



Las dependencias entre documentos deberán identificarse explícitamente mediante referencias cruzadas cuando corresponda.



Toda propuesta de modificación deberá evaluar previamente si el cambio corresponde al nivel documental adecuado.



Cuando exista una contradicción entre documentos prevalecerá siempre el documento ubicado en el nivel jerárquico superior.



\---



\## 9. Referencias



\- GOV-001 – Constitución del Atlas de Fitoterapia.

\- ADR-001 – ROADMAP como Documento Vivo.

\- ADR-002 – Sistema de Identificación Única.

\- ISO 9001:2015 — Sistemas de Gestión de la Calidad.

\- ISO/IEC/IEEE 42010 — Systems and Software Engineering — Architecture Description.



\---



\## Anexo A. Matriz de autoridad documental



| Nivel | Tipo documental | Responsabilidad principal |

|-------:|-----------------|---------------------------|

| 1 | GOV | Gobierno, misión, visión, principios y políticas del Atlas. |

| 2 | ADR | Decisiones arquitectónicas. |

| 3 | ADM | Diseño técnico y modelos de implementación. |

| 4 | EEA | Estándares, convenciones y buenas prácticas. |

| 5 | TPL | Plantillas oficiales del Atlas. |

| 6 | Documentos científicos | Representación del conocimiento científico. |


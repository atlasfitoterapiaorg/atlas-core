\---

id: EEA-001

title: Convenciones Documentales

version: 1.0.0

status: Approved

type: EEA

created: 2026-07-25

updated: 2026-07-25

author: Proyecto Atlas de Fitoterapia

tags:

&#x20; - documentation

&#x20; - standards

&#x20; - markdown

&#x20; - yaml

\---



\# EEA-001



\# Convenciones Documentales



\---



\## 1. Información del documento



| Campo | Valor |

|-------|-------|

| Identificador | EEA-001 |

| Versión | 1.0.0 |

| Estado | Aprobado |

| Fecha | 2026-07-25 |

| Tipo | Estándar de Ejecución del Atlas |

| Autor | Proyecto Atlas de Fitoterapia |



\### Documentos relacionados



\- EEA-000

\- ADR-003

\- ADR-004



\---



\## 2. Propósito



Este estándar define la estructura documental mínima que deberán cumplir todos los documentos oficiales del Atlas de Fitoterapia.



Su finalidad es asegurar uniformidad en la organización de la información, facilitar la navegación entre documentos, simplificar su mantenimiento y permitir la automatización de procesos de validación, generación y publicación.



\---



\## 3. Alcance



Este estándar aplica a todos los documentos incorporados al repositorio oficial del Atlas, independientemente de su categoría documental.



Las reglas aquí definidas constituyen los requisitos mínimos de estructura y presentación para cualquier documento aprobado.



\---



\## 4. Estructura documental



Todo documento oficial deberá seguir la siguiente estructura general:



1\. Front Matter YAML.

2\. Título.

3\. Identificación del documento.

4\. Contenido organizado mediante encabezados jerárquicos.

5\. Referencias.

6\. Historial de versiones (cuando aplique).



Las categorías documentales podrán añadir secciones específicas siempre que no alteren esta estructura base.



\---



\## 5. Metadatos obligatorios



Todo documento oficial del Atlas deberá comenzar con un bloque YAML Front Matter válido.



Como mínimo deberá contener los siguientes campos:



```yaml

id:

title:

version:

status:

type:

created:

updated:

author:

tags:

```



\### Definición de campos



| Campo | Obligatorio | Descripción |

|--------|-------------|-------------|

| id | Sí | Identificador único del documento. |

| title | Sí | Nombre oficial del documento. |

| version | Sí | Versión conforme a Semantic Versioning. |

| status | Sí | Estado del documento. |

| type | Sí | Tipo documental. |

| created | Sí | Fecha de creación. |

| updated | Sí | Fecha de última actualización aprobada. |

| author | Sí | Responsable del documento. |

| tags | Sí | Etiquetas de clasificación. |



No deberán incorporarse campos adicionales salvo que exista un estándar que así lo establezca.



\---



\## 6. Organización del contenido



Los documentos deberán organizarse mediante encabezados jerárquicos de Markdown.



Las secciones deberán seguir un orden lógico.



Cada encabezado deberá representar un único tema.



Se evitarán encabezados vacíos.



Cuando una sección exceda el alcance previsto deberá evaluarse su separación en un documento independiente.



Los títulos deberán ser descriptivos y consistentes con la terminología oficial del Atlas.



\---



\## 7. Reglas de redacción



La redacción deberá:



\- utilizar lenguaje técnico;

\- evitar ambigüedades;

\- evitar opiniones personales;

\- mantener consistencia terminológica;

\- evitar duplicación de contenido;

\- definir términos especializados cuando sea necesario;

\- utilizar tablas y listas cuando mejoren la comprensión.



Toda afirmación técnica, científica o normativa deberá sustentarse mediante referencias cuando corresponda.



Los ejemplos deberán identificarse claramente para diferenciarlos de las reglas normativas.



\---



\## 8. Versionado



Todos los documentos deberán utilizar Semantic Versioning 2.0.0.



Las versiones seguirán el formato:



MAJOR.MINOR.PATCH



\### Cambios mayores (MAJOR)



Cambios incompatibles o modificaciones normativas relevantes.



\### Cambios menores (MINOR)



Nuevas secciones o ampliaciones compatibles.



\### Correcciones (PATCH)



Correcciones editoriales, ortográficas o aclaraciones sin impacto normativo.



Toda actualización deberá reflejarse en el campo `updated`.



\---



\## 9. Validación



Antes de su aprobación todo documento deberá superar las siguientes verificaciones.



\### Validación estructural



\- YAML válido.

\- Metadatos obligatorios.

\- Encabezados jerárquicos.

\- Estructura documental correcta.



\### Validación documental



\- Identificador único.

\- Versión válida.

\- Referencias consistentes.

\- Documentos relacionados existentes.



\### Validación editorial



\- Sin secciones vacías.

\- Sin contenido duplicado.

\- Terminología consistente.

\- Lenguaje técnico y objetivo.



\### Validación automática



Siempre que sea técnicamente posible, estas verificaciones deberán ejecutarse mediante herramientas automatizadas.



Las validaciones automáticas complementan la revisión técnica y editorial.



\---



\## 10. Referencias



\- EEA-000 – Convenciones Generales.

\- ADR-003 – Jerarquía Normativa.

\- ADR-004 – Arquitectura antes que Implementación.

\- Semantic Versioning Specification 2.0.0 (semver.org).

\- YAML 1.2 Specification.

\- CommonMark Specification.


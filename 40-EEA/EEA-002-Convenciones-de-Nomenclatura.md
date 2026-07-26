

\---

id: EEA-002

title: Convenciones de Nomenclatura

version: 1.0.0

status: Approved

type: EEA

created: 2026-07-25

updated: 2026-07-25

author: Proyecto Atlas de Fitoterapia

tags:

&#x20; - standards

&#x20; - naming

&#x20; - governance

\---



\# EEA-002



\# Convenciones de Nomenclatura



\---



\## 1. Información del documento



| Campo | Valor |

|-------|-------|

| Identificador | EEA-002 |

| Versión | 1.0.0 |

| Estado | Aprobado |

| Fecha | 2026-07-25 |

| Tipo | Estándar de Ejecución del Atlas |

| Autor | Proyecto Atlas de Fitoterapia |



\### Documentos relacionados



\- EEA-000

\- EEA-001

\- ADR-002



\---



\## 2. Propósito



Este estándar define las reglas de nomenclatura para todos los activos del Atlas de Fitoterapia.



Su finalidad es garantizar que documentos, directorios, recursos multimedia, conjuntos de datos y demás componentes puedan identificarse de forma consistente, inequívoca y compatible con herramientas de automatización y control de versiones.



\---



\## 3. Alcance



Las disposiciones de este estándar aplican a todos los activos almacenados en los repositorios oficiales del Atlas, incluyendo documentos, imágenes, diagramas, archivos de datos, scripts, plantillas y cualquier otro recurso incorporado al proyecto.



\---



\## 4. Principios de nomenclatura



\### 4.1 Unicidad



Cada activo deberá poseer un nombre que permita distinguirlo de cualquier otro activo de la misma categoría.



\### 4.2 Estabilidad



Los nombres deberán permanecer estables en el tiempo.



Sólo podrán modificarse cuando exista una razón técnica o documental debidamente justificada.



\### 4.3 Legibilidad



Los nombres deberán ser comprensibles para personas sin sacrificar su facilidad de procesamiento automático.



\### 4.4 Consistencia



Las mismas reglas deberán aplicarse de forma uniforme en todos los repositorios del Atlas.



\### 4.5 Compatibilidad



Los nombres deberán ser compatibles con los principales sistemas operativos, sistemas de archivos y plataformas de control de versiones.



\---



\## 5. Convenciones



\### 5.1 Idioma



Los nombres oficiales de documentos deberán redactarse en español.



Los identificadores técnicos podrán utilizar abreviaturas estandarizadas.



\### 5.2 Caracteres permitidos



Se utilizarán únicamente:



\- letras A-Z

\- números 0-9

\- guion medio (-)



No deberán utilizarse:



\- espacios

\- acentos

\- letra ñ

\- caracteres especiales

\- signos de puntuación



\### 5.3 Formato general



Los nombres seguirán el formato:



IDENTIFICADOR-Nombre-Descriptivo.ext



Ejemplos:



ADR-004-Arquitectura-antes-que-Implementacion.md



EEA-002-Convenciones-de-Nomenclatura.md



\### 5.4 Uso de mayúsculas



Los identificadores conservarán su formato institucional.



Las palabras descriptivas utilizarán Mayúscula Inicial.



\### 5.5 Singular



Siempre que sea posible se utilizará el singular.



Ejemplo:



Monografia



No:



Monografias



\### 5.6 Directorios



Los nombres de directorios utilizarán PascalCase sin espacios ni caracteres especiales.



Ejemplos:



Botanica/



PrincipiosActivos/



Farmacologia/



Monografias/



RecursosGraficos/



Cuando representen categorías institucionales podrán conservar el prefijo numérico oficial.



Ejemplos:



10-GOV/



20-ADR/



30-ADM/



40-EEA/



50-TPL/



\---



\## 6. Validación



\### 6.1 Validación del identificador



Se verificará que:



\- exista;

\- sea único;

\- corresponda a la categoría documental;

\- respete el formato oficial.



\### 6.2 Validación del nombre



Se verificará que:



\- describa correctamente el contenido;

\- utilice el idioma oficial;

\- no contenga abreviaturas ambiguas;

\- sea consistente con documentos relacionados.



\### 6.3 Validación de caracteres



Se verificará que:



\- no existan espacios;

\- no existan caracteres especiales;

\- no existan acentos;

\- exista compatibilidad con los sistemas de archivos soportados.



\### 6.4 Validación automática



Siempre que sea posible, estas verificaciones deberán ejecutarse mediante herramientas automatizadas.



Los activos que incumplan estas reglas no deberán incorporarse al repositorio oficial.



\---



\## 7. Referencias



\- EEA-000 – Convenciones Generales.

\- EEA-001 – Convenciones Documentales.

\- ADR-002 – Sistema de Identificación Única.

\- ISO 8601 – Date and Time Format.

\- Semantic Versioning 2.0.0.


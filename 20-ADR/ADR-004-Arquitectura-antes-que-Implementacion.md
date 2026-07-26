\---

id: ADR-004

title: Arquitectura antes que Implementación

version: 1.0

status: Approved

type: ADR

created: 2026-07-25

updated: 2026-07-25

author: Proyecto Atlas de Fitoterapia

tags:

&#x20; - governance

&#x20; - architecture

&#x20; - development

\---



\# ADR-004



\# Arquitectura antes que Implementación



\---



\## 1. Información del documento



| Campo | Valor |

|-------|-------|

| Identificador | ADR-004 |

| Versión | 1.0 |

| Estado | Aprobado |

| Fecha | 2026-07-25 |

| Tipo | Architecture Decision Record |

| Autor | Proyecto Atlas de Fitoterapia |



\### Documentos relacionados



\- GOV-001

\- ADR-001

\- ADR-002

\- ADR-003



\---



\## 2. Contexto



El Atlas de Fitoterapia es un proyecto de largo plazo cuya arquitectura debe mantenerse estable conforme aumente el número de documentos, entidades, estándares y componentes tecnológicos.



Durante la evolución de proyectos de conocimiento es frecuente que las implementaciones surjan como respuesta a necesidades inmediatas, sin que exista una decisión arquitectónica previamente documentada. Esta práctica genera inconsistencias, dificulta la trazabilidad y obliga a rediseñar componentes conforme el proyecto crece.



Con el propósito de preservar la coherencia del Atlas, se establece un principio que determina el orden en que deben desarrollarse las decisiones, los diseños, los estándares y las implementaciones.



\---



\## 3. Problema



Implementar soluciones sin una decisión arquitectónica previa provoca que:



\- diferentes componentes evolucionen siguiendo criterios distintos;

\- existan implementaciones incompatibles entre sí;

\- aumente la deuda arquitectónica;

\- se pierda la trazabilidad entre el problema identificado y la solución implementada;

\- las decisiones dependan del contexto inmediato y no de una visión global del Atlas.



\---



\## 4. Decisión



El Atlas adoptará un flujo de desarrollo basado en el principio \*\*Arquitectura antes que Implementación\*\*.



Toda implementación permanente deberá estar respaldada por la documentación correspondiente dentro de la jerarquía normativa del Atlas.



Como principio general, el desarrollo seguirá la siguiente secuencia:



```text

GOV

&#x20;↓

ADR

&#x20;↓

ADM

&#x20;↓

EEA

&#x20;↓

TPL

&#x20;↓

Implementación

&#x20;↓

Conocimiento

```



Cada etapa deberá proporcionar el contexto necesario para la siguiente.



No se crearán implementaciones permanentes cuya justificación arquitectónica no haya sido previamente documentada.



Las implementaciones experimentales o exploratorias podrán realizarse durante la fase de investigación, siempre que no formen parte del repositorio oficial hasta completar el proceso documental correspondiente.



\---



\## 5. Justificación



La arquitectura constituye el mecanismo mediante el cual el Atlas preserva la coherencia entre sus objetivos, su estructura documental y su implementación tecnológica.



Establecer un flujo donde las decisiones preceden a la implementación garantiza que cada componente del Atlas responda a una necesidad previamente identificada, cuente con una justificación explícita y pueda evolucionar de manera controlada.



Este enfoque reduce la deuda arquitectónica, facilita la incorporación de nuevos colaboradores, mejora la trazabilidad de las decisiones y disminuye la probabilidad de introducir soluciones inconsistentes o difíciles de mantener.



La posibilidad de realizar implementaciones experimentales fuera del repositorio oficial proporciona la flexibilidad necesaria para investigar nuevas herramientas y tecnologías sin comprometer la estabilidad del Atlas.



\---



\## 6. Consecuencias



La adopción de este principio implica que:



\- Toda implementación permanente deberá tener un respaldo documental dentro de la jerarquía normativa del Atlas.

\- Las decisiones arquitectónicas precederán al diseño técnico y a la definición de estándares.

\- Los experimentos podrán desarrollarse libremente mientras permanezcan fuera del repositorio oficial.

\- La incorporación de nuevas funcionalidades requerirá identificar previamente el nivel documental donde debe registrarse la decisión correspondiente.

\- La evolución del Atlas será gradual, trazable y alineada con su arquitectura.



\---



\## 7. Impacto



Esta decisión afecta el desarrollo de todos los componentes del Atlas, incluyendo:



\- Gobernanza.

\- Arquitectura.

\- Desarrollo tecnológico.

\- Automatizaciones.

\- Integraciones con inteligencia artificial.

\- Sitio web.

\- Plantillas.

\- Monografías.

\- Procesos editoriales.



Este principio define la disciplina de desarrollo que regirá el crecimiento del Atlas durante todo su ciclo de vida.



\---



\## 8. Implementación



El desarrollo de nuevas capacidades dentro del Atlas deberá seguir, cuando corresponda, la siguiente secuencia:



1\. Identificación de la necesidad.

2\. Decisión arquitectónica (ADR).

3\. Diseño de la solución (ADM).

4\. Definición de estándares (EEA).

5\. Elaboración de plantillas (TPL).

6\. Implementación.

7\. Incorporación al conocimiento oficial.



Las actividades de investigación, evaluación o experimentación podrán realizarse fuera del repositorio oficial sin seguir esta secuencia, siempre que sus resultados no sean incorporados al Atlas hasta completar el proceso documental correspondiente.



\---



\## 9. Referencias



\- GOV-001 – Constitución del Atlas de Fitoterapia.

\- ADR-001 – ROADMAP como Documento Vivo.

\- ADR-002 – Sistema de Identificación Única.

\- ADR-003 – Jerarquía Normativa.

\- ISO/IEC/IEEE 42010 — Systems and Software Engineering — Architecture Description.

\- ISO 9001:2015 — Sistemas de Gestión de la Calidad.


\---

id: ADM-001

title: Arquitectura General del Atlas

version: 1.0.0

status: Approved

type: ADM

created: 2026-07-25

updated: 2026-07-25

author: Proyecto Atlas de Fitoterapia

tags:

&#x20; - architecture

&#x20; - atlas

&#x20; - governance

\---



\# ADM-001



\# Arquitectura General del Atlas



\---



\## 1. Información del documento



| Campo | Valor |

|-------|-------|

| Identificador | ADM-001 |

| Versión | 1.0.0 |

| Estado | Aprobado |

| Fecha | 2026-07-25 |

| Tipo | Documento de Arquitectura |

| Autor | Proyecto Atlas de Fitoterapia |



\### Documentos relacionados



\- GOV-001

\- ADR-001

\- ADR-002

\- ADR-003

\- ADR-004

\- EEA-000

\- EEA-001

\- EEA-002



\---



\## 2. Propósito



Definir la arquitectura general del Atlas de Fitoterapia, identificando sus componentes principales, responsabilidades e interacción.



Este documento proporciona una visión integral de la solución sin describir detalles de implementación ni del modelo de conocimiento científico.



\---



\## 3. Alcance



Esta arquitectura comprende la organización lógica del proyecto Atlas de Fitoterapia, incluyendo repositorios, componentes documentales, flujo de trabajo y mecanismo de publicación.



No forma parte del alcance de este documento la definición del modelo conceptual del conocimiento ni la implementación tecnológica específica.



\---



\## 4. Objetivos Arquitectónicos



La arquitectura del Atlas deberá garantizar:



\- Escalabilidad.

\- Modularidad.

\- Trazabilidad.

\- Gobernanza documental.

\- Reutilización del conocimiento.

\- Interoperabilidad.

\- Automatización del flujo editorial.

\- Independencia tecnológica cuando sea posible.



\---



\## 5. Componentes del Atlas



\### atlas-core



Repositorio que contiene la gobernanza, arquitectura, estándares, plantillas y documentación técnica.



\### atlas-knowledge



Repositorio destinado al conocimiento científico del Atlas.



\### Quartz



Motor de generación del sitio estático.



\### GitHub



Plataforma de control de versiones y colaboración.



\### Obsidian



Herramienta principal para edición y organización del conocimiento.



\---



\## 6. Arquitectura General



```text

&#x20;                       Atlas de Fitoterapia

&#x20;                               │

&#x20;         ┌─────────────────────┴─────────────────────┐

&#x20;         │                                           │

&#x20;    atlas-core                               atlas-knowledge

&#x20;         │                                           │

&#x20;         │                                           │

&#x20; Gobierno (GOV)                             Monografías

&#x20; Arquitectura (ADR / ADM)                   Perfiles bioquímicos

&#x20; Estándares (EEA)                           Especies

&#x20; Plantillas (TPL)                           Principios activos

&#x20; Documentación técnica                      Enfermedades

&#x20;                                            Preparaciones

&#x20;                                            Referencias científicas

&#x20;         └─────────────────────┬─────────────────────┘

&#x20;                               │

&#x20;                          GitHub Repository

&#x20;                               │

&#x20;                    GitHub Actions

&#x20;                               │

&#x20;                            Quartz

&#x20;                               │

&#x20;                     Sitio Público del Atlas

```



La arquitectura separa la gobernanza del conocimiento científico, permitiendo que ambos evolucionen de forma independiente.



\---



\## 7. Flujo de Información



```text

Investigación científica

&#x20;       │

&#x20;       ▼

Recopilación de evidencia

&#x20;       │

&#x20;       ▼

Elaboración del documento

&#x20;       │

&#x20;       ▼

Revisión técnica

&#x20;       │

&#x20;       ▼

Aprobación

&#x20;       │

&#x20;       ▼

Integración en atlas-knowledge

&#x20;       │

&#x20;       ▼

Publicación

```



Cada etapa mantiene trazabilidad con la evidencia científica correspondiente.



\---



\## 8. Flujo de Publicación



```text

Edición (Obsidian)

&#x20;       │

&#x20;       ▼

Repositorio Git

&#x20;       │

&#x20;       ▼

GitHub

&#x20;       │

&#x20;       ▼

GitHub Actions

&#x20;       │

&#x20;       ▼

Quartz

&#x20;       │

&#x20;       ▼

Sitio Web

```



Sólo los documentos aprobados participan en el proceso de publicación.



\---



\## 9. Referencias



\- GOV-001

\- ADR-001

\- ADR-002

\- ADR-003

\- ADR-004

\- EEA-000

\- EEA-001

\- EEA-002


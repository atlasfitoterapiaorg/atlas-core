---
id: ADR-004
title: Arquitectura antes que Implementación
version: 1.1.0
status: Approved
type: ADR
created: 2026-07-25
updated: 2026-07-28
author: Proyecto Atlas de Fitoterapia
tags:
  - governance
  - architecture
  - development
---

# Arquitectura antes que Implementación

## 1. Contexto

El Atlas de Fitoterapia es un proyecto de largo plazo cuya arquitectura debe mantenerse estable conforme aumente el número de documentos, entidades, estándares y componentes tecnológicos.

Durante la evolución de proyectos de conocimiento es frecuente que las implementaciones surjan como respuesta a necesidades inmediatas sin que exista una decisión arquitectónica previamente documentada. Esta práctica genera inconsistencias, dificulta la trazabilidad y obliga a rediseñar componentes conforme el proyecto crece.

Con el propósito de preservar la coherencia del Atlas, se establece un principio que determina el orden en que deben desarrollarse las decisiones, los diseños, los estándares y las implementaciones.

---

## 2. Problema

Implementar soluciones sin una decisión arquitectónica previa provoca que:

- Diferentes componentes evolucionen siguiendo criterios distintos.
- Existan implementaciones incompatibles entre sí.
- Aumente la deuda arquitectónica.
- Se pierda la trazabilidad entre el problema identificado y la solución implementada.
- Las decisiones dependan del contexto inmediato y no de una visión global del Atlas.

---

## 3. Decisión

El Atlas adoptará un flujo de desarrollo basado en el principio **Arquitectura antes que Implementación**.

Toda implementación permanente deberá estar respaldada por la documentación correspondiente dentro de la jerarquía normativa del Atlas.

Como principio general, el desarrollo seguirá la siguiente secuencia:

```text
                          GOV
                           │
              ┌────────────┴────────────┐
              │                         │
             ADR                       ADM
              │                         │
              └────────────┬────────────┘
                           │
                          EEA
                           │
                          TPL
                           │
                   Implementación
                           │
                     Conocimiento
```

Cada etapa deberá proporcionar el contexto necesario para la siguiente.

No se crearán implementaciones permanentes cuya justificación arquitectónica no haya sido previamente documentada.

Las implementaciones experimentales o exploratorias podrán realizarse durante la fase de investigación, siempre que no formen parte del repositorio oficial hasta completar el proceso documental correspondiente.

---

## 4. Justificación

La arquitectura constituye el mecanismo mediante el cual el Atlas preserva la coherencia entre sus objetivos, su estructura documental y su implementación tecnológica.

La arquitectura no se limita al diseño técnico; constituye el mecanismo mediante el cual las decisiones documentadas se transforman en implementaciones consistentes con la gobernanza del Atlas.

Establecer un flujo donde las decisiones preceden a la implementación garantiza que cada componente del Atlas responda a una necesidad previamente identificada, cuente con una justificación explícita y pueda evolucionar de manera controlada.

Este enfoque reduce la deuda arquitectónica, facilita la incorporación de nuevos colaboradores, mejora la trazabilidad de las decisiones y disminuye la probabilidad de introducir soluciones inconsistentes o difíciles de mantener.

La posibilidad de realizar implementaciones experimentales fuera del repositorio oficial proporciona la flexibilidad necesaria para investigar nuevas herramientas y tecnologías sin comprometer la estabilidad del Atlas.

---

## 5. Consecuencias

Como resultado de esta decisión:

- Toda implementación permanente deberá tener un respaldo documental dentro de la jerarquía normativa del Atlas.
- Las decisiones arquitectónicas precederán al diseño técnico y a la definición de estándares.
- Los experimentos podrán desarrollarse libremente mientras permanezcan fuera del repositorio oficial.
- La incorporación de nuevas funcionalidades requerirá identificar previamente el nivel documental donde debe registrarse la decisión correspondiente.
- Ninguna implementación oficial podrá incorporarse al Atlas sin haber completado previamente el proceso documental correspondiente.
- La evolución del Atlas será gradual, trazable y alineada con su arquitectura.

---

## 6. Impacto

### Gobernanza

- Gobierno documental.
- Políticas.
- Principios del Atlas.

### Arquitectura

- Decisiones arquitectónicas (ADR).
- Modelos arquitectónicos (ADM).
- Diseño técnico.

### Desarrollo

- Implementación tecnológica.
- Automatizaciones.
- Integraciones.

### Publicación

- Plantillas.
- Sitio web.
- Publicación mediante Quartz.

### Conocimiento

- Monografías.
- Ontología.
- Procesos editoriales.

Este principio define la disciplina de desarrollo que regirá el crecimiento del Atlas durante todo su ciclo de vida.

---

## 7. Implementación

El desarrollo de nuevas capacidades dentro del Atlas deberá seguir, cuando corresponda, la siguiente secuencia:

1. Identificación del problema o necesidad.
2. Documentación de la decisión arquitectónica (ADR).
3. Desarrollo del modelo o diseño técnico (ADM).
4. Definición de estándares (EEA).
5. Elaboración de plantillas oficiales (TPL).
6. Implementación.
7. Incorporación al conocimiento oficial del Atlas.

Las actividades de investigación, evaluación o experimentación podrán realizarse fuera del repositorio oficial sin seguir esta secuencia, siempre que sus resultados no sean incorporados al Atlas hasta completar el proceso documental correspondiente.

---

## 8. Referencias

- GOV-001 — Constitución del Atlas de Fitoterapia.
- ADM-001 — Arquitectura General del Atlas de Fitoterapia.
- ADR-001 — El ROADMAP como Documento Vivo de Planificación.
- ADR-002 — Sistema de Identificación Única.
- ADR-003 — Jerarquía Normativa.
- ISO/IEC/IEEE 42010 — Systems and Software Engineering — Architecture Description.
- ISO 9001:2015 — Sistemas de Gestión de la Calidad.
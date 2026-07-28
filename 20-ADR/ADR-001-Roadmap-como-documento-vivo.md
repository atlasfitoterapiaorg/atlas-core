---
id: ADR-001
title: El ROADMAP como Documento Vivo de Planificación
version: 1.1.0
status: Approved
type: ADR
created: 2026-07-25
updated: 2026-07-28
author: Proyecto Atlas de Fitoterapia
tags:
  - roadmap
  - planning
  - governance
  - architecture
---

# El ROADMAP como Documento Vivo de Planificación

## 1. Contexto

Durante la fase de fundación del Atlas de Fitoterapia se identificó la necesidad de establecer un mecanismo formal para planificar el desarrollo del proyecto, controlar su evolución y garantizar una gobernanza consistente sobre el alcance de las iniciativas.

Inicialmente se consideró utilizar un documento denominado `TIMELINE.md`; sin embargo, conforme evolucionó el diseño metodológico del Atlas, se observó que dicho concepto resultaba insuficiente para administrar versiones, sprints, tareas y propuestas de mejora.

Asimismo, surgieron nuevas ideas que, aunque valiosas, no formaban parte del alcance aprobado del proyecto. Esta situación evidenció la necesidad de contar con un mecanismo que permitiera registrar dichas propuestas sin afectar la planificación vigente.

La ausencia de una fuente única de planificación incrementaba el riesgo de incorporar trabajo fuera del alcance aprobado, dificultaba el seguimiento del proyecto y reducía la trazabilidad de las decisiones de evolución.

Como resultado, se determinó la necesidad de establecer un único documento responsable de representar el estado del proyecto y controlar formalmente su alcance.

---

## 2. Problema

El Atlas requería una fuente única de verdad para la planificación estratégica y operativa del proyecto.

La ausencia de este mecanismo provocaba los siguientes riesgos:

- Incorporación de trabajo fuera del alcance aprobado.
- Duplicidad de información sobre el estado del proyecto.
- Pérdida de trazabilidad del avance.
- Dificultad para conocer el estado real del Atlas.
- Incremento de la deuda documental conforme creciera el proyecto.

Era necesario definir un documento oficial que centralizara la planificación y estableciera un mecanismo controlado para la incorporación de nuevas iniciativas.

---

## 3. Decisión

Se adopta `ROADMAP.md` como el único documento oficial de planificación estratégica y operativa del Atlas de Fitoterapia.

El `ROADMAP.md` será un documento vivo responsable de:

- Representar el estado actual del proyecto.
- Organizar el trabajo mediante versiones, sprints y tareas.
- Controlar el alcance del proyecto.
- Registrar propuestas pendientes de evaluación.
- Servir como referencia para la planificación de nuevas iniciativas.

Toda iniciativa que implique la creación, modificación o eliminación de artefactos del Atlas deberá estar previamente registrada y aprobada en el `ROADMAP.md` antes de iniciar su implementación.

---

## 4. Justificación

Centralizar la planificación en un único documento fortalece la gobernanza del Atlas, facilita el seguimiento del proyecto y reduce significativamente el riesgo de inconsistencias documentales.

El uso de un documento vivo permite mantener actualizada la planificación sin alterar el carácter inmutable de los documentos normativos, preservando una separación clara entre la gestión del proyecto y la documentación de gobierno.

La incorporación de un Backlog de Propuestas permite conservar nuevas ideas sin ampliar inmediatamente el alcance del proyecto, favoreciendo una evolución ordenada, controlada y trazable.

---

## 5. Consecuencias

A partir de la aprobación de esta decisión:

- `ROADMAP.md` se convierte en la única fuente oficial para la planificación del Atlas.
- Toda la planificación del proyecto se organizará mediante versiones, sprints y tareas.
- Ninguna iniciativa podrá desarrollarse fuera del alcance definido en el `ROADMAP.md`.
- Las propuestas no aprobadas deberán registrarse en el Backlog de Propuestas hasta su evaluación.
- `TIMELINE.md` deja de ser un mecanismo válido de planificación y queda sustituido por `ROADMAP.md`.

---

## 6. Impacto sobre otros documentos

Esta decisión impacta directamente en los siguientes documentos:

- README.md
- ROADMAP.md
- CHANGELOG.md
- GOV-001 Constitución del Atlas de Fitoterapia.
- ADM-001 Arquitectura General del Atlas de Fitoterapia.

Los documentos actuales y futuros deberán respetar esta decisión cuando hagan referencia a la planificación, al estado del proyecto o al control de alcance.

---

## 7. Implementación

La implementación de esta decisión comprende las siguientes acciones:

1. Crear el documento `ROADMAP.md`.
2. Sustituir el concepto inicial de `TIMELINE.md`.
3. Incorporar un Backlog de Propuestas.
4. Adoptar el modelo de planificación basado en versiones, sprints y tareas.
5. Actualizar los documentos afectados para referenciar `ROADMAP.md` como fuente oficial de planificación.

---

## 8. Referencias

- GOV-001 Constitución del Atlas de Fitoterapia.
- ADM-001 Arquitectura General del Atlas de Fitoterapia.
- README.md.
- ROADMAP.md.
- CHANGELOG.md.
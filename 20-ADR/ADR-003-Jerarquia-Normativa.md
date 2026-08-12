---
id: ADR-003
title: Jerarquía Normativa
version: 1.1.0
status: Approved
type: ADR
created: 2026-07-25
updated: 2026-07-28
author: Proyecto Atlas de Fitoterapia
tags:
  - governance
  - architecture
  - hierarchy
---

# Jerarquía Normativa

## 1. Contexto

El Atlas de Fitoterapia está conformado por diferentes tipos de documentos con responsabilidades específicas, incluyendo documentos de gobierno, decisiones arquitectónicas, modelos de arquitectura, estándares editoriales, plantillas y documentos científicos.

Conforme el proyecto evolucione será necesario garantizar que estos documentos mantengan una relación normativa clara, evitando contradicciones y definiendo qué documento prevalece cuando exista un conflicto.

Una jerarquía normativa bien definida facilita la gobernanza, preserva la coherencia del proyecto y proporciona un mecanismo objetivo para la toma de decisiones futuras.

---

## 2. Problema

Sin una jerarquía normativa pueden presentarse situaciones como:

- Un estándar contradice una decisión arquitectónica.
- Un modelo arquitectónico implementa reglas incompatibles con la gobernanza.
- Una plantilla aplica criterios distintos a los establecidos.
- Una monografía incumple las convenciones editoriales.
- Dos documentos establecen instrucciones incompatibles.

En ausencia de reglas de precedencia, estas situaciones generan ambigüedad y dificultan el mantenimiento del Atlas.

---

## 3. Decisión

El Atlas adopta la siguiente jerarquía normativa.

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
                Documentos científicos
```

### Principios de precedencia

- **GOV** constituye la máxima autoridad normativa del Atlas.
- **ADR** documenta decisiones arquitectónicas que deberán respetar la gobernanza establecida por GOV.
- **ADM** desarrolla los modelos arquitectónicos y técnicos respetando la gobernanza y las decisiones arquitectónicas vigentes.
- **EEA** establece estándares, convenciones y reglas de implementación alineadas con GOV, ADR y ADM.
- **TPL** implementa los estándares mediante plantillas oficiales.
- **Los documentos científicos** representan el conocimiento del Atlas utilizando las reglas definidas por los niveles superiores.

Ningún documento podrá establecer disposiciones que contradigan las definidas por un nivel superior.

---

## 4. Justificación

La jerarquía normativa proporciona un marco de autoridad claro para todos los documentos del Atlas de Fitoterapia.

Al definir explícitamente la precedencia entre los distintos tipos documentales se evita la aparición de reglas contradictorias, duplicidad de responsabilidades y ambigüedad en la toma de decisiones.

Esta estructura facilita la evolución controlada del proyecto, permite distribuir responsabilidades entre los diferentes niveles documentales y garantiza que las decisiones estratégicas permanezcan alineadas con los principios establecidos en GOV-001.

La separación jerárquica también mejora la mantenibilidad del Atlas al permitir que los cambios se realicen en el nivel correspondiente sin afectar innecesariamente al resto de la documentación.

Como principio general, un documento de nivel inferior podrá ampliar o especializar las disposiciones de un documento superior, pero nunca reducir, contradecir o invalidar su alcance.

La jerarquía normativa define la precedencia entre tipos documentales; los ADR documentan decisiones que afectan dicha jerarquía, pero no constituyen por sí mismos un nivel jerárquico superior a los documentos que modifican.

---

## 5. Consecuencias

Como resultado de esta decisión:

- Las decisiones deberán documentarse en el nivel documental correspondiente.
- Todo nuevo tipo documental deberá incorporarse explícitamente dentro de la jerarquía del Atlas.
- Las revisiones documentales deberán considerar las dependencias entre documentos.
- Los conflictos normativos deberán resolverse aplicando el principio de precedencia establecido en este ADR.
- La evolución del Atlas podrá realizarse de forma ordenada sin comprometer la coherencia documental.

---

## 6. Impacto

### Gobernanza

- Constitución del Atlas.
- Políticas.
- Gobierno documental.

### Arquitectura

- ADR.
- ADM.
- Diseño técnico.

### Conocimiento

- Ontología.
- Monografías.
- Entidades científicas.

### Publicación

- Plantillas.
- Publicación mediante Quartz.
- Navegación.
- Referencias internas.

### Automatización

- Validaciones.
- Automatizaciones.
- Integraciones futuras.

La jerarquía normativa constituye el mecanismo formal mediante el cual se preservará la consistencia documental durante todo el ciclo de vida del Atlas.

---

## 7. Implementación

La implementación de esta decisión comprende:

1. Aplicar la jerarquía normativa durante la creación, revisión y actualización de todos los documentos.
2. Identificar explícitamente las dependencias entre documentos mediante referencias cruzadas.
3. Verificar que toda modificación se realice en el nivel documental correspondiente.
4. Resolver cualquier conflicto documental aplicando el principio de precedencia establecido en este ADR.
5. Incorporar nuevos tipos documentales únicamente después de definir su posición dentro de la jerarquía normativa.

---

## 8. Referencias

- GOV-001 — Constitución del Atlas de Fitoterapia.
- ADM-001 — Arquitectura General del Atlas de Fitoterapia.
- ADR-001 — El ROADMAP como Documento Vivo de Planificación.
- ADR-002 — Sistema de Identificación Única.
- ISO 9001:2015 — Sistemas de Gestión de la Calidad.
- ISO/IEC/IEEE 42010 — Systems and Software Engineering — Architecture Description.

---

## Anexo A. Matriz de autoridad documental

| Nivel | Tipo documental | Deriva autoridad de | Responsabilidad principal |
|------:|-----------------|---------------------|---------------------------|
| 1 | GOV | — | Gobierno, misión, visión, principios y políticas del Atlas. |
| 2 | ADR | GOV | Documentar decisiones arquitectónicas y de gobernanza. |
| 2 | ADM | GOV y ADR aplicables | Definir la arquitectura y los modelos técnicos del Atlas. |
| 3 | EEA | GOV, ADR y ADM | Establecer estándares, convenciones y buenas prácticas. |
| 4 | TPL | EEA | Implementar los estándares mediante plantillas oficiales. |
| 5 | Documentos científicos | GOV, ADR, ADM, EEA y TPL | Representar el conocimiento científico del Atlas conforme a las reglas establecidas. |

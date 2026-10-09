# Cómo trabajamos en DYP Software

## Ramas

Cada tarea debe realizarse en una rama propia. Usamos nombres en minúsculas y separados por guiones, con el formato tipo/descripcion.

Ejemplos:
- docs/actualizar-readme
- feat/crear-estructura
- fix/corregir-error

La rama principal es main y está protegida. No se deben subir cambios directamente a ella.

## Commits

Los mensajes de los commits deben escribirse en minúsculas, en presente y con el formato tipo: descripción.

Tipos:
- feat: funcionalidad nueva.
- fix: corrección de errores.
- docs: cambios en documentación.
- chore: configuración y mantenimiento.

Ejemplos:
- docs: actualizar readme
- chore: agregar gitignore

## Revisión de Pull Requests

Cada integrante debe crear sus propios Pull Requests y revisar los cambios de sus compañeros.

Los revisores se asignan entre los integrantes, procurando que todos participen en las revisiones.

Antes de aprobar, se comprueba que los cambios cumplan el objetivo de la tarea, que los archivos estén organizados y que no se incluyan contraseñas ni información secreta.

## Cuándo se aprueba un Pull Request

Un Pull Request puede aprobarse cuando:
- Cumple el objetivo de la tarea.
- Tiene una descripción clara.
- No incluye archivos secretos ni cambios innecesarios.
- Ha sido revisado y aprobado por otro integrante.
- Cumple las reglas de protección de la rama main.

Después de la aprobación, el Pull Request puede fusionarse en main.

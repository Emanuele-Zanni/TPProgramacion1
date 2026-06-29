"""Índices y valores fijos del modelo basado en listas de listas."""

# Proyecto: [id, nombre, tareas, fecha_inicio, fecha_final, estado,
#            integrantes_ids, owner_id]
PROYECTO_ID = 0
PROYECTO_NOMBRE = 1
PROYECTO_TAREAS = 2
PROYECTO_FECHA_INICIO = 3
PROYECTO_FECHA_FINAL = 4
PROYECTO_ESTADO = 5
PROYECTO_INTEGRANTES = 6
PROYECTO_OWNER = 7
CAMPOS_PROYECTO = 8

# Tarea: [id, nombre, descripción, fecha_inicio, fecha_final, estado,
#         integrantes_asignados]
TAREA_ID = 0
TAREA_NOMBRE = 1
TAREA_DESCRIPCION = 2
TAREA_FECHA_INICIO = 3
TAREA_FECHA_FINAL = 4
TAREA_ESTADO = 5
TAREA_ASIGNADOS = 6
CAMPOS_TAREA = 7

# Rol: [id, nombre]
ROL_ID = 0
ROL_NOMBRE = 1
CAMPOS_ROL = 2

ESTADOS_PROYECTO = ("Activo", "Completado", "Expirado")
ESTADOS_TAREA = ("Activo", "Completado", "Expirado")
SEPARADOR_ROLES = "|"

"""Consultas cruzadas y uso significativo de map, filter y conjuntos."""

from General.constantes import (
    PROYECTO_INTEGRANTES,
    PROYECTO_TAREAS,
    TAREA_ASIGNADOS,
    TAREA_ESTADO,
)
from Recursividad.funciones import buscar_por_id_recursivo, obtener_nombres_recursivo


def tareas_de_proyecto(proyectos, proyecto_id):
    posicion = buscar_por_id_recursivo(proyectos, proyecto_id)
    if posicion == -1:
        return None
    return proyectos[posicion][PROYECTO_TAREAS][:]


def tareas_por_estado(proyectos, estado):
    todas = [
        tarea
        for proyecto in proyectos
        for tarea in proyecto[PROYECTO_TAREAS]
    ]
    return list(filter(lambda tarea: tarea[TAREA_ESTADO] == estado, todas))


def tareas_de_integrante(proyectos, usuario_id):
    def esta_asignado(tarea):
        ids = {
            item.get("id") if isinstance(item, dict) else item
            for item in tarea[TAREA_ASIGNADOS]
        }
        return usuario_id in ids

    todas = [
        tarea
        for proyecto in proyectos
        for tarea in proyecto[PROYECTO_TAREAS]
    ]
    return list(filter(esta_asignado, todas))


def integrantes_unicos_proyecto(proyecto, usuarios):
    ids = set(proyecto[PROYECTO_INTEGRANTES])
    for tarea in proyecto[PROYECTO_TAREAS]:
        for asignado in tarea[TAREA_ASIGNADOS]:
            ids.add(asignado.get("id") if isinstance(asignado, dict) else asignado)
    nombres_por_id = {
        datos.get("id"): nombre.title() for nombre, datos in usuarios.items()
    }
    return list(map(lambda usuario_id: nombres_por_id.get(usuario_id, "Desconocido"), sorted(ids)))


def nombres_normalizados(registros):
    return list(map(lambda nombre: str(nombre).strip().title(), obtener_nombres_recursivo(registros)))

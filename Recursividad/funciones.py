"""Tres recorridos recursivos sobre las matrices principales."""

from General.constantes import PROYECTO_TAREAS, TAREA_ESTADO


def buscar_por_id_recursivo(registros, id_buscado, indice=0):
    if indice >= len(registros):
        return -1
    if registros[indice][0] == id_buscado:
        return indice
    return buscar_por_id_recursivo(registros, id_buscado, indice + 1)


def contar_tareas_proyecto_recursivo(proyectos, id_proyecto, indice=0):
    if indice >= len(proyectos):
        return 0
    cantidad = (
        len(proyectos[indice][PROYECTO_TAREAS])
        if proyectos[indice][0] == id_proyecto
        else 0
    )
    return cantidad + contar_tareas_proyecto_recursivo(
        proyectos, id_proyecto, indice + 1
    )


def contar_tareas_estado_recursivo(tareas, estado, indice=0):
    if indice >= len(tareas):
        return 0
    cantidad = 1 if tareas[indice][TAREA_ESTADO] == estado else 0
    return cantidad + contar_tareas_estado_recursivo(tareas, estado, indice + 1)


def obtener_nombres_recursivo(registros, indice=0):
    if indice >= len(registros):
        return []
    return [registros[indice][1]] + obtener_nombres_recursivo(
        registros, indice + 1
    )

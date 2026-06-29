from Recursividad.funciones import (
    buscar_por_id_recursivo,
    contar_tareas_estado_recursivo,
    contar_tareas_proyecto_recursivo,
    obtener_nombres_recursivo,
)


def test_recursividad_lista_vacia():
    assert buscar_por_id_recursivo([], 1) == -1
    assert contar_tareas_proyecto_recursivo([], 1) == 0
    assert obtener_nombres_recursivo([]) == []


def test_recursividad_varios_registros():
    tareas = [
        [1, "A", "", None, None, "Activo", []],
        [2, "B", "", None, None, "Completado", []],
    ]
    proyectos = [[5, "Proyecto", tareas]]
    assert buscar_por_id_recursivo(tareas, 2) == 1
    assert contar_tareas_proyecto_recursivo(proyectos, 5) == 2
    assert contar_tareas_estado_recursivo(tareas, "Activo") == 1
    assert obtener_nombres_recursivo(tareas) == ["A", "B"]


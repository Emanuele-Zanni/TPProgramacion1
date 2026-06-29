from datetime import datetime

from General.consultas import (
    integrantes_unicos_proyecto,
    tareas_de_integrante,
    tareas_por_estado,
)
from Stats.funciones import calcular_resumen_estadistico


def datos():
    fecha = datetime(2026, 1, 1)
    tareas = [
        [1, "Tarea A", "Desc", fecha, fecha, "Completado", [{"id": 1, "nombre": "Ana"}]],
        [2, "Tarea B", "Desc", fecha, fecha, "Activo", [{"id": 1, "nombre": "Ana"}]],
    ]
    proyectos = [[1, "Proyecto", tareas, fecha, fecha, "Activo", [1], 1]]
    usuarios = {
        "ana": {"id": 1, "password": "123", "clearance": 2, "projects": []}
    }
    return proyectos, usuarios


def test_consultas_relacionadas():
    proyectos, usuarios = datos()
    assert len(tareas_por_estado(proyectos, "Activo")) == 1
    assert len(tareas_de_integrante(proyectos, 1)) == 2
    assert integrantes_unicos_proyecto(proyectos[0], usuarios) == ["Ana"]


def test_estadisticas_con_datos():
    proyectos, usuarios = datos()
    resumen = calcular_resumen_estadistico(proyectos, usuarios, [[1, "QA"]])
    assert resumen["totales"] == {
        "proyectos": 1,
        "tareas": 2,
        "integrantes": 1,
        "roles": 1,
    }
    assert resumen["porcentajes"]["tareas_finalizadas"] == 50
    assert resumen["promedios"]["tareas_por_proyecto"] == 2


def test_estadisticas_vacias_sin_division_por_cero():
    resumen = calcular_resumen_estadistico([], {}, [])
    assert resumen["porcentajes"]["tareas_finalizadas"] == 0
    assert resumen["promedios"]["tareas_por_proyecto"] == 0
    assert resumen["extremos_proyectos"] == {"maximo": [], "minimo": []}


def test_empates_en_extremos():
    fecha = datetime(2026, 1, 1)
    proyectos = [
        [1, "A", [], fecha, fecha, "Activo", [], None],
        [2, "B", [], fecha, fecha, "Activo", [], None],
    ]
    extremos = calcular_resumen_estadistico(proyectos, {}, [])["extremos_proyectos"]
    assert extremos["maximo"] == ["A", "B"]
    assert extremos["minimo"] == ["A", "B"]


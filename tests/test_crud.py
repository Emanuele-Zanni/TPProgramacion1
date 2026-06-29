from datetime import datetime

import pytest

from General.logica import (
    crear_integrante_logica,
    buscar_integrante_logica,
    crear_proyecto_logica,
    crear_tarea_logica,
    eliminar_integrante_logica,
    eliminar_proyecto_logica,
    eliminar_tarea_logica,
    modificar_proyecto_logica,
    modificar_tarea_logica,
)
from General.utilidades import buscar_posicion_por_id, obtener_proximo_id


INICIO = datetime(2026, 1, 1)
FIN = datetime(2026, 2, 1)


def test_crud_proyecto_modifica_campo_correcto():
    proyectos = []
    creado = crear_proyecto_logica(proyectos, "Proyecto Uno", INICIO, FIN)
    assert modificar_proyecto_logica(proyectos, creado[0], estado="Completado")
    assert proyectos[0][4] == FIN
    assert proyectos[0][5] == "Completado"


def test_proyecto_con_tareas_no_se_elimina():
    proyectos = []
    proyecto = crear_proyecto_logica(proyectos, "Proyecto Uno", INICIO, FIN)
    crear_tarea_logica(proyecto[2], "Tarea Uno", "Descripción", INICIO, FIN)
    with pytest.raises(ValueError):
        eliminar_proyecto_logica(proyectos, proyecto[0])


def test_crud_tarea_y_busqueda_inexistente():
    tareas = []
    primera = crear_tarea_logica(tareas, "Tarea Uno", "Descripción", INICIO, FIN)
    segunda = crear_tarea_logica(tareas, "Tarea Dos", "Descripción", INICIO, FIN)
    assert eliminar_tarea_logica(tareas, primera[0])
    assert modificar_tarea_logica(tareas, segunda[0], descripcion="Modificada")
    assert tareas[0][2] == "Modificada"
    assert buscar_posicion_por_id(tareas, 999) == -1


def test_id_no_se_reutiliza_por_posicion():
    registros = [[1, "A"], [4, "B"]]
    assert obtener_proximo_id(registros) == 5


def test_integrante_relacionado_no_se_elimina():
    usuarios = {}
    usuario = crear_integrante_logica(usuarios, "usuario", "1234")
    proyectos = [
        [1, "Proyecto", [], INICIO, FIN, "Activo", [usuario["id"]], usuario["id"]]
    ]
    with pytest.raises(ValueError):
        eliminar_integrante_logica(usuarios, "usuario", proyectos)
    assert buscar_integrante_logica(usuarios, usuario["id"])[0] == "usuario"

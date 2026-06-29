import json
from datetime import datetime

import pytest

from General.persistencia import (
    cargar_datos_json,
    cargar_roles_txt,
    crear_rol_txt,
    eliminar_rol_txt,
    guardar_datos_json,
    modificar_rol_txt,
)


def test_json_sobrevive_recarga(tmp_path):
    ruta = tmp_path / "datos.json"
    proyecto = [
        1,
        "Proyecto",
        [[1, "Tarea", "Desc", datetime(2026, 1, 1), datetime(2026, 1, 2), "Activo", []]],
        datetime(2026, 1, 1),
        datetime(2026, 2, 1),
        "Activo",
        [],
        None,
    ]
    guardar_datos_json(ruta, [proyecto], {"admin": {"id": 1}})
    datos = cargar_datos_json(ruta)
    assert datos["proyectos"][0][1] == "Proyecto"
    assert datos["proyectos"][0][2][0][3] == datetime(2026, 1, 1)


def test_json_inexistente_crea_estructura(tmp_path):
    ruta = tmp_path / "nuevo.json"
    assert cargar_datos_json(ruta) == {"proyectos": [], "usuarios": {}}
    assert json.loads(ruta.read_text(encoding="utf-8"))["proyectos"] == []


def test_json_mal_formado(tmp_path):
    ruta = tmp_path / "datos.json"
    ruta.write_text("{mal", encoding="utf-8")
    with pytest.raises(ValueError):
        cargar_datos_json(ruta)


def test_crud_roles_txt(tmp_path):
    ruta = tmp_path / "roles.txt"
    roles = cargar_roles_txt(ruta)
    rol = crear_rol_txt(roles, "desarrollador", ruta)
    assert modificar_rol_txt(roles, rol[0], "analista", ruta)
    assert cargar_roles_txt(ruta) == [[1, "Analista"]]
    assert eliminar_rol_txt(roles, rol[0], ruta)
    assert cargar_roles_txt(ruta) == []


def test_linea_txt_invalida_se_ignora(tmp_path):
    ruta = tmp_path / "roles.txt"
    ruta.write_text("incorrecta\n1|QA\n", encoding="utf-8")
    assert cargar_roles_txt(ruta) == [[1, "QA"]]


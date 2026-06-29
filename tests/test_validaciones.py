from datetime import datetime, timedelta

import pytest

from General.validaciones import (
    convertir_fecha,
    validar_estado_tarea,
    validar_nombre,
    validar_rango_fechas,
    validar_usuario,
)


def test_fecha_valida():
    fecha = datetime.now() + timedelta(days=1)
    assert convertir_fecha(fecha.strftime("%d/%m/%Y")) == datetime(
        fecha.year, fecha.month, fecha.day
    )


@pytest.mark.parametrize("fecha", ["31/02/2026", "1/02/2026", "texto", ""])
def test_fecha_invalida(fecha):
    with pytest.raises(ValueError):
        convertir_fecha(fecha)


def test_fecha_anterior_a_hoy():
    fecha = datetime.now() - timedelta(days=1)
    with pytest.raises(ValueError):
        convertir_fecha(fecha.strftime("%d/%m/%Y"))


def test_fecha_final_anterior():
    with pytest.raises(ValueError):
        validar_rango_fechas(datetime(2026, 2, 2), datetime(2026, 2, 1))


def test_nombre_y_usuario_con_regex():
    assert validar_nombre("Proyecto Uno") == "Proyecto Uno"
    assert validar_usuario("Usuario_1") == "usuario_1"
    with pytest.raises(ValueError):
        validar_usuario("1usuario")


def test_estado_invalido():
    with pytest.raises(ValueError):
        validar_estado_tarea("Cualquier texto")

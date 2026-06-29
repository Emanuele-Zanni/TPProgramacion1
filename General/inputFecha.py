"""Entrada interactiva de fechas usando la validación centralizada."""

from General.validaciones import convertir_fecha


def inputFecha(mode):
    modo = str(mode).strip().lower()
    if modo == "inicio":
        mensaje = "• Ingrese la fecha de inicio (DD/MM/AAAA): "
    elif modo == "final":
        mensaje = "• Ingrese la fecha de finalización (DD/MM/AAAA): "
    else:
        raise ValueError("El modo debe ser Inicio o Final.")

    fecha_texto = input(mensaje).strip()
    if fecha_texto in ("", "0"):
        return fecha_texto
    try:
        return convertir_fecha(fecha_texto)
    except (TypeError, ValueError):
        return None

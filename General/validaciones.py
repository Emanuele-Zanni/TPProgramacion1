"""Validaciones reutilizables sin dependencia de input() ni print()."""

from datetime import datetime
import re

from General.constantes import ESTADOS_PROYECTO, ESTADOS_TAREA


PATRON_FECHA = re.compile(r"^\d{2}/\d{2}/\d{4}$")
PATRON_NOMBRE = re.compile(r"^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9][A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9 _.-]{1,59}$")
PATRON_USUARIO = re.compile(r"^[a-zA-Z][a-zA-Z0-9_.]{2,24}$")


def convertir_fecha(fecha_texto):
    """Convierte dd/mm/aaaa a datetime o levanta ValueError."""
    if not isinstance(fecha_texto, str):
        raise TypeError("La fecha debe recibirse como texto.")
    fecha_texto = fecha_texto.strip()
    if PATRON_FECHA.fullmatch(fecha_texto) is None:
        raise ValueError("El formato debe ser dd/mm/aaaa.")
    fecha = datetime.strptime(fecha_texto, "%d/%m/%Y")
    validar_fecha_no_pasada(fecha)
    return fecha


def validar_fecha_no_pasada(fecha):
    if not isinstance(fecha, datetime):
        raise TypeError("La fecha debe ser un objeto datetime.")
    hoy = datetime.now().date()
    if fecha.date() < hoy:
        raise ValueError("La fecha no puede ser anterior al día de hoy.")
    return True


def validar_rango_fechas(fecha_inicio, fecha_final):
    if not isinstance(fecha_inicio, datetime) or not isinstance(fecha_final, datetime):
        raise TypeError("Las fechas deben ser objetos datetime.")
    if fecha_final < fecha_inicio:
        raise ValueError("La fecha final no puede ser anterior a la inicial.")
    return True


def validar_nombre(nombre, campo="nombre"):
    if not isinstance(nombre, str):
        raise TypeError(f"El {campo} debe ser texto.")
    nombre = " ".join(nombre.strip().split())
    if PATRON_NOMBRE.fullmatch(nombre) is None:
        raise ValueError(
            f"El {campo} debe tener entre 2 y 60 caracteres válidos."
        )
    return nombre


def validar_usuario(usuario):
    if not isinstance(usuario, str):
        raise TypeError("El usuario debe ser texto.")
    usuario = usuario.strip().lower()
    if PATRON_USUARIO.fullmatch(usuario) is None:
        raise ValueError(
            "El usuario debe empezar con una letra y tener de 3 a 25 caracteres."
        )
    return usuario


def validar_password(password):
    if not isinstance(password, str):
        raise TypeError("La contraseña debe ser texto.")
    password = password.strip()
    if len(password) < 3:
        raise ValueError("La contraseña debe tener al menos 3 caracteres.")
    return password


def validar_estado(estado, estados_validos):
    if estado not in estados_validos:
        raise ValueError(f"Estado inválido. Valores permitidos: {estados_validos}.")
    return estado


def validar_estado_proyecto(estado):
    return validar_estado(estado, ESTADOS_PROYECTO)


def validar_estado_tarea(estado):
    return validar_estado(estado, ESTADOS_TAREA)


def pedir_entero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensaje).strip())
            if minimo is not None and valor < minimo:
                raise ValueError
            if maximo is not None and valor > maximo:
                raise ValueError
            return valor
        except ValueError:
            print("Error: ingrese un número entero dentro del rango permitido.")


def pedir_confirmacion(mensaje="¿Confirma la operación? (s/n): "):
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta in ("s", "si", "sí"):
            return True
        if respuesta in ("n", "no"):
            return False
        print("Error: responda s o n.")

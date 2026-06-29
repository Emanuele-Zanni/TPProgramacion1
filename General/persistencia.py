"""Persistencia del sistema: roles en TXT y demás entidades en JSON."""

from datetime import datetime
import json
from pathlib import Path

from General.constantes import (
    CAMPOS_PROYECTO,
    CAMPOS_ROL,
    CAMPOS_TAREA,
    PROYECTO_FECHA_FINAL,
    PROYECTO_FECHA_INICIO,
    PROYECTO_TAREAS,
    SEPARADOR_ROLES,
    TAREA_FECHA_FINAL,
    TAREA_FECHA_INICIO,
)
from General.utilidades import buscar_posicion_por_id, obtener_proximo_id
from General.validaciones import validar_nombre


RUTA_DATOS_JSON = Path("data/datos.json")
RUTA_ROLES_TXT = Path("data/roles.txt")


def estructura_inicial():
    return {"proyectos": [], "usuarios": {}}


def _fecha_a_texto(fecha):
    if isinstance(fecha, datetime):
        return fecha.strftime("%d/%m/%Y")
    return str(fecha)


def _fecha_desde_texto(fecha):
    if isinstance(fecha, datetime):
        return fecha
    return datetime.strptime(fecha, "%d/%m/%Y")


def _serializar_tarea(tarea):
    copia = list(tarea)
    copia[TAREA_FECHA_INICIO] = _fecha_a_texto(copia[TAREA_FECHA_INICIO])
    copia[TAREA_FECHA_FINAL] = _fecha_a_texto(copia[TAREA_FECHA_FINAL])
    return copia


def _serializar_proyecto(proyecto):
    copia = list(proyecto)
    copia[PROYECTO_TAREAS] = [
        _serializar_tarea(tarea) for tarea in proyecto[PROYECTO_TAREAS]
    ]
    copia[PROYECTO_FECHA_INICIO] = _fecha_a_texto(copia[PROYECTO_FECHA_INICIO])
    copia[PROYECTO_FECHA_FINAL] = _fecha_a_texto(copia[PROYECTO_FECHA_FINAL])
    return copia


def _deserializar_tarea(tarea):
    if not isinstance(tarea, list) or len(tarea) != CAMPOS_TAREA:
        raise ValueError("Se encontró una tarea con estructura inválida.")
    copia = list(tarea)
    copia[TAREA_FECHA_INICIO] = _fecha_desde_texto(copia[TAREA_FECHA_INICIO])
    copia[TAREA_FECHA_FINAL] = _fecha_desde_texto(copia[TAREA_FECHA_FINAL])
    return copia


def _deserializar_proyecto(proyecto):
    if not isinstance(proyecto, list) or len(proyecto) != CAMPOS_PROYECTO:
        raise ValueError("Se encontró un proyecto con estructura inválida.")
    copia = list(proyecto)
    copia[PROYECTO_TAREAS] = [
        _deserializar_tarea(tarea) for tarea in copia[PROYECTO_TAREAS]
    ]
    copia[PROYECTO_FECHA_INICIO] = _fecha_desde_texto(
        copia[PROYECTO_FECHA_INICIO]
    )
    copia[PROYECTO_FECHA_FINAL] = _fecha_desde_texto(copia[PROYECTO_FECHA_FINAL])
    return copia


def guardar_datos_json(ruta, proyectos, usuarios):
    ruta = Path(ruta)
    datos = {
        "proyectos": [_serializar_proyecto(proyecto) for proyecto in proyectos],
        "usuarios": usuarios,
    }
    try:
        ruta.parent.mkdir(parents=True, exist_ok=True)
        with ruta.open("w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        return True
    except (PermissionError, OSError) as error:
        raise OSError(f"No se pudieron guardar los datos: {error}") from error


def cargar_datos_json(ruta):
    ruta = Path(ruta)
    try:
        with ruta.open("r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        guardar_datos_json(ruta, [], {})
        return estructura_inicial()
    except json.JSONDecodeError as error:
        raise ValueError("El archivo JSON está vacío o mal formado.") from error
    except (PermissionError, OSError) as error:
        raise OSError(f"No se pudieron cargar los datos: {error}") from error

    if not isinstance(datos, dict):
        raise ValueError("La raíz del JSON debe ser un objeto.")
    proyectos = datos.get("proyectos", [])
    usuarios = datos.get("usuarios", {})
    if not isinstance(proyectos, list) or not isinstance(usuarios, dict):
        raise ValueError("El JSON no contiene las colecciones esperadas.")
    return {
        "proyectos": [_deserializar_proyecto(item) for item in proyectos],
        "usuarios": usuarios,
    }


def guardar_roles_txt(ruta, roles):
    ruta = Path(ruta)
    try:
        ruta.parent.mkdir(parents=True, exist_ok=True)
        with ruta.open("w", encoding="utf-8") as archivo:
            for rol in roles:
                if len(rol) != CAMPOS_ROL:
                    raise ValueError("Rol con estructura inválida.")
                archivo.write(f"{rol[0]}{SEPARADOR_ROLES}{rol[1]}\n")
        return True
    except (PermissionError, OSError) as error:
        raise OSError(f"No se pudieron guardar los roles: {error}") from error


def cargar_roles_txt(ruta):
    ruta = Path(ruta)
    roles = []
    try:
        with ruta.open("r", encoding="utf-8") as archivo:
            for numero_linea, linea in enumerate(archivo, start=1):
                linea = linea.strip()
                if linea == "":
                    continue
                partes = linea.split(SEPARADOR_ROLES)
                if len(partes) != CAMPOS_ROL or not partes[0].isdigit():
                    continue
                rol = [int(partes[0]), partes[1].strip()]
                if rol[1] != "":
                    roles.append(rol)
    except FileNotFoundError:
        guardar_roles_txt(ruta, [])
    except (PermissionError, OSError) as error:
        raise OSError(f"No se pudieron cargar los roles: {error}") from error
    return roles


def crear_rol_txt(roles, nombre, ruta):
    nombre = validar_nombre(nombre, "nombre del rol").title()
    if nombre.lower() in {rol[1].lower() for rol in roles}:
        raise ValueError("El rol ya existe.")
    nuevo = [obtener_proximo_id(roles), nombre]
    roles.append(nuevo)
    guardar_roles_txt(ruta, roles)
    return nuevo


def buscar_rol_txt(roles, rol_id):
    posicion = buscar_posicion_por_id(roles, rol_id)
    return None if posicion == -1 else roles[posicion]


def modificar_rol_txt(roles, rol_id, nombre, ruta):
    posicion = buscar_posicion_por_id(roles, rol_id)
    if posicion == -1:
        return False
    nombre = validar_nombre(nombre, "nombre del rol").title()
    if any(
        indice != posicion and rol[1].lower() == nombre.lower()
        for indice, rol in enumerate(roles)
    ):
        raise ValueError("El rol ya existe.")
    roles[posicion][1] = nombre
    guardar_roles_txt(ruta, roles)
    return True


def eliminar_rol_txt(roles, rol_id, ruta):
    posicion = buscar_posicion_por_id(roles, rol_id)
    if posicion == -1:
        return False
    roles.pop(posicion)
    guardar_roles_txt(ruta, roles)
    return True

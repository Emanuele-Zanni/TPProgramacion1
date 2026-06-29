"""Lógica CRUD pura de las entidades principales."""

from General.constantes import (
    ESTADOS_PROYECTO,
    ESTADOS_TAREA,
    PROYECTO_ESTADO,
    PROYECTO_FECHA_FINAL,
    PROYECTO_FECHA_INICIO,
    PROYECTO_INTEGRANTES,
    PROYECTO_NOMBRE,
    PROYECTO_OWNER,
    PROYECTO_TAREAS,
    TAREA_ASIGNADOS,
    TAREA_DESCRIPCION,
    TAREA_ESTADO,
    TAREA_FECHA_FINAL,
    TAREA_FECHA_INICIO,
    TAREA_NOMBRE,
)
from General.utilidades import buscar_posicion_por_id, obtener_proximo_id
from General.validaciones import (
    validar_estado_proyecto,
    validar_estado_tarea,
    validar_nombre,
    validar_password,
    validar_rango_fechas,
    validar_usuario,
)


def crear_proyecto_logica(
    proyectos, nombre, fecha_inicio, fecha_final, estado="Activo", owner_id=None
):
    nombre = validar_nombre(nombre, "nombre del proyecto")
    validar_rango_fechas(fecha_inicio, fecha_final)
    validar_estado_proyecto(estado)
    if any(proyecto[PROYECTO_NOMBRE].lower() == nombre.lower() for proyecto in proyectos):
        raise ValueError("Ya existe un proyecto con ese nombre.")
    integrantes = [] if owner_id is None else [owner_id]
    proyecto = [
        obtener_proximo_id(proyectos),
        nombre,
        [],
        fecha_inicio,
        fecha_final,
        estado,
        integrantes,
        owner_id,
    ]
    proyectos.append(proyecto)
    return proyecto


def modificar_proyecto_logica(proyectos, proyecto_id, **cambios):
    posicion = buscar_posicion_por_id(proyectos, proyecto_id)
    if posicion == -1:
        return False
    proyecto = proyectos[posicion]
    nombre = validar_nombre(
        cambios.get("nombre", proyecto[PROYECTO_NOMBRE]), "nombre del proyecto"
    )
    fecha_inicio = cambios.get("fecha_inicio", proyecto[PROYECTO_FECHA_INICIO])
    fecha_final = cambios.get("fecha_final", proyecto[PROYECTO_FECHA_FINAL])
    estado = cambios.get("estado", proyecto[PROYECTO_ESTADO])
    validar_rango_fechas(fecha_inicio, fecha_final)
    validar_estado_proyecto(estado)
    proyecto[PROYECTO_NOMBRE] = nombre
    proyecto[PROYECTO_FECHA_INICIO] = fecha_inicio
    proyecto[PROYECTO_FECHA_FINAL] = fecha_final
    proyecto[PROYECTO_ESTADO] = estado
    return True


def eliminar_proyecto_logica(proyectos, proyecto_id):
    posicion = buscar_posicion_por_id(proyectos, proyecto_id)
    if posicion == -1:
        return False
    if len(proyectos[posicion][PROYECTO_TAREAS]) > 0:
        raise ValueError("No se puede eliminar un proyecto que contiene tareas.")
    proyectos.pop(posicion)
    return True


def crear_tarea_logica(
    tareas, nombre, descripcion, fecha_inicio, fecha_final, estado="Activo"
):
    nombre = validar_nombre(nombre, "nombre de la tarea")
    if not isinstance(descripcion, str) or descripcion.strip() == "":
        raise ValueError("La descripción es obligatoria.")
    validar_rango_fechas(fecha_inicio, fecha_final)
    validar_estado_tarea(estado)
    tarea = [
        obtener_proximo_id(tareas),
        nombre,
        descripcion.strip(),
        fecha_inicio,
        fecha_final,
        estado,
        [],
    ]
    tareas.append(tarea)
    return tarea


def modificar_tarea_logica(tareas, tarea_id, **cambios):
    posicion = buscar_posicion_por_id(tareas, tarea_id)
    if posicion == -1:
        return False
    tarea = tareas[posicion]
    nombre = validar_nombre(
        cambios.get("nombre", tarea[TAREA_NOMBRE]), "nombre de la tarea"
    )
    descripcion = cambios.get("descripcion", tarea[TAREA_DESCRIPCION])
    if not isinstance(descripcion, str) or descripcion.strip() == "":
        raise ValueError("La descripción es obligatoria.")
    fecha_inicio = cambios.get("fecha_inicio", tarea[TAREA_FECHA_INICIO])
    fecha_final = cambios.get("fecha_final", tarea[TAREA_FECHA_FINAL])
    estado = cambios.get("estado", tarea[TAREA_ESTADO])
    validar_rango_fechas(fecha_inicio, fecha_final)
    validar_estado_tarea(estado)
    tarea[TAREA_NOMBRE] = nombre
    tarea[TAREA_DESCRIPCION] = descripcion.strip()
    tarea[TAREA_FECHA_INICIO] = fecha_inicio
    tarea[TAREA_FECHA_FINAL] = fecha_final
    tarea[TAREA_ESTADO] = estado
    return True


def eliminar_tarea_logica(tareas, tarea_id):
    posicion = buscar_posicion_por_id(tareas, tarea_id)
    if posicion == -1:
        return False
    tareas.pop(posicion)
    return True


def asignar_integrante_tarea(tarea, usuario_id, nombre):
    asignados = tarea[TAREA_ASIGNADOS]
    if any(
        (item.get("id") if isinstance(item, dict) else item) == usuario_id
        for item in asignados
    ):
        return False
    asignados.append({"id": usuario_id, "nombre": nombre})
    return True


def crear_integrante_logica(usuarios, usuario, password, clearance=1):
    usuario = validar_usuario(usuario)
    password = validar_password(password)
    if usuario in usuarios:
        raise ValueError("El usuario ya existe.")
    siguiente_id = max(
        (datos.get("id", 0) for datos in usuarios.values()), default=0
    ) + 1
    usuarios[usuario] = {
        "id": siguiente_id,
        "password": password,
        "clearance": int(clearance),
        "projects": [],
    }
    return usuarios[usuario]


def modificar_integrante_logica(usuarios, usuario, nuevo_usuario=None, clearance=None):
    if usuario not in usuarios:
        return False
    destino = usuario
    if nuevo_usuario is not None:
        destino = validar_usuario(nuevo_usuario)
        if destino != usuario and destino in usuarios:
            raise ValueError("El nuevo usuario ya existe.")
        usuarios[destino] = usuarios.pop(usuario)
    if clearance is not None:
        usuarios[destino]["clearance"] = int(clearance)
    return destino


def eliminar_integrante_logica(usuarios, usuario, proyectos):
    if usuario not in usuarios:
        return False
    usuario_id = usuarios[usuario]["id"]
    relacionado = any(
        usuario_id in proyecto[PROYECTO_INTEGRANTES]
        or proyecto[PROYECTO_OWNER] == usuario_id
        for proyecto in proyectos
    )
    if relacionado:
        raise ValueError("No se puede eliminar un integrante asignado a proyectos.")
    del usuarios[usuario]
    return True


def buscar_integrante_logica(usuarios, usuario_id):
    for nombre, datos in usuarios.items():
        if datos.get("id") == usuario_id:
            return nombre, datos
    return None


def autenticar(usuarios, usuario, password):
    usuario = usuario.strip().lower()
    return usuario in usuarios and usuarios[usuario].get("password") == password


def estados_disponibles():
    return ESTADOS_PROYECTO, ESTADOS_TAREA

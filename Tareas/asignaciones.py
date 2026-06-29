"""Helpers de asignacion y sincronizacion de tareas con usuarios."""


def obtener_nombre_integrante_asignado(integrante):
    if isinstance(integrante, dict):
        if "nombre" in integrante:
            return str(integrante["nombre"])
        if "user" in integrante:
            return str(integrante["user"])
        if "username" in integrante:
            return str(integrante["username"])
        if "id" in integrante:
            return f"Usuario {integrante['id']}"

    if isinstance(integrante, (list, tuple)) and len(integrante) > 1:
        return str(integrante[1])

    return str(integrante)


def resumir_integrantes_asignados(integrantes_asignados):
    if len(integrantes_asignados) == 0:
        return "Ninguno"
    if len(integrantes_asignados) == 1:
        return obtener_nombre_integrante_asignado(integrantes_asignados[0])
    return f"{len(integrantes_asignados)} personas"


def obtener_integrantes_reales_proyecto(proyecto, ListaUsuarios):
    integrantes = []
    integrantes_ids = proyecto[6] if len(proyecto) > 6 else []

    for usuario_id in integrantes_ids:
        for nombre_usuario, datos_usuario in ListaUsuarios.items():
            if datos_usuario.get("id") == usuario_id:
                integrantes.append(
                    {
                        "id": usuario_id,
                        "nombre": nombre_usuario.capitalize(),
                        "datos": datos_usuario,
                    }
                )
                break

    return integrantes


def obtener_id_usuario_logueado(ListaUsuarios, credencial):
    usuario_logueado = credencial.get("user")

    for nombre_usuario, datos_usuario in ListaUsuarios.items():
        if nombre_usuario == usuario_logueado:
            return datos_usuario.get("id"), nombre_usuario.capitalize()

    return None, None


def sincronizar_tarea_en_usuario(ListaUsuarios, project_id, task_id, usuario_id):
    for _, datos_usuario in ListaUsuarios.items():
        if datos_usuario.get("id") != usuario_id:
            continue

        for proyecto_usuario in datos_usuario.get("projects", []):
            if proyecto_usuario.get("projectId") == project_id:
                tareas_usuario = proyecto_usuario.setdefault("tareas", [])
                if task_id not in tareas_usuario:
                    tareas_usuario.append(task_id)
                return


def desincronizar_tarea_en_usuario(
    ListaUsuarios, project_id, task_id, usuario_id
):
    for _, datos_usuario in ListaUsuarios.items():
        if datos_usuario.get("id") != usuario_id:
            continue

        for proyecto_usuario in datos_usuario.get("projects", []):
            if proyecto_usuario.get("projectId") == project_id:
                tareas_usuario = proyecto_usuario.setdefault("tareas", [])
                if task_id in tareas_usuario:
                    tareas_usuario.remove(task_id)
                return


def integrante_esta_asignado(asignados_actuales, usuario_id):
    for asignado in asignados_actuales:
        if isinstance(asignado, dict) and asignado.get("id") == usuario_id:
            return True
        if asignado == usuario_id:
            return True
    return False


def alternar_asignacion_usuario_logueado(
    tarea, proyecto, ListaUsuarios, credencial
):
    usuario_id, nombre_usuario = obtener_id_usuario_logueado(
        ListaUsuarios, credencial
    )

    if usuario_id is None:
        print()
        input("\033[31m[ERROR] No se pudo identificar al usuario logueado.\033[0m")
        return

    asignados_actuales = tarea[6] if len(tarea) > 6 else []

    if integrante_esta_asignado(asignados_actuales, usuario_id):
        tarea[6] = [
            asignado
            for asignado in asignados_actuales
            if not (
                (isinstance(asignado, dict) and asignado.get("id") == usuario_id)
                or asignado == usuario_id
            )
        ]
        desincronizar_tarea_en_usuario(
            ListaUsuarios, proyecto[0], tarea[0], usuario_id
        )
        print()
        input("\033[92m[EXITO] Dejaste la tarea correctamente.\033[0m")
        return

    tarea[6].append({"id": usuario_id, "nombre": nombre_usuario})
    sincronizar_tarea_en_usuario(ListaUsuarios, proyecto[0], tarea[0], usuario_id)
    print()
    input("\033[92m[EXITO] Te asignaste la tarea correctamente.\033[0m")

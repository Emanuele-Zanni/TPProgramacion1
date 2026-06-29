from datetime import datetime

from General.clearConsole import clearConsole
from General.formato import imprimir_tabla, imprimir_titulo
from Proyectos.funciones import mostrarListaProyectos


def normalizar_estado(estado):
    estado = str(estado).strip().lower()
    if estado in ["completado", "completa"]:
        return "Completado"
    if estado == "expirado":
        return "Expirado"
    return "Activo"


def obtener_nombre_owner(ListaUsuarios, owner_id):
    for nombre_usuario, datos_usuario in ListaUsuarios.items():
        if datos_usuario.get("id") == owner_id:
            return nombre_usuario.capitalize()
    return "Sin owner"


def recolectar_tareas_portafolio(ListaProyectos):
    tareas = []
    for proyecto in ListaProyectos:
        for tarea in proyecto[2]:
            tareas.append((proyecto, tarea))
    return tareas


def calcular_metricas_tareas(ListaProyectos):
    hoy = datetime.now()
    metricas = {
        "total": 0,
        "activas": 0,
        "completadas": 0,
        "expiradas": 0,
        "vencidas": 0,
        "sin_asignar": 0,
    }

    for _, tarea in recolectar_tareas_portafolio(ListaProyectos):
        estado = normalizar_estado(tarea[5])
        metricas["total"] += 1

        if estado == "Activo":
            metricas["activas"] += 1
        elif estado == "Completado":
            metricas["completadas"] += 1
        elif estado == "Expirado":
            metricas["expiradas"] += 1

        if estado != "Completado" and tarea[4] < hoy:
            metricas["vencidas"] += 1

        asignados = tarea[6] if len(tarea) > 6 else []
        if len(asignados) == 0:
            metricas["sin_asignar"] += 1

    return metricas


def calcular_metricas_proyecto(proyecto):
    hoy = datetime.now()
    tareas = proyecto[2]
    total_tareas = len(tareas)
    tareas_activas = 0
    tareas_completadas = 0
    tareas_expiradas = 0
    tareas_vencidas = 0
    tareas_sin_asignar = 0

    for tarea in tareas:
        estado = normalizar_estado(tarea[5])
        if estado == "Activo":
            tareas_activas += 1
        elif estado == "Completado":
            tareas_completadas += 1
        elif estado == "Expirado":
            tareas_expiradas += 1

        if estado != "Completado" and tarea[4] < hoy:
            tareas_vencidas += 1

        asignados = tarea[6] if len(tarea) > 6 else []
        if len(asignados) == 0:
            tareas_sin_asignar += 1

    progreso = 0
    if total_tareas > 0:
        progreso = round((tareas_completadas / total_tareas) * 100)

    duracion = (proyecto[4] - proyecto[3]).days

    return {
        "total_tareas": total_tareas,
        "tareas_activas": tareas_activas,
        "tareas_completadas": tareas_completadas,
        "tareas_expiradas": tareas_expiradas,
        "tareas_vencidas": tareas_vencidas,
        "tareas_sin_asignar": tareas_sin_asignar,
        "integrantes": len(proyecto[6]) if len(proyecto) > 6 else 0,
        "progreso": progreso,
        "duracion": duracion,
    }


def construir_stats_integrantes(ListaUsuarios, ListaProyectos):
    tareas_por_usuario = {}
    ownership_por_usuario = {}

    for nombre_usuario, datos_usuario in ListaUsuarios.items():
        usuario_id = datos_usuario.get("id")
        tareas_por_usuario[usuario_id] = {
            "activas": 0,
            "completadas": 0,
            "expiradas": 0,
            "total": 0,
        }
        ownership_por_usuario[usuario_id] = 0

    for proyecto in ListaProyectos:
        owner_id = proyecto[7] if len(proyecto) > 7 else None
        if owner_id in ownership_por_usuario:
            ownership_por_usuario[owner_id] += 1

        for tarea in proyecto[2]:
            estado = normalizar_estado(tarea[5])
            asignados = tarea[6] if len(tarea) > 6 else []
            for asignado in asignados:
                usuario_id = asignado.get("id") if isinstance(asignado, dict) else asignado
                if usuario_id not in tareas_por_usuario:
                    continue
                tareas_por_usuario[usuario_id]["total"] += 1
                if estado == "Activo":
                    tareas_por_usuario[usuario_id]["activas"] += 1
                elif estado == "Completado":
                    tareas_por_usuario[usuario_id]["completadas"] += 1
                elif estado == "Expirado":
                    tareas_por_usuario[usuario_id]["expiradas"] += 1

    filas = []
    for nombre_usuario, datos_usuario in ListaUsuarios.items():
        usuario_id = datos_usuario.get("id")
        proyectos = datos_usuario.get("projects", [])
        filas.append([
            nombre_usuario.capitalize(),
            datos_usuario.get("clearance", ""),
            len(proyectos),
            tareas_por_usuario[usuario_id]["total"],
            tareas_por_usuario[usuario_id]["activas"],
            tareas_por_usuario[usuario_id]["completadas"],
            ownership_por_usuario[usuario_id],
        ])

    filas.sort(key=lambda fila: (-fila[3], -fila[5], fila[0]))
    return filas


def construir_stats_roles(ListaRoles, ListaUsuarios):
    uso_roles = {}
    for rol in ListaRoles:
        uso_roles[rol[1]] = 0

    for _, datos_usuario in ListaUsuarios.items():
        for proyecto in datos_usuario.get("projects", []):
            rol = proyecto.get("rol", "Sin rol")
            uso_roles[rol] = uso_roles.get(rol, 0) + 1

    filas = []
    for rol in ListaRoles:
        filas.append([rol[0], rol[1], uso_roles.get(rol[1], 0)])

    extras = [rol for rol in uso_roles.keys() if rol not in [item[1] for item in ListaRoles]]
    siguiente_id = len(ListaRoles) + 1
    for rol in extras:
        filas.append([siguiente_id, rol, uso_roles[rol]])
        siguiente_id += 1

    return filas


def ver_StatsProyectos(ListaProyectos, ListaUsuarios):
    while True:
        clearConsole()
        print("\033[33m[Menu principal > *Stats > Proyectos*]\033[0m")
        print()
        imprimir_titulo("Stats de Proyectos")

        proyectos_activos = sum(1 for proyecto in ListaProyectos if proyecto[5] == "Activo")
        proyectos_completados = sum(1 for proyecto in ListaProyectos if proyecto[5] == "Completado")
        proyectos_expirados = sum(1 for proyecto in ListaProyectos if proyecto[5] == "Expirado")
        metricas_tareas = calcular_metricas_tareas(ListaProyectos)

        imprimir_tabla(
            [
                {"titulo": "Proyectos", "min": 10, "peso": 1},
                {"titulo": "Activos", "min": 10, "peso": 1},
                {"titulo": "Completados", "min": 12, "peso": 1},
                {"titulo": "Expirados", "min": 10, "peso": 1},
                {"titulo": "Tareas", "min": 8, "peso": 1},
                {"titulo": "Vencidas", "min": 10, "peso": 1},
            ],
            [[len(ListaProyectos), proyectos_activos, proyectos_completados, proyectos_expirados, metricas_tareas["total"], metricas_tareas["vencidas"]]]
        )

        filas_proyectos = []
        for proyecto in ListaProyectos:
            metricas = calcular_metricas_proyecto(proyecto)
            filas_proyectos.append([
                proyecto[0],
                proyecto[1],
                proyecto[5],
                metricas["integrantes"],
                metricas["total_tareas"],
                f"{metricas['progreso']}%",
                metricas["tareas_vencidas"],
                obtener_nombre_owner(ListaUsuarios, proyecto[7] if len(proyecto) > 7 else None),
            ])

        imprimir_tabla(
            [
                {"titulo": "ID", "min": 4, "peso": 1},
                {"titulo": "Proyecto", "min": 18, "peso": 4},
                {"titulo": "Estado", "min": 10, "peso": 1},
                {"titulo": "Integrantes", "min": 11, "peso": 1},
                {"titulo": "Tareas", "min": 8, "peso": 1},
                {"titulo": "Progreso", "min": 10, "peso": 1},
                {"titulo": "Vencidas", "min": 10, "peso": 1},
                {"titulo": "Owner", "min": 12, "peso": 2},
            ],
            filas_proyectos
        )

        print("1. Ver detalle de un proyecto")
        print("0. Volver")
        opcion = input("Seleccione una opcion: ")

        if opcion == "0":
            return
        if opcion != "1":
            input("\033[31m[ERROR] Opcion invalida. Intente nuevamente.\033[0m")
            continue

        clearConsole()
        print("\033[33m[Menu principal > Stats > Proyectos > *Seleccionar Proyecto*]\033[0m")
        print()
        mostrarListaProyectos(ListaProyectos)
        project_id = input("Ingrese el ID del proyecto (0 para volver): ")

        if project_id == "0":
            continue
        if project_id.isdigit() == False:
            input("\033[31m[ERROR] El ID debe ser numerico.\033[0m")
            continue

        project_id = int(project_id)
        proyecto = None
        for item in ListaProyectos:
            if item[0] == project_id:
                proyecto = item
                break

        if proyecto is None:
            input("\033[31m[ERROR] El proyecto no existe.\033[0m")
            continue

        metricas = calcular_metricas_proyecto(proyecto)
        clearConsole()
        print("\033[33m[Menu principal > Stats > Proyectos > *Detalle de Proyecto*]\033[0m")
        print()
        imprimir_titulo(f"Stats: {proyecto[1]}")
        imprimir_tabla(
            [
                {"titulo": "Integrantes", "min": 11, "peso": 1},
                {"titulo": "Tareas", "min": 8, "peso": 1},
                {"titulo": "Activas", "min": 9, "peso": 1},
                {"titulo": "Completadas", "min": 12, "peso": 1},
                {"titulo": "Expiradas", "min": 10, "peso": 1},
                {"titulo": "Vencidas", "min": 9, "peso": 1},
                {"titulo": "Progreso", "min": 9, "peso": 1},
                {"titulo": "Duracion(d)", "min": 11, "peso": 1},
            ],
            [[
                metricas["integrantes"],
                metricas["total_tareas"],
                metricas["tareas_activas"],
                metricas["tareas_completadas"],
                metricas["tareas_expiradas"],
                metricas["tareas_vencidas"],
                f"{metricas['progreso']}%",
                metricas["duracion"],
            ]]
        )

        filas_asignacion = []
        for integrante_id in proyecto[6]:
            nombre = obtener_nombre_owner(ListaUsuarios, integrante_id)
            tareas_asignadas = 0
            for tarea in proyecto[2]:
                asignados = tarea[6] if len(tarea) > 6 else []
                for asignado in asignados:
                    asignado_id = asignado.get("id") if isinstance(asignado, dict) else asignado
                    if asignado_id == integrante_id:
                        tareas_asignadas += 1
                        break
            filas_asignacion.append([integrante_id, nombre, tareas_asignadas])

        if len(filas_asignacion) > 0:
            imprimir_tabla(
                [
                    {"titulo": "ID", "min": 4, "peso": 1},
                    {"titulo": "Integrante", "min": 18, "peso": 3},
                    {"titulo": "Tareas Asignadas", "min": 15, "peso": 1},
                ],
                filas_asignacion
            )

        input("Presione enter para volver...")


def ver_StatsIntegrantes(ListaUsuarios, ListaProyectos):
    clearConsole()
    print("\033[33m[Menu principal > *Stats > Integrantes*]\033[0m")
    print()
    imprimir_titulo("Stats de Integrantes")

    filas = construir_stats_integrantes(ListaUsuarios, ListaProyectos)
    imprimir_tabla(
        [
            {"titulo": "Usuario", "min": 16, "peso": 3},
            {"titulo": "Nivel", "min": 7, "peso": 1},
            {"titulo": "Proyectos", "min": 9, "peso": 1},
            {"titulo": "Tareas", "min": 7, "peso": 1},
            {"titulo": "Activas", "min": 8, "peso": 1},
            {"titulo": "Completadas", "min": 11, "peso": 1},
            {"titulo": "Ownerships", "min": 10, "peso": 1},
        ],
        filas
    )
    input("Presione enter para volver...")


def ver_StatsRoles(ListaRoles, ListaUsuarios):
    clearConsole()
    print("\033[33m[Menu principal > *Stats > Roles*]\033[0m")
    print()
    imprimir_titulo("Stats de Roles")
    filas = construir_stats_roles(ListaRoles, ListaUsuarios)
    imprimir_tabla(
        [
            {"titulo": "ID", "min": 4, "peso": 1},
            {"titulo": "Rol", "min": 18, "peso": 3},
            {"titulo": "Uso en Proyectos", "min": 15, "peso": 1},
        ],
        filas
    )
    input("Presione enter para volver...")


def ver_StatsTotal(ListaProyectos, ListaUsuarios, ListaRoles):
    clearConsole()
    print("\033[33m[Menu principal > *Stats > Resumen Ejecutivo*]\033[0m")
    print()
    imprimir_titulo("Resumen Ejecutivo")

    metricas_tareas = calcular_metricas_tareas(ListaProyectos)
    proyectos_activos = sum(1 for proyecto in ListaProyectos if proyecto[5] == "Activo")
    proyectos_completados = sum(1 for proyecto in ListaProyectos if proyecto[5] == "Completado")
    managers = sum(1 for _, datos in ListaUsuarios.items() if datos.get("clearance") == 2)
    owners = sum(1 for proyecto in ListaProyectos if len(proyecto) > 7 and proyecto[7] is not None)

    imprimir_tabla(
        [
            {"titulo": "Proyectos", "min": 10, "peso": 1},
            {"titulo": "Activos", "min": 9, "peso": 1},
            {"titulo": "Completados", "min": 12, "peso": 1},
            {"titulo": "Usuarios", "min": 9, "peso": 1},
            {"titulo": "Managers", "min": 9, "peso": 1},
            {"titulo": "Owners", "min": 8, "peso": 1},
        ],
        [[len(ListaProyectos), proyectos_activos, proyectos_completados, len(ListaUsuarios), managers, owners]]
    )

    imprimir_tabla(
        [
            {"titulo": "Tareas Totales", "min": 12, "peso": 1},
            {"titulo": "Activas", "min": 8, "peso": 1},
            {"titulo": "Completadas", "min": 11, "peso": 1},
            {"titulo": "Expiradas", "min": 10, "peso": 1},
            {"titulo": "Vencidas", "min": 9, "peso": 1},
            {"titulo": "Sin Asignar", "min": 11, "peso": 1},
        ],
        [[
            metricas_tareas["total"],
            metricas_tareas["activas"],
            metricas_tareas["completadas"],
            metricas_tareas["expiradas"],
            metricas_tareas["vencidas"],
            metricas_tareas["sin_asignar"],
        ]]
    )

    filas_carga = construir_stats_integrantes(ListaUsuarios, ListaProyectos)[:5]
    if len(filas_carga) > 0:
        imprimir_titulo("Top Carga de Trabajo")
        imprimir_tabla(
            [
                {"titulo": "Usuario", "min": 16, "peso": 3},
                {"titulo": "Tareas", "min": 7, "peso": 1},
                {"titulo": "Activas", "min": 8, "peso": 1},
                {"titulo": "Completadas", "min": 11, "peso": 1},
                {"titulo": "Proyectos", "min": 9, "peso": 1},
            ],
            [[fila[0], fila[3], fila[4], fila[5], fila[2]] for fila in filas_carga]
        )

    input("Presione enter para volver...")

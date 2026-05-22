def ver_StatsProyectos(ListaProyectos):
    print("=== Stats de Proyectos ===")
    print()

    print(f"{'ID':<5}{'Nombre':<25}{'Inicio':<15}{'Final':<15}{'Estado':<15}{'Tareas':<10}")
    print("-" * 85)

    for proyecto in ListaProyectos:

        id_ = proyecto[0]
        nombre = proyecto[1]

        inicio = proyecto[3].strftime("%d/%m/%Y")
        final = proyecto[4].strftime("%d/%m/%Y")

        estado = proyecto[5]
        tareas = len(proyecto[2])

        print(f"{id_:<5}{nombre:<25}{inicio:<15}{final:<15}{estado:<15}{tareas:<10}")

def ver_StatsIntegrantes(ListaUsuarios):
    print("=== Stats de Integrantes ===")
    print()

    print(f"{'Usuario':<20}{'Rol':<20}{'Nivel':<10}{'Tareas':<10}")
    print("-" * 60)

    for usuario in ListaUsuarios:
        rol = ListaUsuarios[usuario]["rol"]
        nivel = ListaUsuarios[usuario]["clearance"]
        tareas = len(ListaUsuarios[usuario]["tareas"])

        print(f"{usuario:<20}{rol:<20}{nivel:<10}{tareas:<10}")

def ver_StatsRoles(ListaRoles):
    print("=== Stats de Roles ===")
    print()

    print(f"{'ID':<5}{'Rol':<25}")
    print("-" * 30)

    for rol in ListaRoles:
        id_ = rol[0]
        nombre = rol[1]

        print(f"{id_:<5}{nombre:<25}") 

def ver_StatsTotal(ListaProyectos, ListaUsuarios, ListaRoles):

    proyectosActivos = 0
    totalTareas = 0

    for proyecto in ListaProyectos:

        if proyecto[5] == "Activo":
            proyectosActivos += 1

        totalTareas += len(proyecto[2])

    print("=== Información General ===")
    print()
    print(f"Cantidad de proyectos: {len(ListaProyectos)}")
    print(f"Cantidad de usuarios: {len(ListaUsuarios)}")
    print(f"Cantidad de roles: {len(ListaRoles)}")
    print(f"Proyectos activos: {proyectosActivos}")
    print(f"Cantidad total de tareas: {totalTareas}")
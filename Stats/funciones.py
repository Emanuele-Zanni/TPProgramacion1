from General.clearConsole import clearConsole
from Proyectos.funciones import mostrarListaProyectos

def ver_StatsProyectos(ListaProyectos):
    p1 = True
    while p1:   
        p2 = True
        clearConsole()
        print("Menu > Stats > *Stats de Proyectos*")
        print()
        print("=== Stats de Proyectos ===")
        print()
        print(f"{'Activos':<10}{'Completados':<15}{'Expirados':<15}{'TareasTotales':<10}")
        print("-" * 53)

        ProyectosActivos = 0
        ProyectosCompletados = 0
        ProyectosExpirados = 0
    
    
        for proyecto in ListaProyectos:
            
            estado = proyecto[5]

            if estado == "Activo":
                ProyectosActivos += 1
            elif estado == "Completado":
                ProyectosCompletados += 1
            elif estado == "Expirado":
                ProyectosExpirados += 1

        print(f"{ProyectosActivos:<10}{ProyectosCompletados:<15}{ProyectosExpirados:<15}{len(proyecto[2]):<10}")
        print()
        print("1. Seleccionar proyecto")
        print("0. Volver")
        opcion = input("ingrese una opcion para continuar: ")
        if opcion == "1":
            while p2:
                clearConsole()
                print("Menu > Stats > Stats de Proyectos > *Seleccionar Proyecto*")
                print()
                mostrarListaProyectos(ListaProyectos)
                
                try:   
                    id = int(input("Ingrese el ID del proyecto(0 para cancelar): "))
                    for proyecto in ListaProyectos:    
                        if id == 0:
                            input("Operacion cancelada")
                            p2 = False

                        elif id == proyecto[0]:
                            clearConsole()
                            tareasActivas = 0
                            tareasCompletadas = 0
                            tareasExpiradas = 0
                            for tarea in proyecto[2]:
                                if tarea[4] == "Activo":
                                    tareasActivas += 1
                                elif tarea[4] == "Completado":
                                    tareasCompletadas += 1
                                elif tarea[4] == "Expirado":
                                    tareasExpiradas += 1
                            

                            print(f"=== Stats del Proyecto: {proyecto[1]} ===")
                            print()
                            print(f"{'Tareas Activas':<17}{'Tareas Completadas':<20}{'Tareas Expiradas':<20}")
                            print("-" * 51)
                            print(f"{tareasActivas:<17}{tareasCompletadas:<20}{tareasExpiradas:<20}")
                            print()
                            input("Ingrese cualquier opcion para volver...")
                            p2 = False

                        elif id != proyecto[0]:
                            print()
                            input("ID invalido. Intente nuevamente.")
                            
                except ValueError:
                    print()
                    input("Opcion invalida. Intente nuevamente.")
                    
        elif opcion == "0":
            input("Operacion cancelada")
            p1 = False        
        else:
            print()
            input("Opcion invalida. Intente nuevamente.")

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
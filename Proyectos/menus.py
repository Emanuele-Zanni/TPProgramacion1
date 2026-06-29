from General.clearConsole import *
from Proyectos.funciones import *
from Tareas.funciones import *
from Tareas.menus import *
from Database.usuarios import *


def imprimirMenuProyectos(ListaProyectos, ListaUsuarios, credencial):
    activo = True
    while activo:
        clearConsole()
        print("\033[33m[Menu Principal > *Proyectos*]\033[0m")
        print("")

        if credencial["clearance"] == 0:
            print("1. Ver proyectos")
            print("0. Volver")
            print()
            opcion = input("â€¢ Seleccione una opcion: ")
            if opcion == "1":
                seleccionar_proyecto(ListaProyectos, ListaUsuarios, credencial)
            elif opcion == "0":
                activo = False
            else:
                print()
                input("\033[31m[ERROR] Opcion invalida. Intente nuevamente.\033[0m")

        elif credencial["clearance"] == 1:
            print("1. Ver proyectos")
            print("0. Volver")
            print()
            opcion = input("â€¢ Seleccione una opcion: ")
            if opcion == "1":
                seleccionar_proyecto(ListaProyectos, ListaUsuarios, credencial)
            elif opcion == "0":
                activo = False
            else:
                input("\033[31m[ERROR] Opcion invalida. Intente nuevamente.\033[0m")

        else:
            print("1. Ver proyectos")
            print("2. Crear Proyecto")
            print("3. Editar Proyecto")
            print("4. Eliminar Proyecto")
            print("0. Volver")
            print()
            opcion = input("â€¢ Seleccione una opcion: ")
            if opcion == "1":
                seleccionar_proyecto(ListaProyectos, ListaUsuarios, credencial)
            elif opcion == "2":
                crear_proyecto(ListaProyectos, ListaUsuarios, credencial)
            elif opcion == "3":
                editar_proyecto(ListaProyectos, ListaUsuarios, credencial)
            elif opcion == "4":
                eliminar_proyecto(ListaProyectos)
            elif opcion == "0":
                activo = False
            else:
                input("\033[31m[ERROR] Opcion invalida. Intente nuevamente.\033[0m")


def imprimirMenuSeleccionarProyecto(proyecto):
    activo = True
    while activo:
        clearConsole()
        print("\033[33m[Menu principal > Proyectos > Seleccionar Proyectos > *Proyecto Seleccionado*]\033[0m")
        # print()
        print(f" {''}*14 === {proyecto[1]} ===")
        print(
            f"\033[36mID:\033[0m {proyecto[0]} | "
            f"\033[36mStatus:\033[0m {proyecto[5]} | "
            f"\033[36mFecha Inicio/Final:\033[0m {proyecto[3]} - {proyecto[4]}"
        )
        print("")

        for tarea in proyecto[2]:
            print(tarea)

        print("1. Ver tarea")
        print("2. Crear tarea")
        print("3. Editar tarea")
        print("4. Eliminar tarea")
        print("5. Asignar tareas")
        print("0. Volver atras")
        print()
        opcion = input("â€¢ Seleccione una opcion: ")
        if opcion == "1":
            ver_tareas(proyecto[2])
        elif opcion == "2":
            crear_tarea(proyecto[2])
        elif opcion == "3":
            editar_tarea(proyecto[2])
        elif opcion == "4":
            eliminar_tarea(proyecto[2])
        elif opcion == "5":
            ListaUsuariosFalsa = [1, 2, 3]
            asignar_tarea_integrante(proyecto[2], ListaUsuariosFalsa)
        elif opcion == "0":
            activo = False
        else:
            input("\033[31m[ERROR] Opcion invalida. Intente nuevamente.\033[0m")

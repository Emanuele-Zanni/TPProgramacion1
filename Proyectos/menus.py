from General.clearConsole import *
from Proyectos.funciones import *


def imprimirMenuProyectos(ListaProyectos):
    on = True
    while on:
        clearConsole()
        print("[Menu Principal > *Proyectos*]")
        print("")
        print("1. Ver Proyectos")
        print("2. Seleccionar Proyecto")
        print("3. Crear Proyecto")
        print("4. Editar Proyecto")
        print("5. Eliminar Proyecto")
        print("6. Volver atras")
        print("")
        opcion=input("Seleccione una opcion: ")
        if opcion=="1":
            ver_proyectos(ListaProyectos)
        elif opcion=="2":
            seleccionar_proyecto(ListaProyectos)
        elif opcion=="3":
            crear_proyecto(ListaProyectos)
        elif opcion=="4":
            editar_proyecto(ListaProyectos)
        elif opcion=="5":
            eliminar_proyecto(ListaProyectos)
        elif opcion=="6":
            on = False
        else:
            print("")
            input("[ERROR] Opcion invalida. Intente nuevamente.")
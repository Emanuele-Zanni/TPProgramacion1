from General.clearConsole import *
from Proyectos.funciones import *


def imprimirMenuProyectos(ListaProyectos):
    activo=True

    while activo:
        clearConsole()
        print("[Menu Principal > *Proyectos*]")
        print("")
        print("1. Ver proyectos")
        print("2. Selecciona Proyecto")
        print("3. Crear Proyecto")
        print("4. Editar Proyecto")
        print("5. Eliminar Proyecto")
        print("0. Volver")
        opcion=input("Seleccione una opcion: ")
        if opcion=="1":
            clearConsole()
            ver_proyectos(ListaProyectos)
            input("Aprete ENTER para continuar...")
        elif opcion=="2":
            clearConsole()
            seleccionar_proyecto(ListaProyectos)
            input("Aprete ENTER para continuar...")
        elif opcion=="3":
            clearConsole()
            crear_proyecto(ListaProyectos)
            input("Aprete ENTER para continuar...")
        elif opcion=="4":
            clearConsole()
            editar_proyecto(ListaProyectos)
            input("Aprete ENTER para continuar...")
        elif opcion=="5":
            clearConsole()
            eliminar_proyecto(ListaProyectos)
            input("Aprete ENTER para continuar...")
        elif opcion=="0":

            activo=False
        else:
            print("Opcion invalida. Intente nuevamente.")
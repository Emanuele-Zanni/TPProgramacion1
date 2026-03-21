from General.clearConsole import *
from Proyectos.funciones import *


def imprimirMenuProyectos(ListaProyectos):
    clearConsole()
    print("1. Ver proyectos")
    print("2. Crear Proyecto")
    print("3. Editar Proyecto")
    print("4. Eliminar Proyecto")
    opcion=input("Seleccione una opcion: ")
    if opcion=="1":
        ver_proyectos(ListaProyectos)
    elif opcion=="2":
        crear_proyecto(ListaProyectos)
    elif opcion=="3":
        editar_proyecto(ListaProyectos)
    elif opcion=="4":
        eliminar_proyecto(ListaProyectos)
    else:
        print("Opcion invalida. Intente nuevamente.")
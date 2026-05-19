from Tareas.funciones import *
from General.clearConsole import *


def imprimirMenuTareas(ListaTareas):
    activo=True
    
    while activo:
        print("1. Ver tarea")
        print("2. Crear tarea")
        print("3. Editar tarea")
        print("4. Eliminar tarea")
        print("0. Volver atras")
        opcion=input("Seleccione una opcion: ")
        if opcion=="1":
            ver_tareas(ListaTareas)
        elif opcion=="2":
            crear_tarea(ListaTareas)
        elif opcion=="3":
            editar_tarea(ListaTareas)
        elif opcion=="4":
            eliminar_tarea(ListaTareas)
        elif opcion=="0":
            activo=False
        else:
            input("\033[31m[ERROR] Opcion invalida. Intente nuevamente.\033[0m")

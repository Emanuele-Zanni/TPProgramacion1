from Tareas.funciones import *
from General.clearConsole import *

def imprimirMenuTareas(ListaTareas):
    clearConsole()
    print("[Menu Principal > Tareas]")
    print("")
    print("1. Ver tarea")
    print("2. Crear tarea")
    print("3. Editar tarea")
    print("4. Eliminar tarea")
    print("")
    opcion=input("Seleccione una opcion: ")
    if opcion=="1":
        ver_tareas(ListaTareas)
    elif opcion=="2":
        crear_tarea(ListaTareas)
    elif opcion=="3":
        editar_tarea(ListaTareas)
    elif opcion=="4":
        eliminar_tarea(ListaTareas)
    else:
        print("Opcion invalida. Intente nuevamente.")
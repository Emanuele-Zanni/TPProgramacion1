from Tareas.funciones import *
from General.clearConsole import *

def imprimirMenuTareas(ListaTareas):
    activo=True
    
    while activo:
        clearConsole()
        print("[Menu Principal > Tareas]")
        print("")
        print("1. Ver tarea")
        print("2. Crear tarea")
        print("3. Editar tarea")
        print("4. Eliminar tarea")
        print("0. Volver atras")
        opcion=input("Seleccione una opcion: ")
        if opcion=="1":
            clearConsole()
            ver_tareas(ListaTareas)
            input("Aprete ENTER para continuar...")
        
        elif opcion=="2":
            clearConsole()
            crear_tarea(ListaTareas)
            input("Aprete ENTER para continuar...")

        elif opcion=="3":
            clearConsole()
            editar_tarea(ListaTareas)
            input("Aprete ENTER para continuar...")

        elif opcion=="4":
            clearConsole()
            eliminar_tarea(ListaTareas)
            input("Aprete ENTER para continuar...")

        elif opcion=="0":
            activo=False
            
        else:
            print("Opcion invalida. Intente nuevamente.")
from General.clearConsole import *
from Proyectos.funciones import *
from Tareas.funciones import *
from Tareas.menus import *
from Database.dataBase import *


def imprimirMenuProyectos(ListaProyectos, basico):
    activo=True
    while activo:
        clearConsole()
        print("[Menu Principal > *Proyectos*]")
        print("")
        if basico==False:

            print("1. Ver proyectos")
            print("2. Selecciona Proyecto")
            print("3. Crear Proyecto")
            print("4. Editar Proyecto")
            print("5. Eliminar Proyecto")
            print("0. Volver")
            opcion=input("Seleccione una opcion: ")
            if opcion=="1":
                ver_proyectos(ListaProyectos)
            elif opcion=="2":
                seleccionar_proyecto(ListaProyectos)
            elif opcion=="3":
                crear_proyecto(ListaProyectos)
            elif opcion=="4":
                #! Verificar esta funcion para no modificar cosas de TAREA
                editar_proyecto(ListaProyectos)
            elif opcion=="5":
                eliminar_proyecto(ListaProyectos)
            elif opcion=="0":
                activo=False
            else:
                print("Opcion invalida. Intente nuevamente.")
        
        else:
            clearConsole()
            print("[Menu Principal > *Proyectos*]")
            print("")
            print("1. Ver proyectos")
            print("2. Selecciona Proyecto")
            print("0. Volver")
            opcion=input("Seleccione una opcion: ")
            if opcion=="1":
                ver_proyectos(ListaProyectos)
            elif opcion=="2":
                seleccionar_proyecto(ListaProyectos)
            elif opcion=="0":
                activo=False
            else:
                print("Opcion invalida. Intente nuevamente.")





def imprimirMenuSeleccionarProyecto(proyecto): 
    clearConsole()
    print("[Menu principal > Proyectos > *Proyecto Seleccionado*]")
    print() 
    print(f"=== {proyecto[1]} ===")
    print(f"ID: {proyecto[0]} | Status: {proyecto[5]} | Fecha Inicio/Final: {proyecto[3]} - {proyecto[4]}")
    print("")
    for tarea in proyecto[2]:
        print(tarea)
    print("---")

    imprimirMenuTareas(ListaTareas)
    # print("1. Ver tareas en LISTA (debug)")
    # print("2. Crear Tarea")
    # print("3. Editar Tarea")
    # print("4. Eliminar Tarea")
    # print("0. Volver Atras")

    # opcion=input("Seleccione una opcion: ")
    # if opcion=="1":
    #     ver_tareas(ListaTareas)
    # elif opcion=="2":
    #     crear_tarea(ListaTareas)
    # elif opcion=="3":
    #     editar_tarea(ListaTareas)
    # elif opcion=="4":
    #     eliminar_tarea(ListaTareas)
    # elif opcion=="0":
    #     activo=False
    # else:
    #     print("Opcion invalida. Intente nuevamente.")
    
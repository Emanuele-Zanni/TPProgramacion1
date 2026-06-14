from General.clearConsole import *
from Proyectos.funciones import *
from Tareas.funciones import *
from Tareas.menus import *
from Database.usuarios import *


def imprimirMenuProyectos(ListaProyectos, credencial):
    activo=True
    while activo:
        clearConsole()
        print("\033[33m[Menu Principal > *Proyectos*]\033[0m")
        print("")

        #? ACCESO COMO INVITADO
        if credencial["clearance"] == 0: 
            print("1. Ver proyectos")
            print("0. Volver")
            print()
            opcion=input("• Seleccione una opcion: ")
            if opcion=="1":
                ver_proyectos(ListaProyectos)
            elif opcion=="0":
                activo=False
            else:
                input("\033[31m[ERROR] Opcion invalida. Intente nuevamente.\033[0m")
        
        #? ACCESO COMO MIEMBRO
        elif credencial["clearance"] == 1:
            print("1. Ver proyectos")
            print("2. Selecciona Proyecto")
            print("0. Volver")
            print()
            opcion=input("• Seleccione una opcion: ")
            if opcion=="1":
                ver_proyectos(ListaProyectos)
            elif opcion=="2":
                seleccionar_proyecto(ListaProyectos,credencial)
            elif opcion=="0":
                activo=False
            else:
                input("\033[31m[ERROR] Opcion invalida. Intente nuevamente.\033[0m")

        #? ACCESO COMO MANAGER / SUPERADMIN
        else:
            print("1. Ver proyectos")
            print("2. Selecciona Proyecto")
            print("3. Crear Proyecto")
            print("4. Editar Proyecto")
            print("5. Eliminar Proyecto")
            print("0. Volver")
            print()
            opcion=input("• Seleccione una opcion: ")
            if opcion=="1":
                ver_proyectos(ListaProyectos)
            elif opcion=="2":
                seleccionar_proyecto(ListaProyectos,credencial)
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
                input("\033[31m[ERROR] Opcion invalida. Intente nuevamente.\033[0m")



def imprimirMenuSeleccionarProyecto(proyecto): 
    activo=True
    while activo:
        clearConsole()
        print("\033[33m[Menu principal > Proyectos > *Proyecto Seleccionado*]\033[0m")
        print() 
        print(f" {""}*14 === {proyecto[1]} ===")
        print(f"ID: {proyecto[0]} | Status: {proyecto[5]} | Fecha Inicio/Final: {proyecto[3]} - {proyecto[4]}")
        print("")

        for tarea in proyecto[2]:
            print(tarea)

        print("1. Ver tarea")
        print("2. Crear tarea")
        print("3. Editar tarea")
        print("4. Eliminar tarea")
        print("5. Asignar tarea")
        print("0. Volver atras")
        print()
        opcion=input("• Seleccione una opcion: ")
        if opcion=="1":
            ver_tareas(proyecto[2])
        elif opcion=="2":
            crear_tarea(proyecto[2])
        elif opcion=="3":
            editar_tarea(proyecto[2])
        elif opcion=="4":
            eliminar_tarea(proyecto[2])
        elif opcion=="5":
            ListaUsuariosFalsa = [1,2,3]
            asignar_tarea_integrante(proyecto[2], ListaUsuariosFalsa)
        elif opcion=="0":
            activo=False
        else:
            input("\033[31m[ERROR] Opcion invalida. Intente nuevamente.\033[0m")

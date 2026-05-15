from Integrantes.funciones import *
from General.clearConsole import *
from Integrantes.funciones import *
from Integrantes.roles import*


def imprimirMenuIntegrantes(ListaIntegrantes,ListaRoles,credencial):
    activo=True
    while activo:
        clearConsole()
        print("[Menu Principal > *Integrantes*]")
        print()
        if credencial["clearance"] < 2: 
            print("1. Ver integrantes")
            print("0. Volver atras")
            opcion=input("Seleccione una opcion: ")
            if opcion=="1":
                ver_integrantes(ListaIntegrantes)
            elif opcion == "0":
                activo=False
            else:
                print()
                input("Opcion invalida. Intente nuevamente.")
        else:
            print("1. Ver integrantes")
            print("2. Agregar integrante")
            print("3. Editar integrante")
            print("4. Eliminar integrante")
            print("5. Gestionar roles")
            print("0. Volver atras")
            opcion=input("Seleccione una opcion: ")
            if opcion=="1":
                ver_integrantes(ListaIntegrantes)
            elif opcion=="2":
                agregar_integrante(ListaIntegrantes, ListaRoles)
            elif opcion=="3":
                editar_integrante(ListaIntegrantes,ListaRoles)
            elif opcion=="4":
                eliminar_integrante(ListaIntegrantes)
            elif opcion=="5":
                imprimirMenuRoles(ListaRoles,credencial)
            elif opcion == "0":
                activo=False
            else:
                print()
                input("Opcion invalida. Intente nuevamente.")

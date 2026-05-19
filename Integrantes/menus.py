from Integrantes.funciones import *
from General.clearConsole import *
from Integrantes.funciones import *
from Integrantes.roles import*


def imprimirMenuIntegrantes(ListaUsuarios,ListaRoles,credencial):
    activo=True
    while activo:
        clearConsole()
        print("[Menu Principal > *Personal*]")
        print()
        if credencial["clearance"] < 2: 
            print("1. Ver integrantes")
            print("0. Volver atras")
            print()
            opcion=input("• Seleccione una opcion: ")
            if opcion=="1":
                ver_integrantes(ListaUsuarios)
            elif opcion == "0":
                activo=False
            else:
                print()
                input("[ERROR] Opcion invalida. Intente nuevamente.")
        elif credencial["clearance"] < 3:
            print("1. Ver integrantes")
            print("2. Editar integrante")
            print("3. Gestionar roles")
            print("0. Volver atras")
            print()
            opcion=input("• Seleccione una opcion: ")
            if opcion=="1":
                ver_integrantes(ListaUsuarios)
            elif opcion=="2":
                editar_integrante(ListaUsuarios,ListaRoles)
            elif opcion=="3":
                imprimirMenuRoles(ListaRoles, credencial["clearance"] >= 2)
            elif opcion == "0":
                activo=False
            else:
                print()
                input("[ERROR] Opcion invalida. Intente nuevamente.")
        else:
            print("1. Ver integrantes")
            print("2. Editar integrante")
            print("3. Eliminar integrante")
            print("4. Gestionar roles")
            print("5. Registrar nuevo usuario")
            print("0. Volver atras")
            print()
            opcion=input("• Seleccione una opcion: ")
            if opcion=="1":
                ver_integrantes(ListaUsuarios)
            elif opcion=="2":
                editar_integrante(ListaUsuarios,ListaRoles)
            elif opcion=="3":
                eliminar_integrante(ListaUsuarios)
            elif opcion=="4":
                imprimirMenuRoles(ListaRoles, credencial["clearance"] >= 2)
            elif opcion=="5":
                signUp(ListaUsuarios, ListaRoles)
            elif opcion == "0":
                activo=False
            else:
                print()
                input("[ERROR] Opcion invalida. Intente nuevamente.")

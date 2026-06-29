from Integrantes.funciones import *
from General.clearConsole import *
from Integrantes.funciones import *
from Integrantes.roles import*


def imprimirMenuIntegrantes(ListaUsuarios,ListaRoles,credencial):
    activo=True
    while activo:
        clearConsole()
        print("\033[33m[Menu Principal > *Personal*]\033[0m")
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
                # input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
            else:
                print()
                input("\033[31m[ERROR] Opcion invalida. Intente nuevamente.\033[0m")
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
                imprimirMenuRoles(ListaRoles, credencial)
            elif opcion == "0":
                activo=False
                # input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
            else:
                print()
                input("\033[31m[ERROR] Opcion invalida. Intente nuevamente.\033[0m")
        else:
            print("1. Ver integrantes")
            print("2. Editar integrante")
            print("3. Eliminar integrante")
            print("4. Gestionar roles")
            print("5. Registrar nuevo usuario (Sing Up)")
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
                imprimirMenuRoles(ListaRoles, credencial)
            elif opcion=="5":
                signUp(ListaUsuarios, ListaRoles,True,False)
            elif opcion == "0":
                activo=False
                # input("\033[93m[CANCELADO] Operacion cancelada\033[0m")
            else:
                print()
                input("\033[31m[ERROR] Opcion invalida. Intente nuevamente.\033[0m")
